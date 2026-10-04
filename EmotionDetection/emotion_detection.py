''' This module calls Emotion predict function of Watson 
NLP and returns emotions with their score. It also returns dominant emotion name'''

#import requests and json
import json
import requests

def emotion_detector(text_to_analyze):
    '''This function calls Emotion predict function of Watson 
       NLP and returns emotions with their score. It also returns dominant emotion name'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/'\
           'NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }    
    response = requests.post(url,headers=headers,json=input_json,timeout=120)   
    if response.status_code == 200:
        formatted_response = json.loads(response.text)["emotionPredictions"][0]["emotion"]
        anger = formatted_response["anger"]
        disgust = formatted_response["disgust"]
        fear = formatted_response["fear"]
        joy = formatted_response["joy"]
        sadness = formatted_response["sadness"]
        dominant_emotion = max(formatted_response, key= formatted_response.get)
        final_out = {'anger': anger,\
                  'disgust': disgust,\
                  'fear': fear, 'joy': joy, 'sadness':sadness,\
                'dominant_emotion': dominant_emotion}
        return json.dumps(final_out, indent=4)
    elif response.status_code == 400:
         final_out = {'anger': None,\
                  'disgust': None,\
                  'fear': None, 'joy': None, 'sadness':None,\
                'dominant_emotion': None}
         return json.dumps(final_out, indent=4)
    else:
        return None     


