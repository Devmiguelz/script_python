from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import sys

def get_reels_urls(profile_url, scroll_times=5):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # si no quieres que se abra la ventana
    options.add_argument(r"--user-data-dir=C:\Users\oscar\AppData\Local\Google\Chrome\User Data")
    options.add_argument("--profile-directory=Profile 11")  # aquí tu perfil real
    
    # Opciones extra por si acaso
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(profile_url)
    
    links = set()
    for i in range(scroll_times):
        # hacer scroll hacia abajo
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)

        # recolectar enlaces hasta ahora
        anchors = driver.find_elements(By.TAG_NAME, "a")
        for a in anchors:
            href = a.get_attribute("href")
            if href and "/reel/" in href:
                links.add(href.split("?")[0])  # limpiar parámetros

        # mostrar progreso
        progress = int(((i + 1) / scroll_times) * 100)
        sys.stdout.write(f"\r🔄 Progreso: {progress}% | Reels encontrados: {len(links)}")
        sys.stdout.flush()

    driver.quit()
    print()  # salto de línea final
    return list(links)

if __name__ == "__main__":
    profile_url = "https://www.facebook.com/profile.php?id=100057065635936&sk=reels_tab"
    reels = get_reels_urls(profile_url, scroll_times=50)  # ajusta la cantidad de scrolls
    print(f"✅ Total encontrados: {len(reels)} reels")
    with open("reels_links.txt", "w", encoding="utf-8") as f:
        for link in reels:
            f.write(link + "\n")

    print("✅ Links guardados en reels_links.txt")
