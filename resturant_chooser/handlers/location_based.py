import random
import googlemaps
import pprint
import time
import geocoder


def get_key():
    with open('./api_key.txt') as f:
        key = f.readline()
        print(key)
        return key



def pick_five():
    # from GoogleMapsAPIKey import get_my_key # should implement this again 

    # food types in Places API: bakery, bar, cafe, meal_delivery, meal_takeaway, restaurant

    API_KEY = '' #get_my_key()

    # getting current location 
    curr_loc= geocoder.ip('me').latlng
    curr_loc_string = str(curr_loc[0]) + ", " + str(curr_loc[1])

    # define client 
    gmaps = googlemaps.Client(key = API_KEY)

    #defining fiels which user can specify later
    max_price_inp = 3
    distance_inp = 3
    meter_dist = distance_inp * 1600
    type_inp = 'restaurant'


    # get request 
    places_request = gmaps.places_nearby(location = curr_loc_string, radius = meter_dist, open_now = 'True', type = type_inp, min_price = 0, max_price = max_price_inp)
 

    place_set = set() # in a set so only one of each restaurant is in there 
    for place in places_request['results']:
        my_place_id = place['name']
        # my_fields = ['name']
        # place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
        place_set.add(my_place_id)

    return random.sample(set(place_set), 5)
        
