from flask import Flask, request, render_template 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def detector():
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze == "":
        return "Please enter a text to analyze"

    # Get the analysis
    emotions = emotion_detector(text_to_analyze)

    # Extract the dominant emotion
    dominant_emotion = emotions["dominant_emotion"]
    del emotions["dominant_emotion"]

    result = ""
    for emotion, score in emotions.items():
        if result != "":
            result += ","
        result += f" '{emotion}': {score}"
    result = f"For the given statement, the system response is {result}. The dominant emotion is <b>{dominant_emotion}</b>"
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)