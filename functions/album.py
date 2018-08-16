def make_album(artist, title):
    album = {'artist':artist, 'title':title}
    return album

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

    albums.append(make_album(artist_name, song_title))

print(albums)
