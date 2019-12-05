def make_album(artist, album, tracks=''):
    if tracks:
        new_album = {'artist': artist, 'album': album, 'tracks': tracks}
    else:
        new_album = {'artist': artist, 'album': album}
    return new_album

#al1 = make_album('imagine dragons', 'album1')
#al2 = make_album('pyatnica', 'kukushka', 5)
#al3 = make_album(' dragons', 'tyty')
#print(al1)
#print(al2)
#print(al3)

while True:
    print("""Plese tell me information about new album.
    (enter 'q' at any time to quit)""")
    artist = input("Artist name: ")
    if artist == 'q':
        break
    album = input("Album name: ")
    if album == 'q':
        break
    new_album = make_album(artist, album)
    print(new_album)

