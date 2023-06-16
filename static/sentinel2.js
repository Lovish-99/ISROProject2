// stablishing the WebSocket connection.
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/action/'
);

// function for getting the messeges.
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    // document.querySelector('#chat-log').textContent = data.message;
    document.querySelector('#chat-log').value += (data.message +'\n');
};

// function for closing the connection
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

// WebSocket function for passing the values in a socket connection.
document.querySelector('#chat-message-submit').onclick = function(e) {
    var pfname = "";
    if(document.getElementById("plateform1").checked){
        pfname = document.getElementById("plateform1").value;
        console.log(pfname);
    }
    else if(document.getElementById("plateform2").checked){
        pfname = document.getElementById("plateform2").value;
        console.log(pfname);
    }
    else if(document.getElementById("plateform3").checked){
        pfname = document.getElementById("plateform3").value;
        console.log(pfname);
    }

    /* pset the values for the querry that we send to the 
    consumer for generating the search querry */
    chatSocket.send(JSON.stringify({
        'message': "start",
        'key1': document.getElementById("starttime").value,
        'key2': document.getElementById("endtime").value,
        'key3': document.getElementById("point").innerHTML,
        'key4': pfname,
        'key5': document.getElementById("ptype").value,
        'key6': document.getElementById("polarmode").value,
        'key7': document.getElementById("sensormode").value,
        'key8': document.getElementById("cloudper").value
    }));
};

// Function for filling the entries accordig to our need.
function Check(){
    //  check for plateform1 i.e. Sentinel-1
    if(document.getElementById("plateform1").checked){
        var lst1 = ["None", "SLC", "GRD", "OCN"];
        var lst2 = ["None", "HH", "VV", "HV", "VH", "HH HV", "VV VH"];
        var lst3 = ["None", "SM", "IW", "EW", "WV"];
        document.getElementById("datahub1").style.visibility = "visible";
        var y = "", z = "", w = "";
        for(i = 0; i < lst1.length; i++){
            y =y + "<option value='"+ lst1[i] +"'>"+lst1[i]+"</option>"+"<br>";
        };
        document.getElementById("ptype").innerHTML = y;
    
        document.getElementById("datahub2").style.visibility = "visible";
        for(i = 0; i < lst2.length; i++){
            z =z + "<option value='"+ lst2[i] +"'>"+lst2[i]+"</option>"+"<br>";
        };
        document.getElementById("sensormode").innerHTML = z;
        
        document.getElementById("datahub3").style.visibility = "hidden";
        for(i = 0; i < lst3.length; i++){
            w =w + "<option value='"+ lst3[i] +"'>"+lst3[i]+"</option>"+"<br>";
        };
        document.getElementById("polarmode").innerHTML = w;
    }
    
    //  check for plateform1 i.e. Sentinel-2
    else if(document.getElementById("plateform2").checked){
        var lst = ["None", "S2MSI1C", "S2MSI2A", "S2MSI2Ap"];
        document.getElementById("datahub1").style.visibility = "visible";
        document.getElementById("datahub2").style.visibility = "hidden";
        document.getElementById("datahub3").style.visibility = "visible";
        var w = "";
        for(i = 0; i < lst.length; i++){
            w =w + "<option value='"+ lst[i] +"'>"+lst[i]+"</option>"+"<br>";
        };
        document.getElementById("ptype").innerHTML = w;
    }

    //  check for plateform1 i.e. Sentinel-3
    else if(document.getElementById("plateform3").checked){
        var lst1 = ["None", "SR1_SRA___", "SR1_SRA_A_", "SR1_SRA_BS","SR2_LAN___","OL_1_EFR___","OL_1_ERR___","OL_2_LFR___","OL_2_LRR___","SL_1_RBT___","SL_2_LST___","SY_2_SYN___","SY_2_V10___","SY_2_VG1___","SY_2_VGP___"];
        document.getElementById("datahub1").style.visibility = "visible";
        document.getElementById("datahub2").style.visibility = "hidden";
        document.getElementById("datahub3").style.visibility = "hidden";
        var w = "";
        for(i = 0; i < lst1.length; i++){
            w =w + "<option value='"+ lst1[i] +"'>"+lst1[i]+"</option>"+"<br>";
        };
        document.getElementById("ptype").innerHTML = w;
    }
}