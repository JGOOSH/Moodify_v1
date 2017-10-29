import sys
import requests
import json

# initial setup, currently using hard-coded authorization
payload = {'limit' : 50, 'offset' : 0}
headers = {'Accept' : 'application/json', 'Authorization' : 'Bearer BQBOQ9_Lpese2Qbnfaw5ENn6ZL9JoxTZISuII222wnVebcWQmdCv1PBrfph-cqRu6mliUQ3d802bA-CBw3TewHZeh_UtGCfltd8BzmgOzxPM2CorsQiW1-hDjP3eeN1cnei1kLyxdxQFsIq6VX2TPYxAgWjj'}
track_request = requests.get('https://api.spotify.com/v1/me/tracks', params=payload, headers=headers)
data = track_request.json()
total = data['total']
count = 0
dict_data = []
fi = open("nameIdRelation.txt", "w")
# run the analysis until reaching the end of the list
while total > 0:
    total -= 50
    for x in data['items']:
        id = (x['track']['id'])
        name = x['track']['name']
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
       
        fi.write("id: {} | name: {}\n".format( feature['id'] ,name))
        print data
        dict_data.append(data)
    if total > 0 :
        payload['offset'] += 50
        
    track_request = requests.get('https://api.spotify.com/v1/me/tracks', params=payload, headers=headers)
    data = track_request.json()

# input
# energy, loudness, mode, speechiness, tempo, valence
