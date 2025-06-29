from flask import Flask, jsonify, send_from_directory
import random
import os

# Create the Flask app and tell it where static files are
app = Flask(__name__, static_folder="static")

# Route: Serve index.html on "/"
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

# Route: Random number generator
@app.route("/generate")
def generate_random_number():
    number = random.randint(1, 10000)
    return jsonify({"number": number})

# Optional: Handle favicon requests gracefully
@app.route("/favicon.ico")
def favicon():
    return "", 204

# Entry point: Render requires 0.0.0.0 and dynamic port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port)
import os

@app.route("/")
def serve_index():
    index_path = os.path.join(app.static_folder, "index.html")
    print(f"Looking for index.html at: {index_path}")
    return send_from_directory(app.static_folder, "index.html")

