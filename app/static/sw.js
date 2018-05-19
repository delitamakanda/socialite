self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open('socialite').then(function(cache) {
            return cache.addAll([
                '/',
                '/manifest.json',
                '/css/app.css',
                '/js/app.js',
            ]);
        })
    );
});

self.addEventListener('fetch', function(event) {
    console.log(event.request.url);

    event.respondWith(
        caches.match(event.request).then(function(response) {
            return response || fetch(event.request);
        })
    );
    
});
