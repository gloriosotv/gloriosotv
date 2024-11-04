
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 7000

# URL da lista IPTV
IPTV_URL = 'https://raw.githubusercontent.com/gloriosotv/Server/refs/heads/main/Lista-GloriosoTv'

# Definindo o manifesto do addon
manifest = {
    "id": "community.glorioso.addon",
    "version": "1.0.0",
    "name": "GloriosoTV Addon",
    "description": "Addon para acessar a lista GloriosoTV.",
    "types": ["tv"],
    "resources": ["stream"],
    "idPrefixes": ["gloriosotv"],
    "catalogs": []
}

class StremioAddonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/manifest.json":
            # Retorna o manifesto do addon
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(manifest).encode("utf-8"))
        
        elif self.path.startswith("/stream/"):
            # Handler de streams - retorna o link da lista IPTV
            stream_response = {
                "streams": [{
                    "title": "GloriosoTV Stream",
                    "url": IPTV_URL
                }]
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(stream_response).encode("utf-8"))
        
        else:
            # Rota não encontrada
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), StremioAddonHandler)
    print(f"Stremio addon server rodando em http://{HOST_NAME}:{PORT_NUMBER}")
    httpd.serve_forever()
