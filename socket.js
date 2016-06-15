var host = "ws://localhost:1919/ws";
var socket = new WebSocket(host);
if(socket){
	socket.onopen() = function(){
		console.log("connection opened");
		socket.send("ok");
	}
	socket.onclose() = function(){
		console.log("connection has been closed");
	}
	socket.onmessage() = function(msg){
		console.log(msg.data);
		data = JSON.parse(msg.data)
		switch(data["cmd"]){
		    case "end": // data = {"cmd": "end"}
		        break;
		        
		    case "pass": // data = {"cmd": "pass", "color": 0 or 1}
		        break;
		        
		    case "invalid": // data = {"cmd": "invalid", "color": 0 or 1}
		        break;
		        
		    case "hand": // data = {"cmd": "hand", "color": 0 or 1, "mp": 0-white, 1:black, -1: empty}
		        break;
		}
		socket.send("ok");
	}
}
