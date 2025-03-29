''' Executing this function initiates the application of emotion detection
     to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyzes the text provided via URL query parameter for sentiment.""" # Added suggestion
    # Retrieve the text to analyze from the request arguments from JS
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract  from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response ['dominant_emotion']

    # Adding error handling for dominant emotion. No else needed in statement
    if dominant_emotion is None:
        return "Invalid input! Try again."

    # Return statement
    return (
    f"For the given statement, the system response is 'anger': {anger_score}, "
    f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and "
    f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    '''Function to render the index page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
