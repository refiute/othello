var host = "ws://192.168.50.177:1919/ws";
var socket = new WebSocket(host);

if(socket){
	socket.onopen = function(){
		console.log("connection opened");
		socket.send("ok");
	}

	socket.onclose = function(){
		console.log("connection has been closed");
	}

	socket.onmessage = function(msg){
		data = JSON.parse(msg.data);
		console.log(data);
		switch(data["cmd"]) {
			case "end": // data = {"cmd": "end"}
				console.log("end");
				break;

			case "pass": // data = {"cmd": "pass", "color": 0 or 1}
				setTimeout('socket.send("ok");', 1000);
				console.log("pass");
				break;

			case "invalid": // data = {"cmd": "invalid", "color": 0 or 1}
				console.log("invalid");
				break;

			case "hand": // data = {"cmd": "hand", "color": 0 or 1, "mp": 0:white, 1:black, -1: empty}
				add_board(data.mp);
				setTimeout('socket.send("ok");', 1000);
				console.log("hand");
				break;
		}
	}
}
