from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/generate")
def generate_number():
    number = random.randint(1, 10000)
    return jsonify({"number": number})

if __name__ == "__main__":
    app.run()
from flask import Flask, jsonify, send_from_directory
import random

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/generate")
def generate_number():
    number = random.randint(1, 10000)
    return jsonify({"number": number})
