"""Module for detecting emotions in text using an external API."""
import requests
import json


def emotion_detector(text_to_analyse): 
    """Sends a POST request to the Watson Emotion API to analyze emotions in the given text."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    try:
        response = requests.post(url, json=myobj, headers=header, timeout=10)
        formatted_response = response.json()
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        emotion_scores = {
            "anger" : emotions["anger"],
            "disgust" : emotions["disgust"],
            "fear" : emotions["fear"],
            "joy" : emotions["joy"],
            "sadness" : emotions["sadness"]
        }
        emotion_scores["dominant_emotion"]=max(emotion_scores, key=emotion_scores.get)
        if response.status_code == 400:
            return {"anger": None, "disgust": None,"fear": None,"joy": None,"sadness": None, 
            "dominant_emotion": None }
        return emotion_scores
        #return response.text
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
