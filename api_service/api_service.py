from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 🔥 BU SATIR ÇÖZÜYOR

messages = []

@app.route("/")
def home():
    return jsonify({"status": "API çalışıyor"})

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

@app.route("/messages", methods=["POST"])
def add_message():
    data = request.json
    messages.append(data)
    return jsonify({"status": "eklendi"})
