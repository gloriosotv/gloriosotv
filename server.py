from flask import Flask, jsonify, request, Response
import requests

app = Flask(__name__)

# URL da lista M3U8
M3U8_URL = "https://raw.githubusercontent.com/gloriosotv/Server/refs/heads/main/Lista-GloriosoTv"

def get_m3u8_content():
    try:
        response = requests.get(M3U8_URL)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Erro ao obter a lista M3U8: {e}")
        return None

@app.route('/stream/<channel_id>')
def stream(channel_id):
    m3u8_content = get_m3u8_content()
    if not m3u8_content:
        return jsonify({"error": "Erro ao obter a lista M3U8"}), 500

    for line in m3u8_content.splitlines():
        if channel_id in line:
            url = next(iter(m3u8_content.splitlines()[m3u8_content.splitlines().index(line) + 1:]), None)
            if url:
                return jsonify({"url": url})

    return jsonify({"error": "Canal não encontrado"}), 404

if __name__ == '__main__':
    app.run(port=7000)
