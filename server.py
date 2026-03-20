# pylint: disable=missing-module-docstring

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect():
    text = request.args.get("textToAnalyze")

    if not text:
        return "Invalid input! Please try again."

    result = emotion_detector(text)

    if result is None:
        return "Invalid input! Please try again."

    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
