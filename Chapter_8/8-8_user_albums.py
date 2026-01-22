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

while True:
    print('\nPlease enter the artist name: ')
    print("(enter 'q' anytime to quit)")

    a_name = input('Artist name: ')
    if a_name == 'q':
        break
    a_title = input('Album title: ')
    if a_title == 'q':
        break
