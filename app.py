from flask import Flask, jsonify, send_from_directory
import random
import os

app = Flask(__name__, static_folder="static")

# Serve the index.html when visiting "/"
@app.route("/")
def index():
    return send_from_directory("static", "index.html")

# API route to generate a number
@app.route("/generate")
def generate():
    return jsonify({"number": random.randint(1, 10000)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, jsonify, send_from_directory
import random
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/generate")
def generate_number():
    number = random.randint(1, 10000)
    return jsonify({"number": number})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Render's PORT, fallback to 5000 for local
    app.run(host="0.0.0.0", port=port)
