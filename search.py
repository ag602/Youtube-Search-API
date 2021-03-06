#!/usr/bin/python3

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..
# export DJANGO_SETTINGS_MODULE=fampay.settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay.settings')
import django

django.setup()

import argparse

from datetime import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

try:
    from models import Vidata
except ImportError:
    from youtubeapi.models import Vidata
from django.db import models

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyCcXAIIWlBsZ1EGffu4vYK_1l4nbkKMuvU'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q='cricket',
        part='id,snippet',
        order="date",
        maxResults=options.max_results,

        # order=options.date,
    ).execute()
    # print(search_response)
    videos = []
    # channels = []
    # playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            found = Vidata.objects.filter(videoid=search_result['id']['videoId'])
            # print(stat)
            if found.exists():
                continue
            else:
                request_stats = youtube.videos().list(
                    part="snippet, statistics",
                    id=search_result['id']['videoId'],
                ).execute()
                stat = {}
                for item in request_stats['items']:
                    for i in item['statistics']:
                        stat[i] = item['statistics'][i]
                if "likeCount" in stat:
                    data = Vidata(videoid=search_result['id']['videoId'], title=search_result['snippet']['title'],
                                          description=search_result['snippet']['description'],
                                          publishedAt=datetime.strptime(search_result['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                                          thumbnail_medium=search_result['snippet']['thumbnails']['medium']['url'],
                                          channeltitle=search_result['snippet']['channelTitle'],
                                          viewcount=stat['viewCount'], likecount=stat['likeCount'],
                                          dislikecount=stat['dislikeCount'],
                                          videourl="https://www.youtube.com/watch?v="+search_result['id']['videoId'])
                else:
                    data = Vidata(videoid=search_result['id']['videoId'],
                                          title=search_result['snippet']['title'],
                                          description=search_result['snippet']['description'],
                                          publishedAt=datetime.strptime(search_result['snippet']['publishedAt'],
                                                                        '%Y-%m-%dT%H:%M:%SZ'),
                                          thumbnail_medium=search_result['snippet']['thumbnails']['medium']['url'],
                                          channeltitle=search_result['snippet']['channelTitle'],
                                          viewcount=stat['viewCount'], likecount="NA",
                                          dislikecount="NA",
                                          videourl="https://www.youtube.com/watch?v=" + search_result['id']['videoId'])

                    data.save()
        videos.extend([search_result['id']['videoId'], search_result['snippet']['title'],
                       search_result['snippet']['description'], search_result['snippet']['publishedAt']])

        # elif search_result['id']['kind'] == 'youtube#channel':
        #   channels.append('%s (%s)' % (search_result['snippet']['title'],
        #                                search_result['id']['channelId']))
        # elif search_result['id']['kind'] == 'youtube#playlist':
        #   playlists.append('%s (%s)' % (search_result['snippet']['title'],
        #                                 search_result['id']['playlistId']))

    # print('Videos:\n', '\n'.join(videos), '\n')
    # print ('Channels:\n', '\n'.join(channels), '\n')
    # print ('Playlists:\n', '\n'.join(playlists), '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default='Google')
    parser.add_argument('--max-results', help='Max results', default=100)
    # parser.add_argument('--order', help='Order', default="date")
    args = parser.parse_args()

    try:
        youtube_search(args)
    except (HttpError, e):
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
