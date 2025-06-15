from flask import Flask, render_template, request, jsonify
from emotion_app.emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotion", methods=["POST"])
def detect_emotion():
    text = request.form["text"]
    result = emotion_predictor(text)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
