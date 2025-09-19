import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL

def get_reels_urls(profile_url, cookies_file="cookies.txt"):
    """
    Extrae todos los enlaces de reels de un perfil/página pública de Facebook.
    Usa cookies para obtener el HTML real.
    """
    # Cargar cookies.txt para la petición HTTP
    cookies = {}
    with open(cookies_file, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 7:
                cookies[parts[5]] = parts[6]

    # Descargar el HTML con cookies (así carga los reels)
    resp = requests.get(profile_url, cookies=cookies, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    })
    
    soup = BeautifulSoup(resp.text, "html.parser")
    links = []

    # Buscar todos los <a href="/reel/...">
    for a in soup.find_all("a", href=True):
        if "/reel/" in a["href"]:
            href = a["href"].split("?")[0]  # quitar parámetros como ?s=...
            if href.startswith("http"):
                links.append(href)
            else:
                links.append("https://www.facebook.com" + href)

    return list(set(links))  # eliminar duplicados


def download_facebook_videos(video_urls, cookies_file="cookies.txt", output_dir="fb_videos"):
    """
    Descarga videos de Facebook usando yt-dlp y cookies.
    """
    ydl_opts = {
        "outtmpl": f"{output_dir}/%(autonumber)03d_%(title).50s.%(ext)s",
        "format": "best",
        "cookiefile": cookies_file,
        "autonumber_start": 1
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_urls)


if __name__ == "__main__":
    fb_url = "https://www.facebook.com/profile.php?id=100057065635936&sk=reels_tab"
    reels = get_reels_urls(fb_url)

    print(f"✅ Se encontraron {len(reels)} reels")
    for r in reels:
        print(r)

    if reels:
        download_facebook_videos(reels)
        print("🎉 Descarga completa.")
    else:
        print("⚠️ No se encontraron reels.")
