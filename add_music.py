from csv import DictWriter
import validators
from info import GENRES, MOODS, NEUTRAL_GENRE, NEUTRAL_MOOD

while True:
    print("Enter ulr")
    url = input()
    print("Enter genres")
    genres = [NEUTRAL_GENRE]
    genre = ''
    while genre != 'mood' or (genre == 'mood' and len(genres) <= 1):
        genre = input()
        if genre in GENRES and genre not in genres:
            genres.append(genre)
    print("Enter moods")
    moods = [NEUTRAL_MOOD]
    mood = ''
    while mood != 'end' or (mood == 'end' and len(moods) <= 1):
        mood = input()
        if mood in MOODS and mood not in moods:
            moods.append(mood)

    dict = {"url": url, 'genres': ".".join(genres), 'moods': ".".join(moods)}

    with open('music.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=['url', 'genres', 'moods'])
        dictwriter_object.writerow(dict)
        f_object.close()


