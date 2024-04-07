from recommender_script import get_selection
with open("song.txt", "r") as file:
    song_lyrics = file.read().replace("\n", "")
list_of_recs=get_selection(artist='Sabrina Carpenter',song='Thumbs',text="happy",rec_num=5)
print("\nRecommended Songs:\n")
for i in list_of_recs:
    print(i[1]," by ",i[2],'\n')


    
    
    