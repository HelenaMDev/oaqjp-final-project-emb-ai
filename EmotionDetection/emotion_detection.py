import requests, json 

def emotion_detector(text_to_analyze):
    '''
    Sends text_to_analyze to Watson AI's API and formats the result
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Send the request to Watson's AI API
    response = requests.post(url, json = myobj, headers=headers, timeout=60)

    # If we get a status code 400, return a dictionary with all values set to None
    if response.status_code == 400:
        # Return a dictionary with all keys set to None
        return {
            'sadness': None,
            'joy': None,
            'fear': None,
            'disgust': None,
            'anger': None,
            'dominant_emotion': None
        }

    # Format the response as JSON dictionary
    formatted_response = json.loads(response.text)

    # Extract the emotions dictionary
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Find the dominant emotion
    dominant_emotion = ""
    max_score = 0
    for emotion, score in emotions.items():
        if score > max_score:
            dominant_emotion = emotion
            max_score = score

    # Add the dominant emotion to the dictionary
    emotions['dominant_emotion'] = dominant_emotion

    # Return the emotions dictionary
    return emotions
