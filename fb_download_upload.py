import os
import re
import pickle
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import openai
from openai import OpenAI
import subprocess

# ------------------------------
# CONFIGURACIÓN
# ------------------------------
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
OUTPUT_DIR = "downloads"

client = OpenAI(organization="org-E9G3jzIfVdsd3oGidLqZs2Po")

TAGS_MARVEL = [
    "short", "viral", "viralshort", "marvel", "avengers", "iron man",
    "captain america", "thor", "hulk", "black widow", "spider-man",
    "doctor strange", "guardians of the galaxy", "superhero", "epic",
    "action", "comics", "mcu", "marvel studios", "battle", "fight", "scene"
]

# ------------------------------
# AUTENTICACIÓN YOUTUBE
# ------------------------------
def authenticate_youtube():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials/client_secret.json", SCOPES
        )
        # 🚀 Usa un servidor local para autenticar
        creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)

# ------------------------------
# DESCARGA VIDEO FACEBOOK
# ------------------------------
def download_facebook_video(url, output_dir=OUTPUT_DIR):
    options = {
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "format": "best",
        "cookies": "cookies.txt",
    }
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        print(f"✅ Video descargado: {filename}")
        return filename, info

# ------------------------------
# EXTRAER METADATOS DEL REEL
# ------------------------------
def extract_facebook_metadata(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    meta = {}
    for m in soup.find_all("meta"):
        if m.get("property") in ["og:title", "og:description", "og:image"]:
            meta[m.get("property")] = m.get("content")

    # Extraer valores
    description = meta.get("og:description", "")

    # Eliminar hashtags (#palabra)
    title = re.sub(r"#\S+", "", description).strip()

    thumbnail = meta.get("og:image", None)

    return title, description, thumbnail

# ------------------------------
# TRANSCRIBIR AUDIO DEL VIDEO
# ------------------------------
def transcribe_audio(video_file):
    audio_file = "audios/temp_audio.mp3"

    # 1. Extraer audio con ffmpeg
    subprocess.run([
        "ffmpeg", "-y", "-i", video_file,
        "-vn", "-acodec", "libmp3lame", "-ar", "44100", "-ac", "2",
        audio_file
    ], check=True)

    # 2. Transcribir audio con OpenAI Whisper
    with open(audio_file, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=f
        )
    return transcript.text

# ------------------------------
# GENERAR TITULO Y DESCRIPCIÓN CON IA
# ------------------------------
def suggest_title_description(transcript, fallback_title, fallback_desc):
    prompt = f"""
    Eres un experto en marketing de YouTube.
    Basado en esta transcripción del video: 

    {transcript}

    Y el título inicial: "{fallback_title}"
    Y la descripción inicial: "{fallback_desc}"

    Sugiere 3 títulos virales y 3 descripciones atractivas para Shorts de Marvel.
    Devuelve el resultado en formato:

    TITULOS:
    1. ...
    2. ...
    3. ...

    DESCRIPCIONES:
    1. ...
    2. ...
    3. ...
    """
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ------------------------------
# PARSEAR SUGERENCIAS
# ------------------------------
def parse_suggestions(raw_text):
    titles = []
    descriptions = []
    section = None

    for line in raw_text.splitlines():
        line = line.strip()
        if line.startswith("TITULOS"):
            section = "titles"
        elif line.startswith("DESCRIPCIONES"):
            section = "descriptions"
        elif line and line[0].isdigit():
            text = line.split(".", 1)[1].strip()
            if section == "titles":
                titles.append(text)
            elif section == "descriptions":
                descriptions.append(text)
    return titles, descriptions


# ------------------------------
# LISTAR LA OPCIONES Y ELEGIR
# ------------------------------
def choose_option(options, prompt="Elige una opción: "):
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    choice = int(input(prompt))
    return options[choice - 1]

# ------------------------------
# SUBIR VIDEO A YOUTUBE
# ------------------------------
def upload_video(youtube, video_file, title, description,
                 category_id="22", privacy_status="public"):
    tags = random.sample(TAGS_MARVEL, k=random.randint(5, 10))

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": privacy_status
        }
    }

    media_file = MediaFileUpload(video_file)

    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_file
    ).execute()

    print(f"🚀 Video subido con ID: {response['id']}")
    return response["id"]

# ------------------------------
# MAIN
# ------------------------------
if __name__ == "__main__":
    fb_url = input("Ingresa el link del video de Facebook: ")

    # 1. Descargar video
    video_file, info = download_facebook_video(fb_url)

    # 2. Extraer metadatos
    title, description, thumbnail = extract_facebook_metadata(fb_url)

    print("**********************************")
    print(f"Título detectado: \n{title}")
    print("**********************************")
    print(f"Descripción detectada: \n{description}")
    print("**********************************")

    # 3. Transcribir audio
    print("🎙️ Transcribiendo audio del video...")
    transcript = transcribe_audio(video_file)

    print("🧠 Generando títulos y descripciones sugeridas...")
    # 4. Generar sugerencias con IA
    raw_suggestions = suggest_title_description(transcript, title, description)

    # 5. Parsear sugerencias
    titles, descriptions = parse_suggestions(raw_suggestions)

    # 6. Mostrar y elegir
    print("\n--- Títulos sugeridos ---")
    final_title = choose_option(titles, "Selecciona el título: ")

    print("\n--- Descripciones sugeridas ---")
    final_description = choose_option(descriptions, "Selecciona la descripción: ")

    print(f"\n✅ Usando:\nTítulo: {final_title}\nDescripción: {final_description}")

    # Asignar los finales
    title = final_title
    description = final_description

    # Preguntar si usar título/descripcion personalizados
    custom_title = input("¿Quieres poner un título personalizado? (s/n): ")
    if custom_title.lower() == "s":
        title = input("Escribe tu título: ")

    custom_desc = input("¿Quieres poner una descripción personalizada? (s/n): ")
    if custom_desc.lower() == "s":
        description = input("Escribe tu descripción: ")

    print("**********************************")
    print(f"Título: \n{title}")
    print("**********************************")
    print(f"Descripción: \n{description}")
    print("**********************************")

    # 3. Autenticación YouTube
    #youtube = authenticate_youtube()

    # 4. Subir video con metadatos del Reel o personalizados
    #upload_video(youtube, video_file, title, description)
