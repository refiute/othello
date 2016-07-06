var Canvas;
var Ctx;

var CanvasW;
var CanvasH;
var CenterX;
var CenterY;
var CenterR;



function Loop(){
	update();
	DrawBox(0,0,CanvasW,CanvasH,GetColor(255,255,255),1);
	draw();
	setTimeout(Loop, 10);
}

window.onload = function(){
	CanvasInit();
	init();
	Loop();
}


function CanvasInit(){
	
	Canvas = document.getElementById("cvs");
	var b = document.body;
	var d = document.documentElement;
	Canvas.width = Math.max(b.clientWidth , b.scrollWidth, d.scrollWidth, d.clientWidth);
	Canvas.height = Math.max(b.clientHeight , b.scrollHeight, d.scrollHeight, d.clientHeight);
	Canvas.height *= 0.7;
	Canvas.width = 800;
	Canvas.height = 600;
	
	CanvasW = Canvas.width;
	CanvasH = Canvas.height;
	CenterX = CanvasW/2;
	CenterY = CanvasH/2;
	CenterR = CenterX;
	if(CenterY < CenterR)CenterR = CenterY;
	if(!Canvas || !Canvas.getContext)return false;
	Ctx = Canvas.getContext('2d');
	
}



//ここからdxlib風
function GetColor(red, green, blue){
	return "rgb("+red+","+green+","+blue+")";
}

function DrawBox(X1,Y1,X2,Y2,Color,FillFlg){
	if(FillFlg){
		Ctx.fillStyle = Color;
		Ctx.fillRect(X1,Y1,X2-X1,Y2-Y1);
	}
	else{
		Ctx.strokeStyle = Color;
		Ctx.strokeRect(X1,Y1,X2-X1,Y2-Y1);
	}
}

function DrawLine(X1,Y1,X2,Y2,Color){
	Ctx.strokeStyle=Color;
	Ctx.beginPath();
	Ctx.moveTo(X1, Y1);
	Ctx.lineTo(X2, Y2);
	Ctx.stroke();
}

function DrawString(X,Y,String,Color){
	//関数呼ぶ前に
	//Ctx.font = "20px 'Times New Roman'";
	//Ctx.textAlign = "center";
	Ctx.fillStyle=Color;
	Ctx.fillText(String,X,Y+16);
}

function LoadGraph(FileName){
	var TMPIMG = new Image();
	TMPIMG.src=FileName;
	return TMPIMG;
}

function DrawGraph(X,Y,GrHandle,TransFlag){
	Ctx.drawImage(GrHandle,X,Y);
}

function DrawCircle(X,Y,R,Color,FillFlag){
	if(FillFlag){
		Ctx.fillStyle = Color;
		Ctx.beginPath();
		Ctx.arc(X, Y, R, 0, Math.PI*2, true);
		Ctx.fill();
	}
	else{
		Ctx.strokeStyle=Color;
		Ctx.beginPath();
		Ctx.arc(X, Y, R, 0, Math.PI*2, false);
		Ctx.stroke();
	}
}



