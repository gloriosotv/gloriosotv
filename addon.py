from flask import Flask, jsonify

app = Flask(__name__)

# URL do servidor proxy
SERVER_URL = "http://localhost:7000"

@app.route('/stream/<channel_id>')
def stream(channel_id):
    return jsonify({
        "streams": [
            {
                "title": "GloriosoTV Stream",
                "url": f"{SERVER_URL}/stream/{channel_id}"
            }
        ]
    })

if __name__ == '__main__':
    app.run(port=9000)
