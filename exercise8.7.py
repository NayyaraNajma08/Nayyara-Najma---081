def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

print(make_album("Taylor Swift", "folklore"))
print(make_album("Adele", "25"))
print(make_album("Yedam", "Only One"))
print(make_album("Seventeen", "Face the Sun", songs=9))