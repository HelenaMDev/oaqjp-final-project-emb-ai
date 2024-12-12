import requests, json 

def emotion_detector(text_to_analyze):
    '''
    Sends text_to_analyze to Watson AI's API and returnst the result as text
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Send the request
    response = requests.post(url, json = myobj, headers=headers, timeout=60)

    # Return its text property
    return response.text
