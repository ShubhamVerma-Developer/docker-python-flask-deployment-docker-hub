from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask app!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)
