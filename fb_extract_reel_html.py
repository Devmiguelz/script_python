from bs4 import BeautifulSoup

def extract_reel_links(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    full_links = []

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href.startswith("/reel/"):
            clean_href = href.split("?")[0]
            full_links.append(f"https://www.facebook.com{clean_href}")

    return full_links

def save_links_to_txt(links: list[str], filename: str, separator: str = "\n"):
    """
    Guarda los links en un archivo .txt
    :param links: lista de URLs
    :param filename: nombre del archivo .txt
    :param separator: "\n" para línea por línea, "|" para separados por |
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(separator.join(links))

# Ejemplo de uso
html = """"""

reels = extract_reel_links(html)

# Guardar uno debajo del otro
save_links_to_txt(reels, "reels_Short_line.txt", separator="\n")

# Guardar separados por |
save_links_to_txt(reels, "reels_Short_pipe.txt", separator="|")

print("Links guardados en reels_Short_line.txt y reels_Short_pipe.txt")