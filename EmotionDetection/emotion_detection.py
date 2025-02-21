import requests
import json

def emotion_detector(text_to_analyze):
    """
    This function sends the user's text to the Watson emotion detection service
    and returns the detected emotions. If the input is blank or invalid, it returns
    a dictionary with None values, so we can still handle it gracefully.
    """
    
    # Check if the input is blank before sending it to the server. If blank, return None values
    if not text_to_analyze.strip():  # Strip removes leading/trailing spaces, so even '   ' counts
        print("Oops! No text provided! Please enter something for me to analyze.")
        return {'emotionPredictions': [{
            'emotion': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            }
        }]}

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Sending the request to the API
    response = requests.post(URL, json=input_json, headers=header)
    
    # If the response is successful (status code 200), process it
    if response.status_code == 200:
        detected_text = json.loads(response.text)
    elif response.status_code == 400:
        # If the request was bad (blank input or something else), we return a default 'None' dictionary
        print("Bad request! You might have sent empty text, or something went wrong!")
        detected_text = {'emotionPredictions': [{
            'emotion': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            }
        }]}
    else:
        # In case of any other error, we'll return the same 'None' dictionary just to be safe
        print(f"Error! Something went wrong. Server returned status code: {response.status_code}")
        detected_text = {'emotionPredictions': [{
            'emotion': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            }
        }]}

    return detected_text

def emotion_predictor(detected_text):
    """
    This function processes the detected text and predicts the dominant emotion.
    It returns the emotion with the highest score or None if no valid emotions are detected.
    """
    
    # Checking if the emotion predictions are present and valid
    if (detected_text.get('emotionPredictions') is None or
        detected_text['emotionPredictions'][0].get('emotion') is None):
        return None
    
    # Extracting the emotions and finding the dominant one
    emotions = detected_text['emotionPredictions'][0]['emotion']
    
    # Find the emotion with the highest score (this is the 'dominant' emotion)
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_emotion_score = emotions[dominant_emotion]
    
    # Returning the dominant emotion and its score
    return {dominant_emotion: dominant_emotion_score}

# Test the application with a sample text
if __name__ == "__main__":
    test_text = "I am so happy I am doing this."
    detected = emotion_detector(test_text)
    result = emotion_predictor(detected)
    print(result)
