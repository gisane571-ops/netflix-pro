from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API ONLINE"

@app.route("/cmd", methods=["POST"])
def cmd():

    data = request.json
    cmd = data.get("cmd")

    return jsonify({
        "msg": f"Executado {cmd}"
    })
