from recommender_script import get_selection
with open("song.txt", "r") as file:
    song_lyrics = file.read().replace("\n", "")
get_selection(artist='Sabrina Carpenter',song='Thumbs',text=song_lyrics,rec_num=5)


    
    
    