"""
Emotion Detection Flask app
Uses Watson's AI API to analyze the emotion of a text 
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render index page
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def detector():
    """ 
    Analyze the emotion of a text passed by GET request
    """
    text_to_analyze = request.args.get("textToAnalyze")

    # Get the analysis
    emotions = emotion_detector(text_to_analyze)

    # Extract the dominant emotion
    dominant_emotion = emotions["dominant_emotion"]
    if dominant_emotion is None:
        return "<b>Invalid text! Please try again!</b>"

    # Create the result phrase
    del emotions["dominant_emotion"]
    result = ""
    for emotion, score in emotions.items():
        if result != "":
            result += ","
        result += f" '{emotion}': {score}"
    result = f"For the given statement, the system response is {result}."
    result += f"The dominant emotion is <b>{dominant_emotion}</b>"
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
