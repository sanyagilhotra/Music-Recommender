from recom_script import get_selection
with open("song.txt", "r") as file:
    song_lyrics = file.read().replace("\n", "")
list_of_recs=get_selection(artist='Sabrina Carpenter',song='Thumbs',text=song_lyrics,rec_num=5)
print("\nRecommended Songs:\n")
for i in list_of_recs:
    print(i['Song']," by ",i['Artist'],'\n')


    
    
    