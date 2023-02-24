import json

class ImagesToDownload(list):
    pass

js = None

with open('input.json', 'r', encoding='utf-8') as file:
    js = json.load(file)

def get_medias():
    'Retourne une liste des médias Twitter'

    images_to_download = ImagesToDownload()

    for tweet in js:
        tweet_details:dict = json.loads(tweet['tweet_json'])

        if tweet_details['media']:
            images_to_download.extend(tweet_details['media'])
    
    return images_to_download