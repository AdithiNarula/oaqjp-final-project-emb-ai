'''This is server.py file for flask'''
#Import json
import json

#Import flask
from flask import Flask, render_template, request
#Import emotion detector
from EmotionDetection.emotion_detection import emotion_detector

#Initialise flask
app = Flask("EmotionDetector")

#route the request
@app.route('/emotionDetector')
def emotion_detection():
    '''This function will call emotion detection to 
    analyse emotion and return response'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is not None:
        formatted_response = json.loads(response)
        if formatted_response['dominant_emotion'] is None:
            return "Invalid text!Please try again!"
        return f"For the given statement, the system response is 'anger': \
            {formatted_response['anger']},'disgust': {formatted_response['disgust']},\
             'fear': {formatted_response['fear']}, 'joy': {formatted_response['joy']}\
            and 'sadness': {formatted_response['sadness']}.\
            The dominant emotion is <b>{formatted_response['dominant_emotion']}.</b>"
    return "An error has incurred!"

@app.route('/')
def initial_load():
    '''This function is called to render index.html'''
    return render_template('/index.html')

if __name__ ==  "__main__":
    app.run(host='localhost', port='5000')
