from os import mkdir
from requests import get
from reader import get_medias
from urllib.parse import parse_qs, urlparse

def download_url():
    try: mkdir('medias')
    except FileExistsError: pass
    
    medias = get_medias()
    for i, media in enumerate(medias):
        media:dict
        format:str = ''

        url:str = media.get('fullUrl')
        if not url:
            bitrates_urls:dict[int, str] = {} # Get the video in HD!!!

            for variant in media.get('variants'):
                if variant['contentType'] == 'video/mp4':
                    bitrates_urls['bitrate'] = variant['url']

            url = bitrates_urls[max(bitrates_urls.keys())] 
            format = 'mp4'

        r = get(url, allow_redirects=True)
        r.raise_for_status()
        
        if not format:
            format = parse_qs(urlparse(url).query)['format'][0]

        with open(f'medias/{i}.{format}', 'wb') as file: 
            file.write(r.content)

download_url()