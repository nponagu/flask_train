from random import sample

from flask import Flask, render_template

from data import tours, departures


app = Flask(__name__)


@app.route('/')  
def render_main():

    random_tours = dict(sample(list(tours.items()), 6))

    return render_template('index.html',
                           tours=random_tours,
                           departures=departures)


@app.route('/departures/<string:departure>/')
def render_departures(departure):

    selected_tours = dict()
    for key, value in tours.items():
        if value["departure"] == departure:
            selected_tours[key] = value

    return render_template('departure.html',
                           tours=selected_tours,
                           departures=departures)


@app.route('/tours/<int:id>/')
def render_tour(id):

    tour = tours[id]

    return render_template('tour.html',
                           tour=tour,
                           departures=departures)


app.run('0.0.0.0',8000, debug=True)
