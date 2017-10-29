import sys
import requests
import json
#from pymongo import MongoClient

def readTracks():
    # client = MongoClient("mongodb://hacktx2017:hacktx2017alllowercase@ds047762.mlab.com:47762")
    # db = client["emotion_music"]

    fi = open("songs.txt", "a")
    # fi2 = open("nameIdRelation.txt", "a")

    # initial setup, currently using hard-coded authorization
    payload = {"limit" : 50, "offset" : 0}
    headers = {"Accept" : "application/json", "Authorization" : "Bearer BQDzXQpM_-E0BdfJc7mk3-DB6ssteVA0OU9_PjCUeXrhKsLwPq49fUPUHGoAXCgk_vAmpkpMkDUDgwPQHkiysCC9RjITr79S0ltuTyCilHsowBzTenqxExLmOTITvj0Jfh_XEo3pJ3-c3qz1lkvYm2yeiGy8epdcc5Q"}
    track_request = requests.get("https://api.spotify.com/v1/me/tracks", params=payload, headers=headers)
    data = track_request.json()
    total = data["total"]
    count = 0
    dict_data = []

    # run the analysis until reaching the end of the list
    while total > 0:
        total -= 50
        for x in data["items"]:
            id = (x["track"]["id"])

            #query = db.find({"id": id})
            if not query:
                name = x["track"]["name"]
                url = "https://api.spotify.com/v1/audio-features/"
                url = url + id
                feature_request = requests.get(url, headers=headers)
                feature = feature_request.json()
                data = {
                    "id" : feature["id"],
                    "energy" : feature["energy"],
                    "loudness" : feature["loudness"],
                    "mode" : feature["mode"],
                    "speechiness" : feature["speechiness"],
                    "tempo" : feature["tempo"],
                    "valence" : feature["valence"]
                }

                fi.write(data)
                # fi2.write("id: {} | name: {}\n".format( feature["id"] ,name))
                # print data
                # dict_data.append(data)
        if total > 0 :
            payload["offset"] += 50

        track_request = requests.get("https://api.spotify.com/v1/me/tracks", params=payload, headers=headers)
        data = track_request.json()

def readPlayList():
    f2 = open("playlist_songs.txt", "a")
    fi2 = open("nameIdRelation.txt", "a")
    url = "https://api.spotify.com/v1/users/" + "lockijazz" +"/playlists/"  + "0KxCwQWV2dag4n81XQNu2K" + "/tracks"
    headers = {"Accept" : "application/json", "Authorization" : "Bearer BQDzXQpM_-E0BdfJc7mk3-DB6ssteVA0OU9_PjCUeXrhKsLwPq49fUPUHGoAXCgk_vAmpkpMkDUDgwPQHkiysCC9RjITr79S0ltuTyCilHsowBzTenqxExLmOTITvj0Jfh_XEo3pJ3-c3qz1lkvYm2yeiGy8epdcc5Q"}
    payload = {"limit" : 50}
    playlist_request = requests.get(url, headers = headers, params=payload)
    data = playlist_request.json()
    f2.write("[")
    for x in data["items"]:
        url = "https://api.spotify.com/v1/audio-features/"
        url = url + x["track"]["id"]
        feature_request = requests.get(url, headers=headers)
        feature = feature_request.json()
        song = {
            "id" : feature["id"],
            "energy" : feature["energy"],
            "loudness" : feature["loudness"],
            "mode" : feature["mode"],
            "speechiness" : feature["speechiness"],
            "tempo" : feature["tempo"],
            "valence" : feature["valence"],
            "name" : x["track"]["name"]
        }
        f2.write(str(song) + ",")
        fi2.write("id: {} | name: {}\n".format( feature["id"] , x["track"]["name"]))
    f2.write("]")


readPlayList()


    # input
    # energy, loudness, mode, speechiness, tempo, valence
