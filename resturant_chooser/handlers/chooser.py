import random
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

def main():
    return choose_resturant()

if __name__ == '__main__':
    main()
