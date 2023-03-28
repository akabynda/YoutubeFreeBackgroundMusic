import csv
from flask import Flask, render_template, request, jsonify
from info import GENRES, MOODS, NEUTRAL_GENRE, NEUTRAL_MOOD

app = Flask(__name__)


class Track:
    def __init__(self, url, genres, moods):
        self.url = url
        self.genres = genres
        self.moods = moods


def find_tracks(genre, mood):
    list = []
    with open('music.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            genres = row['genres'].split('.')
            moods = row['moods'].split('.')
            if genre in genres and mood in moods:
                genres.remove(NEUTRAL_GENRE)
                moods.remove(NEUTRAL_MOOD)
                genres_str = ", ".join(genres)
                moods_str = ", ".join(moods)
                list.append(Track(row["url"], genres_str, moods_str))
    return list


@app.route("/")
def index():
    return render_template('index.html', len_genres=len(GENRES),
                           genres=GENRES,
                           len_moods=len(MOODS), moods=MOODS)


@app.route("/filter", methods=["POST", "GET"])
def filter():
    genre = NEUTRAL_GENRE
    mood = NEUTRAL_MOOD
    if request.method == 'POST':
        genre_query = request.form['a']
        if genre_query != '':
            genre_search = request.form['a']
            genre = GENRES[int(genre_search)]
        mood_query = request.form['b']
        if mood_query != '':
            mood_search = request.form['b']
            mood = MOODS[int(mood_search)]
    track_list = find_tracks(genre, mood)
    return jsonify({'htmlresponse': render_template('response.html', track_list=track_list)})


if __name__ == '__main__':
    app.run(debug=False)
