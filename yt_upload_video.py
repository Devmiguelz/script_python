import os
import pickle
import random
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Permisos necesarios
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Etiquetas predefinidas para videos de héroes Marvel
TAGS_MARVEL = [
    "Marvel", "Avengers", "Iron Man", "Captain America", "Thor",
    "Hulk", "Black Widow", "Spider-Man", "Doctor Strange",
    "Guardians of the Galaxy", "superhero", "epic", "action",
    "comics", "MCU", "Marvel Studios", "battle", "fight", "scene"
]

def authenticate_youtube():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file("credentials/client_secret.json", SCOPES)
        creds = flow.run_console()  # Esto abrirá un enlace para autorizar
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("youtube", "v3", credentials=creds)

def generate_video_filename():
    now = datetime.now()
    return f"video_{now.strftime('%Y%m%d_%H%M%S')}.mp4"

def upload_video(youtube, video_file, title, description, category_id="20", privacy_status="public"):
    # Elegir aleatoriamente entre 5 y 10 tags de TAGS_MARVEL
    tags = random.sample(TAGS_MARVEL, k=random.randint(5, 10))

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
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

    video_id = response["id"]
    print(f"Video subido con ID: {video_id}")
    print(f"Tags utilizadas: {tags}")

if __name__ == "__main__":
    youtube = authenticate_youtube()
    
    # Generar nombre de archivo de video automáticamente
    video_file = generate_video_filename()
    
    # Aquí asumimos que el archivo ya existe con ese nombre
    # Si lo generas desde algún editor, asegúrate de que coincida
    upload_video(
        youtube,
        video_file=video_file,
        title="Héroes de Marvel Épicos",
        description="Disfruta de los mejores momentos y batallas de tus héroes favoritos de Marvel. #Marvel #Avengers #Epic",
        category_id="20",  # Gaming/Entretenimiento
        privacy_status="public"
    )
