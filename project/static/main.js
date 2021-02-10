try{
    var sock = new WebSocket('ws://' + window.location.host + '/ws/');
}
catch(err){
    var sock = new WebSocket('wss://' + window.location.host + '/ws/');
}

// show message in div#subscribe
function showMessage(message) {
    var messageElem = $('#subscribe'),
        height = 0;
    text = '<b>' + message['name'] + '</b>: ' + message['text']
    messageElem.append($('<p>').html(text));
    messageElem.find('p').each(function(i, value){
        height += parseInt($(this).height());
    });
    messageElem.animate({scrollTop: height});
}

function sendMessage(){
    sock.send($('[name="search_phrase"]').val());
    $('[name="search_phrase"]').val('').focus();
}

sock.onopen = function(){
    showMessage({'name': 'system', 'text': 'Connection to server started'})
}

// send message from form
$('#submit').click(function() {
    sendMessage();
});

// income message handler
sock.onmessage = function(event) {
  data = JSON.parse(event.data)  
  showMessage(data);
};

sock.onclose = function(event){
    if(event.wasClean){
        showMessage({'name': 'system', 'text': 'Clean connection end'})
    }else{
        showMessage({'name': 'system', 'text': 'Connection broken'})
    }
};

sock.onerror = function(error){
    showMessage(error);
}