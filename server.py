"""Flask app for detecting emotions in user-submitted text."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
@app.route("/")
def index():
    """Renders the homepage with the input form."""
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """Handles emotion detection requests via query parameter."""
    text_to_analyze = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyze)
    if emotion_result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, "
        f"'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, "
        f"'joy': {emotion_result['joy']} and "
        f"'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is {emotion_result['dominant_emotion']}."
    )
if __name__ == "__main__":
    app.run(debug=True)
