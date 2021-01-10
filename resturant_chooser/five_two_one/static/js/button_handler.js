
// Buttons on the screen we want to do stuff with 
let but1 = document.getElementById("but1");
let but2 = document.getElementById("but2");
let but3 = document.getElementById("but3");
let but4 = document.getElementById("but4");
let but5 = document.getElementById("but5");
let submit = document.getElementById("submit");
let start_over = document.getElementById("start_over");
let final_choice_text = document.getElementById("final_choice");
let choose_again = document.getElementById("choose_again");

var choices = []
var clicks = 0

var has_clicked = [false, false, false, false, false];

but1.addEventListener("click", but1_handler);
but2.addEventListener("click", but2_handler);
but3.addEventListener("click", but3_handler);
but4.addEventListener("click", but4_handler);
but5.addEventListener("click", but5_handler)
submit.addEventListener("click", submit_button_handler)
start_over.addEventListener("click", start_over_button_handler);
choose_again.addEventListener("click", choose_again_handler)

function but1_handler() {
    if (clicks < 2 && !has_clicked[0]) {
        but1.style.background = 'blue';
        but1.style.color = 'white';
        choices.push(but1.innerHTML);
        has_clicked = true;
        clicks = clicks + 1;
    } 
}

function but2_handler() {
    if (clicks < 2 && !has_clicked[1]) {
        but2.style.background = 'gray';
        but2.style.color = 'white';
        choices.push(but2.innerHTML);
        has_clicked = true;
        clicks = clicks + 1;
    } 
}

function but3_handler() {
    if (clicks < 2 && !has_clicked[2]) {
        but3.style.background = 'green';
        but3.style.color = 'white';
        choices.push(but3.innerHTML);
        has_clicked = true;
        clicks = clicks + 1;
    } 
}

function but4_handler() {
    if (clicks < 2 && !has_clicked[3]) {
        but4.style.background = 'red';
        but4.style.color = 'white';
        choices.push(but4.innerHTML);
        has_clicked = true;
        clicks = clicks + 1;
    } 
}

function but5_handler() {
    if (clicks < 2 && !has_clicked[4]) {
        but5.style.background = '#f8c10a';
        but5.style.color = 'black';
        choices.push(but5.innerHTML);
        has_clicked = true;
        clicks = clicks + 1;
    } 
}

function submit_button_handler() {
    var random_idx = Math.floor(Math.random() * choices.length)
    if (clicks >= 2) {
        final_choice_text.innerHTML = "Tonight's Place to Eat: " + choices[random_idx];
    }
    else if (clicks == 1) {
        final_choice_text.innerHTML = "Choose 2 resturants!";
    }
    else {
        final_choice_text.innerHTML = "Choose 1 more resturant!";
    }
}

function start_over_button_handler() {
    clicks = 0;
    choices = [];
    but1.style.background = 'white';
    but1.style.color = 'blue';

    but2.style.background = 'white';
    but2.style.color = 'gray';

    but3.style.background = 'white';
    but3.style.color = 'green';

    but4.style.background = 'white';
    but4.style.color = 'red';

    but5.style.background = 'white';
    but5.style.color = '#f8c10a';
}

function choose_again_handler() {
    window.location.reload();
}
