# Import the requests library to handle HTTP requests
import requests
# Import the json library to parse the API response
import json

# Define a function named emotion_detector that takes a string
def emotion_detector(text_to_analyse):
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create a dictionary with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyse}}
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)

    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)

    # Extract the emotion scores from the nested dictionary
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_dict['anger']
    disgust_score = emotion_dict['disgust']
    fear_score = emotion_dict['fear']
    joy_score = emotion_dict['joy']
    sadness_score = emotion_dict['sadness']

    # Find the dominant emotion (highest score)
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the required output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }