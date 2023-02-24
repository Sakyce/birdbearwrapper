import json, csv

class ImagesToDownload(list):
    def __init__(self):
        super().__init__()
        self.output_csv = [['index', 'date', 'user', 'content', 'url']]

    def add(self, tweet_details):
        self.output_csv.append(
            [
                str(len(self)),
                tweet_details['date'],
                tweet_details['user']['username'],
                tweet_details['content'],
                tweet_details['url']
            ]
        )
        self.extend(tweet_details['media'])
    
    def output(self, file):
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(self.output_csv)

js = None

with open('input.json', 'r', encoding='utf-8') as file:
    js = json.load(file)

def get_medias():
    'Retourne une liste des médias Twitter'

    images_to_download = ImagesToDownload()

    for tweet in js:
        tweet_details:dict = json.loads(tweet['tweet_json'])

        if tweet_details['media']:
            print(tweet_details)
            images_to_download.add(tweet_details)
    
    return images_to_download

if __name__ == '__main__':
    print(get_medias().output_csv)