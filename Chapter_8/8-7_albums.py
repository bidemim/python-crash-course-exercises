def make_album(artist_name, album_title, number_of_songs=None):
    if number_of_songs:
        album_details = {
            'artist_name': artist_name, 
            'album_title': album_title, 
            'number_of_songs': number_of_songs,
            }
    else:
        album_details = {
            'artist_name': artist_name, 
            'album_title': album_title, 
            }
    return album_details

album = make_album('bob marley', 'the wailing wailers')
print(album)
album = make_album('fela kuti', 'zombie')
print(album)
album = make_album('lauryn hill', 'The Miseducation of Lauryn Hill', 16)
print(album)