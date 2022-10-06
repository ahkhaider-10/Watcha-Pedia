import requests
import pandas as pd
import pickle
from numpy import random
import numpy as np


selected = pickle.load(open('movies2.pkl', 'rb'))
movies = pd.DataFrame(selected)
movies = movies.reset_index()


# similar = pickle.load(open('similar.pkl', 'rb'))
# similar2 = pickle.load(open("similar2.pkl", "rb"))
similar_movies = pickle.load(open("distance_movie.pkl", "rb"))


def poster_get(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=055cbae9f25a461165851543835e6272&language=en-US".format(movie_id))
    data = response.json()
    a = str(data['poster_path'])

    poster = "https://image.tmdb.org/t/p/w500/" + a
    return poster, data['release_date'], data['overview'], data['runtime']


def suggestions():
    idxlist = []
    suggest = []
    suggest_poster = []
    released_date = []
    overview = []
    for num in range(0, 14):
        idxlist.append(random.randint(10000))
    # return idxlist
    for j in idxlist:
        index_id = movies.loc[j, 'tmdbId']
        suggest.append(movies.loc[j, 'title'])
        a, b, c, d = poster_get(index_id)
        suggest_poster.append(a)
        released_date.append(b)
        overview.append(c)
    return suggest, suggest_poster, released_date, overview


def recommand(movie):
    if movie not in movies['oldtitle'].values:
        return ("no", "such", "movie", "here", " ")
    else:
        movie_index = movies[movies['oldtitle'] == movie].index[0]
        distances = enumerate(list(similar_movies[movie_index]))
        j = sorted(distances, reverse=True, key=lambda x: x[1])
        movie_rec = j[0:5]
        movie_name = []
        movie_poster = []
        date = []
        overview = []
        runtime = []
        for i in movie_rec:
            index, distance = i
            movie_name.append(movies.loc[index, 'title'])
            movieid = movies.loc[index, 'tmdbId']
            a, b, c, d = poster_get(movieid)
            movie_poster.append(a)
            date.append(b)
            overview.append(c)
            runtime.append(d)
    return movie_name, movie_poster, date, overview, runtime

# def genre_specify():