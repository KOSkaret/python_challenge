import make_album
# ... is the same as 'artist_name,song_title'

#from make_album import make_album
# change line 29 to albums.append(make_album(...))

#from make_album import make_album as ma
#change line 29 to albums.append(ma(...))

#import make_album as ma
#change line 29 to albums.append(ma.make_album(...))

#from make_album import*
#change line 29 to albums.append(make_album(...))

albums = []

while True:
    print("\nPlease write artist name and song title:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist name:")
    if artist_name == 'q':
        break
    song_title = input("Song title:")
    if song_title == 'q':
        break

    albums.append(make_album.make_album(artist_name, song_title))

print(albums)
