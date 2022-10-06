import pickle
import pandas as pd
import requests
from numpy import random

a90s = pickle.load(open("movies90s.pkl", "rb"))
a80s = pickle.load(open("movies80s.pkl", "rb"))
a2000s = pickle.load(open("movies2000s.pkl", "rb"))
alatest = pickle.load(open("latest.pkl", "rb"))

a90s = pd.DataFrame(a90s)
a90s = a90s.reset_index()
a80s = pd.DataFrame(a80s)
a80s = a80s.reset_index()
a2000s = pd.DataFrame(a2000s)
a2000s = a2000s.reset_index()
alatest = pd.DataFrame(alatest)
alatest = alatest.reset_index()


def poster_get_movie(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=055cbae9f25a461165851543835e6272&language=en-US".format(movie_id))
    data = response.json()
    a = str(data['poster_path'])

    poster = "https://image.tmdb.org/t/p/w500/" + a
    return poster


def a80ss():
    idxlist = []
    suggest = []
    suggest_poster = []
    for num in range(0, 20):
        idxlist.append(random.randint(1270))
    # return idxlist
    for j in idxlist:
        index_id = a80s.loc[j, 'tmdbId']
        suggest.append(a80s.loc[j, 'title'])
        a = poster_get_movie(index_id)
        suggest_poster.append(a)
    return suggest, suggest_poster


def a90ss():
    idxlist = []
    suggest = []
    suggest_poster = []
    for num in range(0, 20):
        idxlist.append(random.randint(2610))
    # return idxlist
    for j in idxlist:
        index_id = a90s.loc[j, 'tmdbId']
        suggest.append(a90s.loc[j, 'title'])
        a = poster_get_movie(index_id)
        suggest_poster.append(a)
    return suggest, suggest_poster


def a2000ss():
    idxlist = []
    suggest = []
    suggest_poster = []
    for num in range(0, 20):
        idxlist.append(random.randint(1071))
    # return idxlist
    for j in idxlist:
        index_id = a2000s.loc[j, 'tmdbId']
        suggest.append(a2000s.loc[j, 'title'])
        a = poster_get_movie(index_id)
        suggest_poster.append(a)
    return suggest, suggest_poster


def alatests():
    idxlist = []
    suggest = []
    suggest_poster = []
    for num in range(0, 20):
        idxlist.append(random.randint(3126))
    # return idxlist
    for j in idxlist:
        index_id = alatest.loc[j, 'tmdbId']
        suggest.append(alatest.loc[j, 'title'])
        a = poster_get_movie(index_id)
        suggest_poster.append(a)
    return suggest, suggest_poster
