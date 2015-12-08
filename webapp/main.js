function aggiorna_img(){
		var url = "http://192.168.2.133:81/snapshot.cgi?user=admin&pwd=&";
		var rand=Math.random();
		var url_unica= url+rand;
		var img=document.getElementById("stream-img");
		img.src=url_unica;
}
setInterval(aggiorna_img,100);
