import os
import sys
import random
import googlemaps
import pprint
import time
import geocoder
import flask
from flask import Flask
import handlers.chooser as chooser
import handlers.location_based as location

#from flask.ext.bootstrap import Bootstrap  

app = Flask(__name__)

#bootstrap = Bootstrap(app)


@app.route('/')
def index():
    resturants = chooser.choose_resturant(shuffle=True)
    return flask.render_template('index.html', rest1=resturants[0], 
                                 rest2=resturants[1], rest3=resturants[2],
                                 rest4=resturants[3], rest5=resturants[4])



@app.route('/location')
def location_based():
    resturants = location.pick_five()
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
