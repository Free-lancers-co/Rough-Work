function displayTime(){
    var dateTime = new Date();
    var hrs = dateTime.getHours();
    var min = dateTime.getMinutes();
    var sec = dateTime.getSeconds();
    var sessions = document.getElementById('sessions');

    if(hrs >= 12){
        sessions.innerHTML = 'PM';
    }
    else{
        sessions.innerHTML = 'AM';
    }

    if (hrs > 12){
        hrs = hrs - 12
    }


    document.getElementById('hours').innerHTML = hrs;
    document.getElementById('minutes').innerHTML = min;
    document.getElementById('seconds').innerHTML = sec;
}

setInterval(displayTime, 10);