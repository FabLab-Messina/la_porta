var ip_camera = '192.168.1.200';


function aggiorna_img() {
    var url = "http://" + ip_camera + ":81/snapshot.cgi?user=admin&pwd=&";
    var rand = Math.random();
    var url_unica = url+rand;
    var img = document.getElementById("stream-img");
    img.src = url_unica;
}

function apri_porta() {
    var request = new XMLHttpRequest();
    request.open('GET', "http://porta.fablabmessina.it:8080/fablab/porta/unlock", true);    
    request.send();
}

setInterval(aggiorna_img,100);
