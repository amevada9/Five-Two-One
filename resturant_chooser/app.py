import os
import sys
import random
import googlemaps
import pprint
import time
import geocoder
import flask
from flask import Flask
import handlers.chooser

#from flask.ext.bootstrap import Bootstrap  

app = Flask(__name__)

#bootstrap = Bootstrap(app)


def choose_resturant(shuffle=True):
    resturant_options = [
        "Chipotle",
        "Willy's",
        "Taco Bell",
        "Olive Garden",
        "Panera Bread",
        "Carrabas",
        "Macroni Grill",
        "Fresh to Go",
        "Chick-Fil-A",
        "Zaxby's",
        "Arby's",
        "McDonalds",
        "Dominos",
        "Pizza Hut",
        "Subway",
        "KFC",
        "Whataburger",
        "In-N-Out Burger"
    ]
    if shuffle:
        random.shuffle(resturant_options)
    return resturant_options[:5]

@app.route('/')
def index():
    resturants = choose_resturant(shuffle=True)
    return flask.render_template('index.html', rest1=resturants[0], 
                                 rest2=resturants[1], rest3=resturants[2],
                                 rest4=resturants[3], rest5=resturants[4])


def pick_five():
    # from GoogleMapsAPIKey import get_my_key # should implement this again

    # food types in Places API: bakery, bar, cafe, meal_delivery, meal_takeaway, restaurant

    API_KEY = 'AIzaSyAthdZ4vpbtc6o_Gbqa2tc4l4AuwxisDns'  # get_my_key()

    # getting current location
    curr_loc = geocoder.ip('me').latlng
    curr_loc_string = str(curr_loc[0]) + ", " + str(curr_loc[1])

    # define client
    gmaps = googlemaps.Client(key=API_KEY)

    #defining fiels which user can specify later
    max_price_inp = 3
    distance_inp = 3
    meter_dist = distance_inp * 1600
    type_inp = 'restaurant'

    # get request
    places_request = gmaps.places_nearby(location=curr_loc_string, radius=meter_dist,
                                         open_now='True', type=type_inp, min_price=0, max_price=max_price_inp)

    place_set = set()  # in a set so only one of each restaurant is in there
    for place in places_request['results']:
        my_place_id = place['name']
        # my_fields = ['name']
        # place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
        place_set.add(my_place_id)

    return random.sample(set(place_set), 5)

@app.route('/location')
def location_based():
    resturants = pick_five()
    return flask.render_template('index.html', rest1=resturants[0],
                                 rest2=resturants[1], rest3=resturants[2],
                                 rest4=resturants[3], rest5=resturants[4])


@app.errorhandler(404) 
def page_not_found(e):
    return flask.render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return flask.render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
