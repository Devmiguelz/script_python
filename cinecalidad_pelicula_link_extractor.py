import requests
from bs4 import BeautifulSoup
import json
import csv
import time
from urllib.parse import urljoin, urlparse
import base64

class AdvancedLinksExtractor:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
    
    def cargar_peliculas_json(self, archivo_json):
        """Carga películas desde JSON"""
        try:
            with open(archivo_json, 'r', encoding='utf-8') as f:
                peliculas = json.load(f)
            print(f"✓ {len(peliculas)} películas cargadas desde {archivo_json}")
            return peliculas
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo {archivo_json}")
            return []
    
    def extraer_player_url(self, url_pelicula):
        """
        Extrae la URL del iframe player desde la página de la película
        """
        try:
            response = self.session.get(url_pelicula, headers=self.headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Buscar el iframe
            iframe = soup.find('iframe')
            if iframe and 'src' in iframe.attrs:
                player_url = iframe['src']
                print(f"  ✓ Player URL encontrada: {player_url}")
                return player_url
            else:
                print("  ⚠️ No se encontró iframe")
                return None
                
        except Exception as e:
            print(f"  ❌ Error extrayendo player URL: {e}")
            return None
    
    def extraer_servidores_video(self, player_url, referer_url):
        """
        Accede al iframe del player y extrae los servidores de video disponibles
        """
        try:
            # Headers específicos con referer
            headers_player = self.headers.copy()
            headers_player['Referer'] = referer_url
            
            print(f"  → Accediendo al player...")
            response = self.session.get(player_url, headers=headers_player, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            servidores = []
            
            # Buscar todos los botones de servidor (los <li> con onclick)
            botones_servidor = soup.find_all('li', onclick=True)
            
            for boton in botones_servidor:
                try:
                    # Extraer el onclick
                    onclick = boton.get('onclick', '')
                    
                    # El onclick contiene: go_to_player('/r.php?id=...&hash=...')
                    if 'go_to_player' in onclick:
                        # Extraer la URL entre comillas
                        import re
                        match = re.search(r"go_to_player\('([^']+)'\)", onclick)
                        if match:
                            ruta_relativa = match.group(1)
                            
                            # Construir URL completa
                            base_url = urlparse(player_url)
                            url_completa = f"{base_url.scheme}://{base_url.netloc}{ruta_relativa}"
                            
                            # Extraer nombre del servidor
                            span = boton.find('span')
                            nombre_servidor = span.text.strip() if span else 'Desconocido'
                            
                            # Extraer descripción
                            p = boton.find('p')
                            descripcion = p.text.strip() if p else ''
                            
                            servidor_info = {
                                'nombre': nombre_servidor,
                                'descripcion': descripcion,
                                'url_redirect': url_completa,
                                'ruta_relativa': ruta_relativa
                            }
                            
                            servidores.append(servidor_info)
                            
                except Exception as e:
                    print(f"    Error extrayendo servidor: {e}")
                    continue
            
            print(f"  ✓ {len(servidores)} servidores encontrados")
            return servidores
            
        except Exception as e:
            print(f"  ❌ Error accediendo al player: {e}")
            return []
    
    def obtener_url_final_video(self, redirect_url, referer_url):
        """
        Sigue la redirección de /r.php para obtener la URL final del video
        """
        try:
            headers_redirect = self.headers.copy()
            headers_redirect['Referer'] = referer_url
            
            # Hacer petición pero NO seguir redirects automáticamente
            response = self.session.get(
                redirect_url, 
                headers=headers_redirect, 
                timeout=15,
                allow_redirects=False
            )
            
            # Si hay redirección (código 3xx)
            if 300 <= response.status_code < 400:
                url_final = response.headers.get('Location')
                return url_final
            
            # Si no hay redirección, intentar extraer del HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            iframe = soup.find('iframe')
            if iframe and 'src' in iframe.attrs:
                return iframe['src']
            
            return None
            
        except Exception as e:
            print(f"    Error obteniendo URL final: {e}")
            return None
    
    def procesar_pelicula(self, pelicula):
        """
        Procesa una película completa: extrae player y todos los servidores
        """
        titulo = pelicula.get('titulo', 'Desconocido')
        url_pelicula = pelicula.get('enlace')
        
        if not url_pelicula:
            print(f"  ⚠️ {titulo}: No tiene URL")
            return None
        
        resultado = {
            'titulo': titulo,
            'año': pelicula.get('año'),
            'calidad': pelicula.get('calidad'),
            'generos': pelicula.get('generos'),
            'url_pelicula': url_pelicula,
            'servidores': []
        }
        
        # 1. Extraer URL del player
        player_url = self.extraer_player_url(url_pelicula)
        if not player_url:
            return resultado
        
        resultado['player_url'] = player_url
        
        # 2. Extraer servidores del player
        servidores = self.extraer_servidores_video(player_url, url_pelicula)
        
        # 3. Opcionalmente, obtener URLs finales (esto puede ser lento)
        # for servidor in servidores:
        #     url_final = self.obtener_url_final_video(
        #         servidor['url_redirect'], 
        #         player_url
        #     )
        #     if url_final:
        #         servidor['url_video_final'] = url_final
        
        resultado['servidores'] = servidores
        
        return resultado
    
    def procesar_peliculas(self, archivo_json, limite=None, delay=3):
        """
        Procesa múltiples películas
        """
        peliculas = self.cargar_peliculas_json(archivo_json)
        
        if not peliculas:
            return []
        
        if limite:
            peliculas = peliculas[:limite]
        
        resultados = []
        total = len(peliculas)
        
        print(f"\n{'='*80}")
        print(f"Procesando {total} películas...")
        print('='*80)
        
        for i, pelicula in enumerate(peliculas, 1):
            print(f"\n[{i}/{total}] {pelicula.get('titulo', 'Sin título')}")
            
            resultado = self.procesar_pelicula(pelicula)
            
            if resultado:
                # Mostrar servidores encontrados
                if resultado.get('servidores'):
                    for servidor in resultado['servidores']:
                        print(f"    ✓ {servidor['nombre']} - {servidor['descripcion']}")
                else:
                    print("    ⚠️ No se encontraron servidores")
                
                resultados.append(resultado)
            
            # Pausa entre películas
            if i < total:
                time.sleep(delay)
        
        return resultados
    
    def guardar_resultados(self, resultados, prefijo='peliculas_servidores'):
        """
        Guarda resultados en JSON y CSV
        """
        if not resultados:
            print("No hay resultados para guardar")
            return
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        # Guardar JSON completo
        archivo_json = f'{prefijo}_{timestamp}.json'
        with open(archivo_json, 'w', encoding='utf-8') as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)
        print(f"\n✓ JSON guardado: {archivo_json}")
        
        # Guardar CSV con servidores
        archivo_csv = f'{prefijo}_{timestamp}.csv'
        datos_csv = []
        
        for pelicula in resultados:
            base = {
                'titulo': pelicula.get('titulo'),
                'año': pelicula.get('año'),
                'calidad': pelicula.get('calidad'),
                'generos': pelicula.get('generos'),
                'url_pelicula': pelicula.get('url_pelicula'),
                'player_url': pelicula.get('player_url')
            }
            
            if pelicula.get('servidores'):
                for servidor in pelicula['servidores']:
                    fila = base.copy()
                    fila['servidor_nombre'] = servidor.get('nombre')
                    fila['servidor_descripcion'] = servidor.get('descripcion')
                    fila['servidor_url'] = servidor.get('url_redirect')
                    fila['url_video_final'] = servidor.get('url_video_final', 'N/A')
                    datos_csv.append(fila)
            else:
                datos_csv.append(base)
        
        if datos_csv:
            with open(archivo_csv, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=datos_csv[0].keys())
                writer.writeheader()
                writer.writerows(datos_csv)
            print(f"✓ CSV guardado: {archivo_csv}")
        
        # Guardar resumen legible
        archivo_txt = f'{prefijo}_{timestamp}.txt'
        with open(archivo_txt, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("SERVIDORES DE VIDEO EXTRAÍDOS\n")
            f.write("=" * 80 + "\n\n")
            
            for pelicula in resultados:
                f.write(f"\n{'='*60}\n")
                f.write(f"PELÍCULA: {pelicula.get('titulo')}\n")
                f.write(f"Año: {pelicula.get('año')} | Calidad: {pelicula.get('calidad')}\n")
                f.write(f"URL: {pelicula.get('url_pelicula')}\n")
                f.write(f"Player: {pelicula.get('player_url', 'N/A')}\n")
                f.write(f"{'='*60}\n\n")
                
                if pelicula.get('servidores'):
                    f.write("SERVIDORES DISPONIBLES:\n\n")
                    for idx, servidor in enumerate(pelicula['servidores'], 1):
                        f.write(f"{idx}. {servidor['nombre']}\n")
                        f.write(f"   Descripción: {servidor['descripcion']}\n")
                        f.write(f"   URL: {servidor['url_redirect']}\n")
                        if servidor.get('url_video_final'):
                            f.write(f"   Video final: {servidor['url_video_final']}\n")
                        f.write("\n")
                else:
                    f.write("No se encontraron servidores\n\n")
        
        print(f"✓ Resumen TXT guardado: {archivo_txt}")

# Ejemplo de uso
if __name__ == "__main__":
    extractor = AdvancedLinksExtractor()
    
    print("🎬 EXTRACTOR AVANZADO DE ENLACES DE VIDEO")
    print("="*80)
    
    # Solicitar archivo JSON
    archivo_json = input("\nArchivo JSON de películas (default: peliculas_cinecalidad.json): ").strip()
    if not archivo_json:
        archivo_json = "peliculas_cinecalidad.json"
    
    # Preguntar cuántas procesar
    print("\n¿Cuántas películas procesar?")
    print("  1. Solo 3 (prueba rápida)")
    print("  2. 10 películas")
    print("  3. 25 películas")
    print("  4. Todas")
    
    opcion = input("\nOpción (1-4): ").strip()
    limite_map = {'1': 3, '2': 10, '3': 25, '4': None}
    limite = limite_map.get(opcion, 3)
    
    if limite:
        print(f"\n⚙️ Procesando {limite} películas...")
    else:
        print("\n⚙️ Procesando TODAS las películas (esto puede tardar)...")
    
    # Procesar
    resultados = extractor.procesar_peliculas(
        archivo_json=archivo_json,
        limite=limite,
        delay=3  # 3 segundos entre películas
    )
    
    if resultados:
        print(f"\n{'='*80}")
        print(f"✅ Completado: {len(resultados)} películas procesadas")
        print('='*80)
        
        # Estadísticas
        total_servidores = sum(len(p.get('servidores', [])) for p in resultados)
        print(f"\n📊 ESTADÍSTICAS:")
        print(f"  - Total servidores encontrados: {total_servidores}")
        print(f"  - Promedio por película: {total_servidores/len(resultados):.1f}")
        
        # Guardar
        extractor.guardar_resultados(resultados)
    else:
        print("\n❌ No se procesó ninguna película")