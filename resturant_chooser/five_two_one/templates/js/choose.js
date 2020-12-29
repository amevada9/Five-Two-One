var resturants = [
    "Chipotle", 
    "Willy's",
    "Taco Bell",
    "Olive Garden",
    "Panera Bread",
    "Carrabas",
    "Macroni Grill",
    "Fresh to Go",
    "Pinch of Spice",
    "Chick-Fil-A",
    "Zaxby's"
]

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
    rests = shuffle(resturants)
    document.getElementById("rest1").innerHTML = resturants[0];
    document.getElementById("rest2").innerHTML = resturants[1];
    document.getElementById("rest3").innerHTML = resturants[2];
    document.getElementById("rest4").innerHTML = resturants[3];
    document.getElementById("rest5").innerHTML = resturants[4];
}