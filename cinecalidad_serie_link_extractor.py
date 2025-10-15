import requests
from bs4 import BeautifulSoup
import json
import time
import re
from urllib.parse import urljoin, urlparse

class CineCalidadSerieExtractor:
    def __init__(self):
        self.base_url = "https://cinecalidad.bar"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def extraer_datos_serie(self, url_serie, extraer_urls_finales=False):
        """
        Extrae todos los datos de una serie incluyendo episodios y enlaces
        
        Args:
            url_serie (str): URL de la serie (ej: https://cinecalidad.bar/serie/andor-v4/)
            extraer_urls_finales (bool): Si True, extrae las URLs finales de video (más lento)
        
        Returns:
            dict: Diccionario con toda la información de la serie
        """
        try:
            print(f"\n{'='*60}")
            print(f"Extrayendo datos de: {url_serie}")
            print(f"{'='*60}\n")
            
            response = requests.get(url_serie, headers=self.headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extraer información básica de la serie
            serie_info = self._extraer_info_basica(soup)
            
            # Extraer temporadas y episodios
            temporadas = self._extraer_temporadas_episodios(soup)
            
            # Extraer enlaces de cada episodio
            print("\n🎬 Extrayendo enlaces de servidores de cada episodio...\n")
            for temporada in temporadas:
                for episodio in temporada['episodios']:
                    print(f"  → Procesando: {episodio['titulo']}")
                    enlaces = self._extraer_enlaces_episodio(episodio['url'])
                    
                    # Opcionalmente extraer URLs finales
                    if extraer_urls_finales and enlaces:
                        print(f"      → Extrayendo URLs finales...")
                        for servidor in enlaces:
                            if servidor.get('url_redirect'):
                                url_final = self.obtener_url_final_video(
                                    servidor['url_redirect'],
                                    episodio['url']
                                )
                                if url_final:
                                    servidor['url_video_final'] = url_final
                                time.sleep(0.5)
                    
                    episodio['servidores'] = enlaces
                    time.sleep(1)  # Pausa entre peticiones
            
            # Construir el resultado final
            resultado = {
                **serie_info,
                'temporadas': temporadas,
                'url_serie': url_serie
            }
            
            print(f"\n{'='*60}")
            print(f"✓ Extracción completada exitosamente")
            print(f"{'='*60}\n")
            
            return resultado
            
        except Exception as e:
            print(f"❌ Error al extraer datos de la serie: {e}")
            return None
    
    def _extraer_info_basica(self, soup):
        """Extrae la información básica de la serie"""
        info = {}
        
        try:
            # Título
            titulo_tag = soup.find('h1', class_='mb-2')
            info['titulo'] = titulo_tag.text.strip() if titulo_tag else None
            
            # Imagen principal
            img_tag = soup.find('figure', class_='md:col-span-2')
            if img_tag:
                img = img_tag.find('img')
                info['imagen'] = img['src'] if img else None
            
            # Trailer (YouTube)
            trailer_iframe = soup.find('iframe', id='videoPlayer')
            if trailer_iframe and 'src' in trailer_iframe.attrs:
                info['trailer'] = trailer_iframe['src']
            else:
                info['trailer'] = None
            
            # Descripción
            desc_container = soup.find('div', class_='capturar')
            if desc_container:
                desc_p = desc_container.find('p')
                info['descripcion'] = desc_p.text.strip() if desc_p else None
            else:
                info['descripcion'] = None
            
            # Lista de detalles
            aside = soup.find('aside', class_='md:col-span-3')
            if aside:
                ul = aside.find('ul', class_='list-none')
                if ul:
                    items = ul.find_all('li')
                    
                    for item in items:
                        texto = item.text.strip()
                        
                        # Título original
                        if 'Título original' in texto:
                            info['titulo_original'] = texto.replace('Título original', '').strip()
                        
                        # Enlaces TMDB/IMDB
                        if 'Mas detalles en' in texto:
                            tmdb_link = item.find('a', class_='tmdb-s')
                            imdb_link = item.find('a', class_='imdb-s')
                            info['tmdb'] = tmdb_link['href'] if tmdb_link and tmdb_link.get('href') else None
                            info['imdb'] = imdb_link['href'] if imdb_link and imdb_link.get('href') else None
                        
                        # Géneros
                        if 'Géneros' in texto:
                            generos_links = item.find_all('a')
                            info['generos'] = [g.text.strip() for g in generos_links]
            
            print(f"✓ Información básica extraída: {info.get('titulo', 'Sin título')}")
            
        except Exception as e:
            print(f"Error al extraer información básica: {e}")
        
        return info
    
    def _extraer_temporadas_episodios(self, soup):
        """Extrae las temporadas y sus episodios"""
        temporadas = []
        
        try:
            # Buscar el selector de temporadas
            season_selector = soup.find('select', id='season-selector')
            
            if not season_selector:
                print("No se encontró selector de temporadas")
                return temporadas
            
            # Obtener todas las opciones de temporada
            options = season_selector.find_all('option')
            
            print(f"\n📺 Temporadas encontradas: {len(options)}")
            
            for option in options:
                temp_numero = option['value']
                temp_nombre = option.text.strip()
                
                print(f"  → {temp_nombre}")
                
                temporada_data = {
                    'numero': temp_numero,
                    'nombre': temp_nombre,
                    'episodios': []
                }
                
                # Buscar los episodios de esta temporada
                # Los episodios están en divs con clase 'se-a'
                episodes_container = soup.find('div', class_='se-a')
                
                if episodes_container:
                    episodios_list = episodes_container.find_all('li', class_='TPostMve')
                    
                    for ep in episodios_list:
                        article = ep.find('article')
                        if article:
                            link_tag = article.find('a')
                            titulo_tag = article.find('h2', class_='episodiotitle')
                            numero_tag = article.find('span', class_='tilpisode')
                            img_tag = article.find('img')
                            estado_tag = article.find('span', class_='displ')
                            
                            episodio_data = {
                                'numero': numero_tag.text.strip() if numero_tag else None,
                                'titulo': titulo_tag.text.strip() if titulo_tag else None,
                                'url': link_tag['href'] if link_tag else None,
                                'imagen': img_tag['src'] if img_tag else None,
                                'estado': estado_tag.text.strip() if estado_tag else None,
                                'servidores': []  # Se llenará después
                            }
                            
                            temporada_data['episodios'].append(episodio_data)
                    
                    print(f"    ✓ {len(temporada_data['episodios'])} episodios encontrados")
                
                temporadas.append(temporada_data)
            
        except Exception as e:
            print(f"Error al extraer temporadas y episodios: {e}")
        
        return temporadas
    
    def _extraer_enlaces_episodio(self, url_episodio):
        """Extrae los enlaces de servidores de un episodio específico"""
        servidores = []
        
        try:
            response = requests.get(url_episodio, headers=self.headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Buscar el iframe del player
            iframe = soup.find('iframe', class_='absolute')
            
            if iframe and 'src' in iframe.attrs:
                player_url = iframe['src']
                
                # Acceder a la URL del player para obtener los servidores
                # Pasamos la URL del episodio como referer
                servidores = self._extraer_servidores_player(player_url, url_episodio)
            
        except Exception as e:
            print(f"    ⚠️  Error al extraer enlaces: {e}")
        
        return servidores
    
    def _extraer_servidores_player(self, player_url, referer_url):
        """Extrae los servidores disponibles desde el player"""
        servidores = []
        
        try:
            # Headers específicos con referer para evitar 403
            headers_player = self.headers.copy()
            headers_player['Referer'] = referer_url
            
            time.sleep(0.5)  # Pausa pequeña
            response = requests.get(player_url, headers=headers_player, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Buscar los idiomas disponibles
            idiomas = soup.find_all('li', onclick=lambda x: x and 'SelLang' in x)
            
            for idioma_li in idiomas:
                onclick_text = idioma_li.get('onclick', '')
                # Extraer el código de idioma (LAT, SUB, etc.)
                match = re.search(r"'(\w+)'", onclick_text)
                idioma_code = match.group(1) if match else 'UNKNOWN'
                
                # Buscar el contenedor de servidores para este idioma
                clase_servidores = f"OD OD_{idioma_code}"
                servidores_container = soup.find('div', class_=clase_servidores)
                
                if servidores_container:
                    links = servidores_container.find_all('li', onclick=lambda x: x and 'go_to_player' in x)
                    
                    for link in links:
                        servidor_img = link.find('img')
                        servidor_span = link.find('span')
                        servidor_p = link.find('p')
                        
                        onclick_attr = link.get('onclick', '')
                        # Extraer la URL del onclick (ruta relativa)
                        url_match = re.search(r"go_to_player\('([^']+)'\)", onclick_attr)
                        ruta_relativa = url_match.group(1) if url_match else None
                        
                        # Construir URL completa para el redirect
                        url_completa = None
                        if ruta_relativa:
                            base_url = urlparse(player_url)
                            url_completa = f"{base_url.scheme}://{base_url.netloc}{ruta_relativa}"
                        
                        servidor_data = {
                            'idioma': idioma_code,
                            'nombre': servidor_span.text.strip() if servidor_span else None,
                            'descripcion': servidor_p.text.strip() if servidor_p else None,
                            'url_redirect': url_completa,
                            'ruta_relativa': ruta_relativa,
                            'logo': servidor_img['src'] if servidor_img else None
                        }
                        
                        servidores.append(servidor_data)
            
            if servidores:
                print(f"      ✓ {len(servidores)} servidores encontrados")
            
        except Exception as e:
            print(f"      ⚠️  Error al extraer servidores del player: {e}")
        
        return servidores
    
    def obtener_url_final_video(self, redirect_url, referer_url):
        """
        Sigue la redirección de /r.php para obtener la URL final del video
        (Opcional - puede ser lento)
        """
        try:
            headers_redirect = self.headers.copy()
            headers_redirect['Referer'] = referer_url
            
            # Hacer petición pero NO seguir redirects automáticamente
            response = requests.get(
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
            print(f"      ⚠️  Error obteniendo URL final: {e}")
            return None
    
    def guardar_json(self, datos, nombre_archivo='serie_completa.json'):
        """Guarda los datos extraídos en un archivo JSON"""
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
            print(f"\n💾 Datos guardados en: {nombre_archivo}")
            return True
        except Exception as e:
            print(f"❌ Error al guardar JSON: {e}")
            return False


# Ejemplo de uso
if __name__ == "__main__":
    extractor = CineCalidadSerieExtractor()
    
    print("🎬 EXTRACTOR DE SERIES - CINECALIDAD")
    print("="*80)
    
    # URL de la serie a extraer
    url_serie = "https://cinecalidad.bar/serie/la-nueva-brigada/"
    
    # Preguntar si quiere extraer URLs finales
    print("\n¿Desea extraer las URLs finales de video?")
    print("  Nota: Esto hará el proceso MÁS LENTO pero obtendrá las URLs directas")
    print("  1. No - Solo enlaces de servidores (Rápido)")
    print("  2. Sí - Incluir URLs finales de video (Lento)")
    
    opcion = input("\nOpción (1-2): ").strip()
    extraer_urls_finales = (opcion == '2')
    
    if extraer_urls_finales:
        print("\n⚙️ Modo: Extracción completa con URLs finales")
    else:
        print("\n⚙️ Modo: Extracción rápida (solo servidores)")
    
    # Extraer todos los datos
    datos_serie = extractor.extraer_datos_serie(url_serie, extraer_urls_finales)
    
    if datos_serie:
        # Guardar en JSON
        extractor.guardar_json(datos_serie, 'andor_completo.json')
        
        # Mostrar resumen
        print("\n" + "="*60)
        print("RESUMEN DE EXTRACCIÓN")
        print("="*60)
        print(f"Título: {datos_serie.get('titulo')}")
        print(f"Temporadas: {len(datos_serie.get('temporadas', []))}")
        
        total_episodios = sum(len(t['episodios']) for t in datos_serie.get('temporadas', []))
        print(f"Total episodios: {total_episodios}")
        
        total_servidores = sum(
            len(ep['servidores']) 
            for t in datos_serie.get('temporadas', []) 
            for ep in t['episodios']
        )
        print(f"Total enlaces de servidores: {total_servidores}")
        
        if extraer_urls_finales:
            urls_finales = sum(
                1 for t in datos_serie.get('temporadas', []) 
                for ep in t['episodios']
                for srv in ep['servidores']
                if srv.get('url_video_final')
            )
            print(f"URLs finales obtenidas: {urls_finales}")
        
        print("="*60)
        
        # Mostrar ejemplo de estructura
        print("\n📋 Ejemplo de datos extraídos:")
        print("-" * 60)
        if datos_serie.get('temporadas'):
            temp = datos_serie['temporadas'][0]
            print(f"\n{temp['nombre']}:")
            if temp['episodios']:
                ep = temp['episodios'][0]
                print(f"  {ep['titulo']}")
                print(f"  Estado: {ep['estado']}")
                print(f"  Servidores disponibles: {len(ep['servidores'])}")
                if ep['servidores']:
                    for i, srv in enumerate(ep['servidores'][:3], 1):
                        print(f"    {i}. {srv['nombre']} ({srv['idioma']}) - {srv['descripcion']}")
                        if srv.get('url_video_final'):
                            print(f"       URL final: {srv['url_video_final'][:60]}...")
        print("-" * 60)