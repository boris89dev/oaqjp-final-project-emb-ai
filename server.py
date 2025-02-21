"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-provided text.

Author(Learner): [Boris A. Carollo]
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection")

def run_emotion_detection():
    """
    Main function to run the Emotion Detection application.
    Starting the Flask server, making it ready to detect all the feelings!
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    In other words: turn your feelings into data!
    """
    text_to_detect = request.args.get('textToAnalyze')
    
    if not text_to_detect:
        return "No text provided! Please tell me how you feel."
    
    # Get the response from the emotion detection system
    response = emotion_detector(text_to_detect)
    
    # Predict the dominant emotion based on the response
    formated_response = emotion_predictor(response)
    
    # If the response is invalid (dominant emotion is None), tell the user!
    if not formated_response or list(formated_response.values())[0] is None:
        return "Invalid text! Please try again!"  # Clear as day! 😅

    # If there's a dominant emotion, display it!
    dominant_emotion = list(formated_response.keys())[0]  # We only get one key here
    dominant_score = formated_response[dominant_emotion]
    
    return (
        f"For the given statement, the emotion scores are: "
        f"anger: {formated_response.get('anger', 'N/A')}, "
        f"disgust: {formated_response.get('disgust', 'N/A')}, "
        f"fear: {formated_response.get('fear', 'N/A')}, "
        f"joy: {formated_response.get('joy', 'N/A')}, "
        f"sadness: {formated_response.get('sadness', 'N/A')}. "
        f"The dominant emotion is {dominant_emotion} with a score of {dominant_score:.2f}."
    )

@app.route("/")
def render_index_page():
    """ 
    This function initiates the rendering of the main application 
    page over the Flask channel. 
    The moment when the web page comes to life!
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()
