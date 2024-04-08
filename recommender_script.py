# %%
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict
from textblob import TextBlob

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
def sentiment_analysis(input_song_lyrics, recommended_songs):
    input_sentiment = TextBlob(input_song_lyrics).sentiment.polarity
    sentiment_scores = {}
    
    for song_data in recommended_songs:
        song_lyrics = song_data[1]  # Assuming lyrics are in the second position
        sentiment_score = TextBlob(song_lyrics).sentiment.polarity
        sentiment_scores[song_data[1]] = abs(sentiment_score - input_sentiment),song_data[2]
    
    # Sort the songs based on sentiment difference
    sorted_songs = sorted(sentiment_scores.items(), key=lambda x: x[1])

    # Return top rec_num sentimentally similar songs
    return sorted_songs

# %%
def get_selection(artist,song,text,rec_num):
    
    global songs
    
    # add the song for recommendations to the dataset
    x={'artist':artist,'song':song,'text':text}
    x=pd.DataFrame([x])
    songs = songs.sample(n=3000)
    songs=pd.concat([songs,x])
    
    # finding the tfidf scores for all 
    tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
    lyrics_matrix = tfidf.fit_transform(songs['text'])
    
    # finding the cosine similarities for the songs based on tf-idf scores
    cosine_similarities = cosine_similarity(lyrics_matrix) 
    similarities = {}
    
    # stores the top 50 cosime similarities in similarities dictionary 
    for i in range(len(cosine_similarities)):
        similar_indices = cosine_similarities[i].argsort()[:-50:-1] 
        similarities[songs['song'].iloc[i]] = [(cosine_similarities[i][x], songs['song'].iloc[x], songs['artist'].iloc[x]) for x in similar_indices][1:]
    
    rec_list=sentiment_analysis(text,similarities[song][1:])
    return rec_list[:rec_num]

# %%



