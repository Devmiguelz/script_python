import requests
from bs4 import BeautifulSoup

url = input("Ingresa el link del video de Facebook: ")
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

metas = soup.find_all("meta")
for m in metas:
    if m.get("property") in ["og:title", "og:description", "og:image"]:
        print(m.get("property"), ":", m.get("content"))
