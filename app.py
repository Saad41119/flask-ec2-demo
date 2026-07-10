from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        message="Hello from Flask on EC2! Now updated.",
        hostname=socket.gethostname(),
        time=datetime.utcnow().isoformat() + "Z",
    )


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/about")
def about():
    return jsonify(
        app="flask-ec2-demo",
        author="Saadi",
        purpose="Learning Git + EC2 deployment workflow",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
