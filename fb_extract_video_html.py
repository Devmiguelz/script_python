from bs4 import BeautifulSoup

def extract_facebook_links(html: str) -> dict[str, list[str]]:
    soup = BeautifulSoup(html, "html.parser")
    reels = []
    videos = []

    all_links = soup.find_all("a", href=True)
    total = len(all_links)

    for idx, a_tag in enumerate(all_links, start=1):
        href = a_tag["href"]

        # --- Detectar reels ---
        if href.startswith("/reel/") or "/reel/" in href:
            clean_href = href.split("?")[0]
            reels.append(f"https://www.facebook.com{clean_href}")

        # --- Detectar videos ---
        elif "/videos/" in href or "/watch/?" in href:
            clean_href = href.split("?")[0]
            # Si ya es link absoluto lo dejo igual
            if href.startswith("http"):
                videos.append(clean_href)
            else:
                videos.append(f"https://www.facebook.com{clean_href}")

        # Mostrar porcentaje con print
        percent = int((idx / total) * 100)
        print(f" video {idx} de {total}")
        print(f"🔎 Procesando enlaces... {percent}%")

    return {"reels": list(set(reels)), "videos": list(set(videos))}

def save_links_to_txt(links: list[str], filename: str, separator: str = "\n"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(separator.join(links))


# Ejemplo de uso
html = """"""  # aquí metes el HTML copiado de la página

links = extract_facebook_links(html)

save_links_to_txt(links["videos"], "facebook_videos.txt")

print("✅ Links de reels y videos guardados.")