"use strict";
console.log(document.location);

function submit()
{
    let upName = document.getElementById("upName").value;
    let upEmail = document.getElementById("upEmail").value;
    let upDOB = document.getElementById("upDOB").value;
    let upPic = document.getElementById("upPic").files[0];
    if (!upPic)
    {
        console.log("NO!");
        return;
    }
    console.log("Updated Info:",upName, upEmail, upDOB);
    


    let FR = new FileReader();
    FR.addEventListener("load", ()=>
    {
        let L =
        {
            uppName: upName,
            uppEmail: upEmail,
            uppDOB: upDOB,
            uppPic: btoa(FR.result),
            uuName: document.location.search.substring(1)
        };

        fetch ("/updates",
        {
            method: "POST",
            body: JSON.stringify(L)
        })
        .then(()=> {document.location="/profile/" + document.location.search.substring(1)});
    } )

    FR.readAsBinaryString(upPic);


}