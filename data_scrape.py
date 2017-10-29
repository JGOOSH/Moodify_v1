import sys
import requests
import json

# initial setup, currently using hard-coded authorization
payload = {'limit' : 50, 'offset' : 0}
headers = {'Accept' : 'application/json', 'Authorization' : 'Bearer BQD7asQomCVVLXYjy3LDA5wFbWf_atAdLDbersQG4BQsrVpSUJ1JS5A7a1z4qEDMcFjnTv-OLDdbEpKiTieeR36SjDAbXs8or1iTlmeLYw6RkrFKKVmbOXx_bJF3oGHDe18ouZztXsN-k4ffm16IMBULWNVz5DS8gw4bz3sKDPY'}
r = requests.get('https://api.spotify.com/v1/me/tracks', params=payload, headers=headers)
data = r.json();
total = data['total']
count = 0;

#run first iteration
while total > 0:
    total -= 50
    for x in data['items']:
        id = (x['track']['id'])
        url = 'https://api.spotify.com/v1/audio-features/'
        url = url + id
        feature_request = requests.get(url, headers=headers)
        print(feature_request.text)
        count += 1
    if total > 0 :
        payload['offset'] += 50

print (count)

#total = data['total']
# data = json.loads(r.text)
#print(data['items'][0]['track']['name'])
#print(data['total'])
#name =(data['items'][0]['track']['id'])

# url = 'https://api.spotify.com/v1/audio-features/'
# url = url + name
# a = requests.get(url, headers = headers)
#print(a.url);
#print(name)
#print(a.text)

#print(len(data['items']))
#print(r.text)
