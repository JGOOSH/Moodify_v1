import sys
import requests
import json

# initial setup, currently using hard-coded authorization
payload = {'limit' : 50, 'offset' : 0}
headers = {'Accept' : 'application/json', 'Authorization' : 'Bearer BQD7asQomCVVLXYjy3LDA5wFbWf_atAdLDbersQG4BQsrVpSUJ1JS5A7a1z4qEDMcFjnTv-OLDdbEpKiTieeR36SjDAbXs8or1iTlmeLYw6RkrFKKVmbOXx_bJF3oGHDe18ouZztXsN-k4ffm16IMBULWNVz5DS8gw4bz3sKDPY'}
track_request = requests.get('https://api.spotify.com/v1/me/tracks', params=payload, headers=headers)
data = track_request.json()
total = data['total']
count = 0
dict_data = []

# run the analysis until reaching the end of the list
while total > 0:
    total -= 50
    for x in data['items']:
        id = (x['track']['id'])
        url = 'https://api.spotify.com/v1/audio-features/'
        url = url + id
        feature_request = requests.get(url, headers=headers)
        feature = feature_request.json()
        data = {
            'id' : feature['id'],
            'energy' : feature['energy'],
            'loudness' : feature['loudness'],
            'mode' : feature['mode'],
            'speechiness' : feature['speechiness'],
            'tempo' : feature['tempo'],
            'valence' : feature['valence']
        }
        dict_data.append(data);
    if total > 0 :
        payload['offset'] += 50

# input
# energy, loudness, mode, speechiness, tempo, valence
