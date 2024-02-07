"use strict"

let sock;   // global

function sendMessage()
{
    console.log("send");
    let input = document.getElementById("mess");
    let msg = input.value;
    input.value = "";

    sock.send( msg );

    //let box = document.getElementById("chatbox");
    //box.value += "\n"+ msg;


}

function messageReceived(ev)
{
    let box = document.getElementById("chatbox");
    let msg = ev.data;
    console.log(msg);
    box.value += "\n"+ msg;
}

function main()
{
    sock = new WebSocket("ws://"+document.location.host+"/sock");
    sock.addEventListener("open", ()=>{
        let b = document.getElementById("sendButt");
        b.disabled = 0;

    })

    sock.addEventListener("message", messageReceived)
}

main();