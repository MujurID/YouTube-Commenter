import os, sys
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google_auth_oauthlib.flow
from google_auth_oauthlib.flow import InstalledAppFlow
import requests
import re
import time
import random

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

def add_comment(client, video_id, cmnt):
    resource = {'snippet': {
                    'channelId': 'UCBR8-60-B28hp2BmDPdntcQ', # Fill in with any random channel id
                    'videoId': video_id,
                    'topLevelComment': {
                        'snippet': {
                            'textOriginal': cmnt
                        }
                    }
                }}

    # https://developers.google.com/youtube/v3/docs/commentThreads/insert
    response = client.commentThreads().insert( 
        body=resource,
        **{'part': 'snippet'}
    ).execute()

    # https://developers.google.com/youtube/v3/docs/commentThreads#resource
    print(response)

# Extremely inefficient, defintely some better way to do this
def scrape_ids(kw):
    base_url = f'https://www.youtube.com/results?search_query={kw}'
    r = requests.get(url=base_url)
    lines = [line.strip() for line in r.text.split('\n')]
    line = ''

    for x in lines:
        if x.startswith('window["ytInitialData"]'):
            line = x
            break
    if line == '':
        print('Error scraping links. Exiting.')
        sys.exit(0)

    video_ids = re.findall(r'\/watch\?v=[.a-zA-Z0-9_-]*', line)
    return video_ids

def get_data(file):
    with open(file) as f:
        data = [line.strip() for line in f]
    return data

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', ['https://www.googleapis.com/auth/youtube.force-ssl'])
    credentials = flow.run_console()
    return build('youtube', 'v3', credentials=credentials)

def main():
    delay = int(input('Input delay: '))
    client = authenticate()

    kws = get_data('data/keywords.txt')
    cmnts = get_data('data/comments.txt')
    prefixes = get_data('data/prefixes.txt')

    try:
        while True:
            video_ids = []

            for kw in kws:
                video_ids = video_ids + scrape_ids(kw)
            video_ids = [video_id.replace('/watch?v=', '')
                         for video_id in video_ids]

            for video_id in video_ids:
                for cmnt in cmnts:
                    new_cmnt = f'{random.choice(prefixes)}\n\n{cmnt}'
                    add_comment(client, video_id, new_cmnt)
                    time.sleep(delay)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()