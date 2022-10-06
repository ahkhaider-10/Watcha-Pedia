from typing_extensions import runtime
from flask import Flask, render_template, request
import model as m
import movies

app = Flask(__name__)


@app.route('/')
def homepage():
    home_movie, home_poster, date, overview = m.suggestions()
    return render_template('index.html', home_movie=home_movie, home_poster=home_poster, date=date, overview=overview)


@app.route('/display', methods=['POST'])
def recommandpage():
    if (request.method == "POST"):
        enter_movie = request.form["moviename"]
        movie_name, movie_poster, date, overview, runtime = m.recommand(
            enter_movie.lower().replace(" ", ""))
        if movie_name == "no":
            return render_template('nomovie.html', wrongmovie=enter_movie)
        else:
            return render_template('display.html', name=movie_name, poster=movie_poster, date=date, overview=overview, runtime=runtime)


@app.route('/time80')
def time80():
    name, poster = movies.a80ss()
    return render_template('action.html', name=name, poster=poster, a="80's")


@app.route('/time90')
def time90():
    name, poster = movies.a90ss()
    return render_template('action.html', name=name, poster=poster, a="90's")


@app.route('/time20')
def time2000():
    name, poster = movies.a2000ss()
    return render_template('action.html', name=name, poster=poster, a="2000's")


@app.route('/latest')
def timelatest():
    name, poster = movies.alatests()
    return render_template('action.html', name=name, poster=poster, a="Latest")


if __name__ == '__main__':
    app.run(debug=True)
