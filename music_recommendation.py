import numpy as np
import csv
import os.path
import json
import pandas as pd

def normalize(column):
    max_value = column.max()
    min_value = column.min()
    result = (column - min_value) / (max_value - min_value)
    
    return result

def readData(data_file):
    raw_data = open(data_file,'rt')
    data = pd.read_csv(raw_data)
    data = data.replace(np.nan,"")
    
    return data
SONGS = readData("data_o.csv")
SONGS = SONGS.drop_duplicates(subset=['artists','name'],keep='first')
SONGS['name']=SONGS['name'].str.upper()
SONGS['artists']=SONGS['artists'].str.upper()
TARGET_SONG_ATTRIBUTES = ["acousticness","danceability","instrumentalness","liveness","speechiness","tempo","valence"]
song_data = SONGS[TARGET_SONG_ATTRIBUTES]
song_name = SONGS[['name','artists']]
# for attr in TARGET_SONG_ATTRIBUTES:
#     song_data[attr] = normalize(SONGS[attr])
    
ENCODER = dict()


for i,song in enumerate(song_name.values):
    if not (song[0]) in ENCODER:
        ENCODER[song[0]] = i
       
def recommendSongs(song):
    global song_name,song_data
    
    RECOMMENDED_SONGS =[]
    distances = []
    
    for pos,targ_song in enumerate(song_data.values):
        distances.append((np.linalg.norm(song - targ_song),pos))
    
    distances.sort(key=lambda x:x[0])
    AMTOFRECOMMENDEDSONGS = 5
    for x in range(AMTOFRECOMMENDEDSONGS):
        RECOMMENDED_SONGS.append(ENCODER[song_name.values[distances[x+1][1]][0]])
        # RECOMMENDED_SONGS.append(SONGS.values[distances[x+1][1]])

    return RECOMMENDED_SONGS 
# name='JE M'DONNE"
# artist="['MAURICE CHEVALIER']"
name=input()
# artist=input()
num=ENCODER [(name)]
test = song_data.values[num]
recommend = recommendSongs(test)
print(recommend
      )
# recommend_sort=sorted(recommend,key=lambda x: x[1])
for song in recommend:
    # print(song)
    print(SONGS.loc[song, "name"])