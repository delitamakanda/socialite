'use strict';

$(function() {
    var close = $('.close-btn');
    var i;

    for (i = 0; i < close.length; i++) {
        close.on('click', function(){
            var div = $(this).parent();
            div.css('opacity', 0);
            setTimeout(function() {
                div.css('display', 'none');
            }, 600);
        })
    }
});

var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});
