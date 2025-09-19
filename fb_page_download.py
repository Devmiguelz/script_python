from yt_dlp import YoutubeDL
import os

def download_facebook_page(page_url, output_dir="fb_videos"):
    """
    Descarga todos los videos públicos de una página de Facebook con numeración 1..N
    """
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        "outtmpl": f"{output_dir}/%(autonumber)03d_%(title).50s.%(ext)s",
        "format": "best",        # mejor calidad
        "noplaylist": False,     # permite listas de videos
        "autonumber_start": 1,   # empieza numeración en 1
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([page_url])


if __name__ == "__main__":
    fb_page = input("Ingresa la URL de la página de Facebook: ")
    download_facebook_page(fb_page)
