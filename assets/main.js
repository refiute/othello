var Board = [
[2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2],
[2,2,2,0,1,2,2,2],
[2,2,2,1,0,2,2,2],
[2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2]
];

var Boards = new Array(65);
var mn,mx,pos;
var bk,wh,gr;

function init(){
	Ctx.font = "32px 'Times New Roman'";
	Boards[0]=Board;
	mn=0;
	mx=0;
	pos=0;
}

function reset(){
	mn=0;
	mx=0;
	pos=0;
}

function add_board(mp){
	if(mx>=60)return;
	mx++;
	Boards[mx]=mp;
	if(document.Form.auto.checked){
		pos=mx;
	}
}

function sta(){
	pos=mn;
}
function pre(){
	if(pos>mn)pos--;
}
function nxt(){
	if(pos<mx)pos++;
}
function end(){
	pos=mx;
}

function update(){
	wh=0;
	bk=0;
	gr=0;
	for(var y=0;y<8;y++){
		for(var x=0;x<8;x++){
			if(Boards[pos][y][x]==0)wh++;
			else if(Boards[pos][y][x]==1)bk++;
			else gr++;
		}
	}
}

function draw(){
	
	for(var y=0;y<=8;y++){
		DrawLine(0,y*64,512,y*64,GetColor(0,0,0));
	}
	for(var x=0;x<=8;x++){
		DrawLine(x*64,0,x*64,512,GetColor(0,0,0));
	}
	
	for(var y=0;y<8;y++){
		for(var x=0;x<8;x++){
			if(Boards[pos][y][x]==0)DrawCircle(x*64+32,y*64+32,24,GetColor(0,0,0),0);
			if(Boards[pos][y][x]==1)DrawCircle(x*64+32,y*64+32,24,GetColor(0,0,0),1);
			
		}
	}
	DrawString(0,550,""+pos+"手目/"+mx+"手 , 白:"+wh+" , 黒:"+bk+" , 空:"+gr,GetColor(0,0,0));
	
	DrawBox(550,0,600,512,GetColor(0,255,255),1);
	DrawBox(550,0,600,wh*8,GetColor(255,255,255),1);
	DrawBox(550,0,600,wh*8,GetColor(0,0,0),0);
	DrawBox(550,512-bk*8,600,512,GetColor(0,0,0),1);
	
	
}

