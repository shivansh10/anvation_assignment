import requests

def predict_text(utterance):
    try:
        appId = '222def36-5d75-4a47-b524-5f10928abb14'
        prediction_key = 'cbf5967a60034c179448c881ad8058ce'
        prediction_endpoint = 'https://westus.api.cognitive.microsoft.com/'
        headers = {

        }
        params ={
            'query': utterance,
            'timezoneOffset': '0',
            'verbose': 'true',
            'show-all-intents': 'true',
            'spellCheck': 'false',
            'staging': 'false',
            'subscription-key': prediction_key
            }
        
        response = requests.get(f'{prediction_endpoint}luis/prediction/v3.0/apps/{appId}/slots/production/predict', headers=headers, params=params)
        return response.json()
    
    except Exception as e:
        print(f'{e}')