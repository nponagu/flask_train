from flask import Flask
from flask import render_template
from data import tours, departures


app = Flask(__name__)


@app.route('/')  
def render_main():
    return render_template('index.html', tours=tours, departures=departures)


@app.route('/departures/<departure>/')  
def render_departures(departure):

    # afordable_hotels = [tour for tour in tours if ]
    #
    # for _ in range(3):
    #     max_price = 0
    #     for hotel in afordable_hotels:
    #         if hotel["price"] > max_price:
    #             max_price = hotel["price"]
    #
    #     for hotel in afordable_hotels:
    #         if hotel["price"] == max_price and len(selected_hotels) <= 3:
    #             selected_hotels.append(hotel)
    #             afordable_hotels.remove(hotel)

    return render_template('departure.html', tours=tours, departures=departures, departure=departure)


@app.route('/tours/<int:id>/')
def render_tour(id):
    return render_template('tour.html', tours=tours, id=id)



app.run('0.0.0.0',8000, debug=True)
