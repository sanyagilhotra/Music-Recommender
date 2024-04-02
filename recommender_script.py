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
artists=str.split()

# %%
unique_artists=set(artists)

# %%
len(unique_artists)

# %%
class ContentBasedRecommender:
    def __init__(self, matrix):
        self.matrix_similar = matrix

    def _print_message(self, song, recom_song):
        rec_num = len(recom_song)
        print(f'The {rec_num} recommended songs for {song} are:')
        for i in range(rec_num):
            print(f"\nNumber {i+1}:")
            print(f"{recom_song[i][1]} by {recom_song[i][2]}") 
        
        
    def recommend(self, recommendation):
        song = recommendation['song']
        number_songs = recommendation['number_songs']
        recom_song = self.matrix_similar[song][:number_songs]
        self._print_message(song=song, recom_song=recom_song)

# %%
# class CollaborativeFilteringRecommender:

# %%
def get_selection(artist,song,text,rec_num):
    global songs
    x={'artist':artist,'song':song,'text':text}
    x=pd.DataFrame([x])
    songs = songs.sample(n=3000).drop('link', axis=1).reset_index(drop=True)
    songs=pd.concat([songs,x])
    tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
    lyrics_matrix = tfidf.fit_transform(songs['text'])
    cosine_similarities = cosine_similarity(lyrics_matrix) 
    similarities = {}
    for i in range(len(cosine_similarities)):
        similar_indices = cosine_similarities[i].argsort()[:-50:-1] 
        similarities[songs['song'].iloc[i]] = [(cosine_similarities[i][x], songs['song'].iloc[x], songs['artist'].iloc[x]) for x in similar_indices][1:]
    recommedations = ContentBasedRecommender(similarities)
    recommendation = {
    "song": songs['song'].iloc[3000],
    "number_songs": rec_num }
    rec_songs=recommedations.recommend(recommendation)
    

# %%



