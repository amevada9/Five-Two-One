object.addEventListener("load", choose);

function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }
    return array;
}   
function choose() {
    var resturants = [
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
    resturants = shuffle(resturants)
    document.getElementById("but1").innerHTML = resturants[0];
    document.getElementById("but2").innerHTML = resturants[1];
    document.getElementById("but3").innerHTML = resturants[2];
    document.getElementById("but4").innerHTML = resturants[3];
    document.getElementById("but5").innerHTML = resturants[4];
}
