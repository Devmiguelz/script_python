import requests
from bs4 import BeautifulSoup
import json
import re

class PlayerAccessHelper:
    """
    Helper para acceder a players con protección de referer
    """
    
    def __init__(self):
        self.session = requests.Session()
    
    def acceder_con_referer(self, player_url, referer_url):
        """
        Accede al player con los headers correctos (referer)
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': referer_url,
            'Origin': 'https://cinecalidad.bar',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        
        try:
            response = self.session.get(player_url, headers=headers, timeout=15)
            
            print(f"Status Code: {response.status_code}")
            print(f"Content Length: {len(response.content)} bytes")
            
            if response.status_code == 200:
                return self.analizar_player(response, player_url, referer_url)
            elif response.status_code == 403:
                print("❌ Error 403: Acceso denegado (protección activa)")
                return None
            else:
                print(f"❌ Error {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error de conexión: {e}")
            return None
    
    def analizar_player(self, response, player_url, referer_url):
        """
        Analiza el contenido del player para encontrar el video real
        """
        soup = BeautifulSoup(response.content, 'html.parser')
        resultados = {
            'player_url': player_url,
            'referer': referer_url,
            'iframes': [],
            'videos_directos': [],
            'scripts_importantes': []
        }
        
        # 1. Buscar iframes anidados
        iframes = soup.find_all('iframe')
        for iframe in iframes:
            if 'src' in iframe.attrs:
                resultados['iframes'].append(iframe['src'])
        
        # 2. Buscar tags de video HTML5
        videos = soup.find_all('video')
        for video in videos:
            sources = video.find_all('source')
            for source in sources:
                if 'src' in source.attrs:
                    resultados['videos_directos'].append(source['src'])
        
        # 3. Buscar en el código JavaScript
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string:
                # Buscar URLs de video (.m3u8, .mp4, etc.)
                urls_video = re.findall(r'https?://[^\s<>"\']+?\.(?:m3u8|mp4|mkv)', script.string)
                resultados['videos_directos'].extend(urls_video)
                
                # Buscar configuraciones de player
                if 'file:' in script.string or 'source:' in script.string or 'sources:' in script.string:
                    resultados['scripts_importantes'].append(script.string[:500])
        
        # 4. Buscar en atributos data-*
        elementos_con_data = soup.find_all(attrs={'data-src': True})
        elementos_con_data += soup.find_all(attrs={'data-file': True})
        elementos_con_data += soup.find_all(attrs={'data-video': True})
        
        for elemento in elementos_con_data:
            for attr in ['data-src', 'data-file', 'data-video']:
                if attr in elemento.attrs:
                    resultados['videos_directos'].append(elemento[attr])
        
        # Eliminar duplicados
        resultados['videos_directos'] = list(set(resultados['videos_directos']))
        resultados['iframes'] = list(set(resultados['iframes']))
        
        return resultados
    
    def generar_curl_command(self, player_url, referer_url):
        """
        Genera un comando curl que funciona con el referer correcto
        """
        curl = f'''curl '{player_url}' \\
        -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \\
        -H 'Referer: {referer_url}' \\
        -H 'Origin: https://cinecalidad.bar' \\
        -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \\
        --compressed'''
        
        return curl
    
    def generar_html_embed(self, player_url, referer_url):
        """
        Genera código HTML para embedear el video con referer
        """
        html = f'''<!DOCTYPE html>
        <html>
        <head>
            <title>Player</title>
            <meta name="referrer" content="origin">
            <style>
                body {{ margin: 0; padding: 0; overflow: hidden; }}
                iframe {{ width: 100vw; height: 100vh; border: none; }}
            </style>
        </head>
        <body>
            <iframe src="{player_url}" 
                    referrerpolicy="origin"
                    allowfullscreen>
            </iframe>
            
            <script>
                // Configurar referer para peticiones
                document.referrer = '{referer_url}';
            </script>
        </body>
        </html>'''
        
        return html
    
    def mostrar_info_completa(self, resultados):
        """
        Muestra toda la información extraída de forma organizada
        """
        print("\n" + "="*80)
        print("📊 RESULTADOS DEL ANÁLISIS")
        print("="*80)
        
        print(f"\n🔗 Player URL: {resultados['player_url']}")
        print(f"📄 Referer: {resultados['referer']}")
        
        if resultados['iframes']:
            print(f"\n📺 Iframes encontrados ({len(resultados['iframes'])}):")
            for i, iframe in enumerate(resultados['iframes'], 1):
                print(f"  {i}. {iframe}")
        
        if resultados['videos_directos']:
            print(f"\n🎬 Videos directos encontrados ({len(resultados['videos_directos'])}):")
            for i, video in enumerate(resultados['videos_directos'], 1):
                print(f"  {i}. {video}")
        
        if resultados['scripts_importantes']:
            print(f"\n📝 Scripts con posibles configuraciones ({len(resultados['scripts_importantes'])}):")
            for i, script in enumerate(resultados['scripts_importantes'], 1):
                print(f"  Script {i}:")
                print(f"    {script[:200]}...")
        
        if not resultados['iframes'] and not resultados['videos_directos']:
            print("\n⚠️ No se encontraron videos directos.")
            print("   El player podría estar usando:")
            print("   - Encriptación adicional")
            print("   - Carga dinámica con JavaScript")
            print("   - Protección anti-bot avanzada")

# Ejemplo de uso
if __name__ == "__main__":
    helper = PlayerAccessHelper()
    
    print("🎬 HELPER PARA ACCEDER A PLAYERS PROTEGIDOS")
    print("="*80)
    
    # Ejemplo con la película "El último encargo"
    player_url = "https://playerkasjkajs.top/embed.php?id=5613"
    referer_url = "https://cinecalidad.bar/peli/el-ultimo-encargo/"
    
    print(f"\n📌 Ejemplo: El último encargo")
    print(f"   Player: {player_url}")
    print(f"   Referer: {referer_url}")
    
    print("\n🔍 Analizando player...")
    resultados = helper.acceder_con_referer(player_url, referer_url)
    
    if resultados:
        helper.mostrar_info_completa(resultados)
        
        # Generar comando curl
        print("\n" + "="*80)
        print("💻 COMANDO CURL (para terminal):")
        print("="*80)
        print(helper.generar_curl_command(player_url, referer_url))
        
        # Generar HTML embed
        print("\n" + "="*80)
        print("📄 HTML PARA EMBEDEAR (guarda como .html):")
        print("="*80)
        print(helper.generar_html_embed(player_url, referer_url))
        
        # Guardar HTML
        with open('player_embed.html', 'w', encoding='utf-8') as f:
            f.write(helper.generar_html_embed(player_url, referer_url))
        print("\n✓ Archivo 'player_embed.html' creado")
        
    print("\n" + "="*80)
    print("📖 CÓMO USAR:")
    print("="*80)
    print("1. Abre 'player_embed.html' en tu navegador")
    print("2. O usa el comando curl en tu terminal")
    print("3. O integra el iframe con el referer correcto en tu app")