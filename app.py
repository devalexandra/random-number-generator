from flask import Flask, jsonify, send_from_directory
import random
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def serve_index():
    index_path = os.path.join(app.static_folder, "index.html")
    print(f"Looking for index.html at: {index_path}")
    return send_from_directory(app.static_folder, "index.html")

@app.route("/generate")
def generate_random_number():
    number = random.randint(1, 10000)
    return jsonify({"number": number})

@app.route("/favicon.ico")
def favicon():
    return "", 204

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


