# %%
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

# %%
songs = pd.read_csv('songdata (1).csv')

# %%
songs.head()

# %%
songs.isna().sum()

# %%
songs['text'] = songs['text'].replace(r'\n','')


# %%
str=''
for i in range(0,len(songs)):
    str=str+songs['artist'][i]+" "

# %%
songs=songs.drop('link', axis=1).reset_index(drop=True)

# %%
artists=str.split()

# %%
unique_artists=set(artists)

# %%
len(unique_artists)

# %%
def get_selection(artist,song,text,rec_num):
    global songs
    x={'artist':artist,'song':song,'text':text}
    x=pd.DataFrame([x])
    songs = songs.sample(n=3000)
    songs=pd.concat([songs,x])
    tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
    lyrics_matrix = tfidf.fit_transform(songs['text'])
    cosine_similarities = cosine_similarity(lyrics_matrix) 
    similarities = {}
    for i in range(len(cosine_similarities)):
        similar_indices = cosine_similarities[i].argsort()[:-50:-1] 
        similarities[songs['song'].iloc[i]] = [(cosine_similarities[i][x], songs['song'].iloc[x], songs['artist'].iloc[x]) for x in similar_indices][1:]
    rec_data = {
    "song": songs['song'].iloc[3000],
    "number_songs": rec_num }
    rec_list=similarities[song][1:rec_num+1]
    
    
    return rec_list

# %%
with open("song.txt", "r") as file:
    song_lyrics = file.read().replace("\n", "")


# %%
list_of_recs=get_selection(artist='Sabrina Carpenter',song='Thumbs',text=song_lyrics,rec_num=5)

# %%
# print("\nRecommended Songs:\n")
# for i in list_of_recs:
#     print(i[1]," by ",i[2])

# %%



