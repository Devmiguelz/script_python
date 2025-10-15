import requests
from bs4 import BeautifulSoup
import csv
import json
import time

class CinecalidadScraper:
    def __init__(self):
        self.base_url = "https://cinecalidad.bar"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    
    def extraer_peliculas(self, url=None, pagina=1):
        """
        Extrae información de las películas de la página principal o una página específica
        """
        if url is None:
            if pagina == 1:
                url = self.base_url
            else:
                url = f"{self.base_url}/page/{pagina}/"
        
        try:
            print(f"Scrapeando: {url}")
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Encontrar todos los artículos de películas
            peliculas = soup.find_all('article', class_='tposty')
            
            datos_peliculas = []
            
            for pelicula in peliculas:
                try:
                    # Extraer el enlace
                    enlace_tag = pelicula.find('a', class_='absolute')
                    enlace = enlace_tag['href'] if enlace_tag else None
                    
                    # Extraer el título
                    titulo_span = pelicula.find('span', class_='sr-only')
                    titulo = titulo_span.text.strip() if titulo_span else None
                    
                    # Extraer la imagen
                    img_tag = pelicula.find('img')
                    imagen = img_tag['src'] if img_tag else None
                    
                    # Extraer calidad y año
                    calidad_tag = pelicula.find('span', class_='quality')
                    calidad = calidad_tag.text.strip() if calidad_tag else None
                    
                    año_tag = pelicula.find('span', class_='year')
                    año = año_tag.text.strip() if año_tag else None
                    
                    # Extraer descripción
                    desc_tag = pelicula.find('p', class_='text-sm opacity-70')
                    descripcion = desc_tag.text.strip() if desc_tag else None
                    
                    # Extraer géneros
                    generos_container = pelicula.find('p', class_=['absolute', 'bottom-0'])
                    generos = []
                    if generos_container:
                        generos_links = generos_container.find_all('a')
                        generos = [g.text.strip() for g in generos_links]
                    
                    pelicula_data = {
                        'titulo': titulo,
                        'enlace': enlace,
                        'imagen': imagen,
                        'calidad': calidad,
                        'año': año,
                        'descripcion': descripcion,
                        'generos': generos if generos else []
                    }
                    
                    datos_peliculas.append(pelicula_data)
                    
                except Exception as e:
                    print(f"Error al extraer película: {e}")
                    continue
            
            print(f"✓ {len(datos_peliculas)} películas extraídas de la página {pagina}")
            return datos_peliculas
            
        except Exception as e:
            print(f"Error al hacer scraping: {e}")
            return []
    
    def extraer_multiples_paginas(self, num_paginas=3):
        """
        Extrae películas de múltiples páginas
        """
        todas_peliculas = []
        
        for pagina in range(1, num_paginas + 1):
            print(f"\n{'='*60}")
            print(f"Página {pagina} de {num_paginas}")
            print('='*60)
            
            peliculas = self.extraer_peliculas(pagina=pagina)
            todas_peliculas.extend(peliculas)
            
            # Pausa entre páginas para ser respetuoso
            if pagina < num_paginas:
                time.sleep(2)
        
        return todas_peliculas

    def guardar_json(self, datos, archivo='peliculas_cinecalidad.json'):
        """
        Guarda los datos en un archivo JSON
        """
        if not datos:
            print("No hay datos para guardar")
            return
        
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
        
        print(f"✓ Datos guardados en '{archivo}'")
    
    def mostrar_peliculas(self, datos, limite=5):
        """
        Muestra las películas extraídas en la consola
        """
        print(f"\n{'='*80}")
        print(f"PELÍCULAS ENCONTRADAS (Mostrando {min(limite, len(datos))} de {len(datos)})")
        print('='*80)
        
        for i, pelicula in enumerate(datos[:limite], 1):
            print(f"\n{i}. {pelicula['titulo']}")
            print(f"   Año: {pelicula['año']} | Calidad: {pelicula['calidad']}")
            print(f"   Géneros: {pelicula['generos']}")
            print(f"   URL: {pelicula['enlace']}")
            if pelicula['descripcion']:
                desc = pelicula['descripcion'][:100] + "..." if len(pelicula['descripcion']) > 100 else pelicula['descripcion']
                print(f"   Descripción: {desc}")

# Ejemplo de uso
if __name__ == "__main__":
    scraper = CinecalidadScraper()
    
    print("🎬 SCRAPER DE CINECALIDAD")
    print("="*80)
    
    # Opción 1: Extraer películas de una sola página
    print("\n📄 Extrayendo películas de la página principal...")
    peliculas = scraper.extraer_peliculas()
    
    # Mostrar resultados
    scraper.mostrar_peliculas(peliculas)
    
    # Guardar en JSON
    scraper.guardar_json(peliculas)
    
    # Opción 2: Extraer de múltiples páginas
    print("\n" + "="*80)
    respuesta = input("\n¿Quieres extraer de múltiples páginas? (s/n): ").lower()
    
    if respuesta == 's':
        try:
            num_paginas = int(input("¿Cuántas páginas quieres scrapear? (1-79): "))
            if 1 <= num_paginas <= 79:
                print(f"\n📚 Extrayendo películas de {num_paginas} páginas...")
                todas_peliculas = scraper.extraer_multiples_paginas(num_paginas=num_paginas)
                scraper.mostrar_peliculas(todas_peliculas, limite=15)
                scraper.guardar_json(todas_peliculas, f'peliculas_{num_paginas}_paginas.json')
                print(f"\n📊 Total de películas extraídas: {len(todas_peliculas)}")
            else:
                print("⚠️ Número de páginas fuera de rango (1-79)")
        except ValueError:
            print("⚠️ Por favor ingresa un número válido")
    
    print("\n✅ Scraping completado exitosamente!")