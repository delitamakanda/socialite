var cacheName = 'socialite-v1';
var filesToCache = [
  '/index.html',
  '/css/app.css',
  '/js/app.js',
  /* ...and other assets (jQuery, Materialize, fonts, etc) */
];

self.addEventListener('install', function(e) {
  console.log('[ServiceWorker] Install');
  e.waitUntil(
    caches.open(cacheName).then(function(cache) {
      console.log('[ServiceWorker] Caching app shell');
      return cache.addAll(filesToCache);
    })
  );
});

self.addEventListener('activate', function(e) {
  console.log('[ServiceWorker] Activate');
  e.waitUntil(
    caches.keys().then(function(keyList) {
      return Promise.all(keyList.map(function(key) {
        if (key !== cacheName) {
          console.log('[ServiceWorker] Removing old cache', key);
          return caches.delete(key);
        }
      }));
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.open(cacheName).then(function(cache) {
      return cache.match(event.request).then(function (response) {
        return response || fetch(event.request).then(function(response) {
          cache.put(event.request, response.clone());
          return response;
        });
      });
    })
  );
});

self.addEventListener('fetch', function(e) {
  console.log('[ServiceWorker] Fetch', e.request.url);
  e.respondWith(
    caches.match(e.request).then(function(response) {
      return response || fetch(e.request);
    })
  );
});

const networkReturned = false;
if ('caches' in window) {
  caches.match(app.apiURL).then(function(response) {
    if (response) {
      response.json().then(function(trends) {
        console.log('From cache...')
        if(!networkReturned) {
          app.updateTrends(trends);
        }
      });
    }
  });
}

fetch(app.apiURL)
.then(response => response.json())
.then(function(trends) {
  console.log('From server...')
  networkReturned = true;
  app.updateTrends(trends.items)
}).catch(function(err) {
  // Error
});





