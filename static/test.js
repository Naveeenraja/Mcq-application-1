var date = new Date();
const todaydate = document.querySelector('.date');
const todayday = document.querySelector('.day');
const todaytime = document.querySelector('.time');
const noofday =["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

function printDate(){
    var date = new Date();
    var day = date.getDate();
    var month = date.getMonth()+1;
    var year = date.getFullYear()
    todaydate.innerHTML = day + "/" + month + "/" + year
}
printDate();

function printDay(){
    var date = new Date();
    var today = date.getDay();
    var day = noofday[today];
    todayday.innerHTML = day
}
printDay();

function printTime(){
    var date = new Date();
    var hour = date.getHours();
    var min = date.getMinutes();
    var sec = date.getSeconds();
    var period = "AM"

    if (hour == 0){
        hour = 12;
    }
    if (hour > 12){
        hour = hour - 12;
        period = "PM"
    }
    if (hour < 10){
        hour = "0" + hour
    }
    if(min < 10){
        min = "0" + min
    }
    if(sec < 10){
        sec = "0" + sec
    }
    var time = hour + ":" + min + ":" + sec + " " + period;
    todaytime.innerHTML = time;
    setTimeout(printTime, 1000)
}
printTime();


// Initialize the timer
var timeLeft = 120;  // seconds
var timerId = setInterval(countdown, 1000);
function countdown() {
    if (timeLeft == 0) {
        clearTimeout(timerId);
        document.getElementById("timer").innerHTML = "Time's up!";
        window.location.href = "/nextpage.html";
    } else {
        var minutes = Math.floor(timeLeft/60);
        var seconds = timeLeft % 60;
        document.getElementById("timer").innerHTML = "Time " + minutes +":" + seconds ;
        timeLeft--;
    }
}


// var countdown = 10;

// // Get a reference to the timer element
// var timer = document.getElementById("timer");

// // Start the countdown
// var countdownInterval = setInterval(function() {
//     countdown--;

//     // convert the seconds to minutes
//     var minutes = Math.floor(countdown / 60);
//     var remainingSeconds = countdown % 60;

//     // Update the timer element with the current time remaining
//     timer.innerHTML = minutes + ":" + remainingSeconds;

//     // Check if the countdown is finished
//     if (countdown <= 0) {
//         clearInterval(countdownInterval);
//         timer.innerHTML = "Time's up!";
//         window.location.href = "/nextpage.html";
//     }
// }, 1000);