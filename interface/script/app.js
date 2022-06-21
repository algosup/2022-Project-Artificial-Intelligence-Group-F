


let message = document.getElementById('message');
let bar = document.getElementById('myBar');
let hide = document.getElementById('hide');
let border = document.getElementById('border');


fr = '';
en = '';


const timer = ms => new Promise(res => setTimeout(res, ms))

async function load () { // We need to wrap the loop into an async function for this to work
for (var i = 0; i < i+1; i++) {


    $.getJSON('./predict/value.json', function (jd) {


        fr = ((Math.round(jd.french * 100)/100).toFixed(2))*100;
        en = ((Math.round(jd.english * 100)/100).toFixed(2))*100;

        if (en >= 0 && en < 33) {
            message.innerHTML = "Careful, you are not speaking <b>English</b>";

            bar.style.backgroundColor = '#ff0000';

        } else if (en >= 33 && en < 66) {
            message.innerHTML = "Careful, I'm not sure you speak <b>English</b>";


            bar.style.backgroundColor = '#FFA500';
        }
        else if (en >= 66 && en <= 100) {
            message.innerHTML = "You are speaking <b>English</b>";

            bar.style.backgroundColor = '#00ff00';
        }
        console.log(en);
        bar.innerHTML = en + '%';
        bar.style.width = en + '%';
        
    });
    await timer(3000); // then the created Promise can be awaited
}
}



$(document).ready(function () {

    load();
});
