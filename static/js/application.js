
var mousePos={x:0,y:0,btn:0,dx:0,dy:0}
var keyBoard={code:0}
var textPos={x:0,y:0}
document.onmousemove = handleMouseMove;
document.onmousedown = handleMouseDown;
document.onmouseup = handleMouseUp;
document.onkeydown = handleKeyDown;
document.onkeyup = handleKeyUp;
function handleKeyDown(event) {
  //<- 37, ^ 38, -> 39, v 40
  //enter 13, esc 27, space 32
  //a 65
  keyBoard.code = event.keyCode
}
function handleKeyUp(event) {
  keyBoard.code = 0
}
function handleMouseDown(event) {
  premousePos = mousePos
  if ('which' in event) {
    mousePos.btn = event.which
  }else{
    if ('button' in event) {
      mousePos.btn = event.button
    }   
  }
}
function handleMouseUp(event) {
  mousePos.btn = 0
  premousePos = mousePos
}
function handleMouseMove(event) {
  var dot, eventDoc, doc, body, pageX, pageY, dx,dy;
  event = event || window.event
  if (event.pageX == null && event.clientX != null) {
    eventDoc = (event.target && event.target.ownerDocument) || document;
    doc = eventDoc.documentElement;
    body = eventDoc.body;
    event.pageX = event.clientX +
      (doc && doc.scrollLeft || body && body.scrollLeft || 0) -
      (doc && doc.clientLeft || body && body.clientLeft || 0);
    event.pageY = event.clientY +
      (doc && doc.scrollTop  || body && body.scrollTop  || 0) -
      (doc && doc.clientTop  || body && body.clientTop  || 0 );
  }

  if ('which' in event) {
    mousePos.btn = event.which
  }else{
    if ('button' in event) {
      mousePos.btn = event.button
    }   
  }

  if (mousePos.btn == 1){
    dx = event.pageX - premousePos.x
    dy = event.pageY - premousePos.y
  }else{
    dx = 0
    dy = 0
  }
  mousePos = {
    x: event.pageX,
    y: event.pageY,
    btn: mousePos.btn,
    dx: dx,
    dy: dy
  };
 
}

if (window.location.protocol == "https:") {
  var ws_scheme = "wss://";
} else {
  var ws_scheme = "ws://"
};

//var receivebox = new ReconnectingWebSocket(ws_scheme + location.host + "/receive");
//var sendbox = new ReconnectingWebSocket(ws_scheme + location.host + "/send");

function myDrawing()
{
  var canvas = document.getElementById("myCanvas");
  var ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.moveTo(0,0);
  ctx.lineTo(200,100);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(95, 50, 40, 0, 2 * Math.PI);
  ctx.stroke();
  //ctx.font = "30px Arial";
  //ctx.fillText("Hello World", mousePos.dx, mousePos.dy); 
  var img = new Image();
  img.src = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAIAAAACDbGyAAAAAXNSR0IArs4c6QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9oMCRUiMrIBQVkAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAADElEQVQI12NgoC4AAABQAAEiE+h1AAAAAElFTkSuQmCC";
  ctx.drawImage(img, mousePos.dx, mousePos.dy);

}

var myVar = setInterval(myTimer, 15);
function myTimer() {
  var d = new Date();
  document.getElementById("demo").innerHTML = d.toLocaleTimeString();
  //
  if("y" in mousePos){
  myMouseTable = document.getElementById("myMouse_Keyboard")
  //y
  myMouseTable.rows[2].cells[1].innerHTML = mousePos.y;
  //x
  myMouseTable.rows[3].cells[1].innerHTML = mousePos.x;
  //btn
  myMouseTable.rows[4].cells[1].innerHTML = mousePos.btn;
  //dx
  myMouseTable.rows[0].cells[1].innerHTML = mousePos.dx;
  //dy
  myMouseTable.rows[1].cells[1].innerHTML = mousePos.dy;
  //keycode
  myMouseTable.rows[5].cells[1].innerHTML = keyBoard.code;
  }
  myDrawing()
}
/*
receivebox.onopen = function() {
   console.log('receivebox opened');
}

receivebox.onclose = function() {
   console.log('receivebox closed');
}

receivebox.onmessage = function(message) {
  //console.log("receivebox: "+message.data);
  var data = JSON.parse(message.data);
  if (data.type == "log"){
    var d = new Date();
    //$("#debug-text").append(d+": "+data.text+"<br>")
    $("#debug-text").prepend(d+": "+data.text+"<br>")
  }else if (data.type == "img"){
   console.log('img');
   //$("#debug-text").append("<img src=\"data:image/jpeg;base64," + data.text + "\"><br>")
   $("#debug-text").prepend("<img src=\"data:image/jpeg;base64," + data.text + "\"><br>")
  }
}

sendbox.onopen = function() {
   console.log('sendbox opened');
}

sendbox.onclose = function() {
   console.log('sendbox closed');
}

sendbox.onmessage = function(message) {
  console.log("sendbox: "+message.data);
}

$("#input-form").on("submit", function(event) {
  event.preventDefault();
  var handle = $("#input-handle")[0].value;
  var type = $("#input-type")[0].value;
  var text   = $("#input-text")[0].value;
  console.log("input-form submit: "+ text);
  sendbox.send(JSON.stringify({ handle: handle, type: type, text: text }));
  $("#input-text")[0].value = "";
});

$('#logButton').on('click', function(event) {
  event.preventDefault();
  //console.log("takePicButton click");
  window.location.assign("http://"+location.host + "/logs");
  //sendbox.send(JSON.stringify({ handle: "", type: "cam", text: "requestPhoto" }));
});

$('#log2Button').on('click', function(event) {
  event.preventDefault();
  window.location.assign("http://"+location.host + "/log2h");
});
*/
