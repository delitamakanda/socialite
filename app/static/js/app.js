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


(function(){
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker
     .register('service-worker.js')
     .then(function() {
        console.log('Service Worker Registered');
      });
  }
})()
