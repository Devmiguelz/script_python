from yt_dlp import YoutubeDL

def download_facebook_video(url, output_dir="downloads"):
    """
    Descarga un solo video público de Facebook
    """
    options = {
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",  # carpeta de salida
        "format": "best",  # mejor calidad disponible
    }

    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)  # descarga
        filename = ydl.prepare_filename(info)        # ruta final
        print(f"✅ Video descargado: {filename}")
        return filename

if __name__ == "__main__":
    fb_url = input("Ingresa el link del video de Facebook: ")
    download_facebook_video(fb_url)
