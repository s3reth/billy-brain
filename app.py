from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

latest_movement = {}

@app.route('/')
def home():
    return "✅ Billy AI Server is Running"

@app.route('/movement', methods=['POST'])
def receive_movement():
    global latest_movement
    latest_movement = request.json
    print("Received movement:", latest_movement)
    return jsonify({"status": "ok"})

@app.route('/latest')
def get_latest():
    return jsonify(latest_movement)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
