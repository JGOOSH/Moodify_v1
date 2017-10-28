import sys
import requests
import json

payload = {'limit' : 1}
headers = {'Accept' : 'application/json', 'Authorization' : 'Bearer BQDKABD1wSwzeuC3krGxIU4SckLx0l2uFi_WLoBCnys1t0uNfG3wMEH2Hh-FTA_kf91hyKNYnBJxHIcTQT9mGwvcVENMssGw1E65c1zjrqmkfUPi6Nh0zzA68ZvgPri-CMQCl5n3khIcQMiYq_iRIQUxC5FLeZ46vFDYXBamIsI'}
r = requests.get('https://api.spotify.com/v1/me/tracks', params=payload, headers=headers)

# data = json.loads(r.text)
data = r.json();
print(data['items']['name'])
# print(r.text);
