const cacheName = 'portfolio-v1';
const appShellFiles = [
  '/',
  '/manifest.json',
  '/avatar.jpg'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    (async () => {
      const cache = await caches.open(cacheName);
      await cache.addAll(appShellFiles);
    })()
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    (async () => {
      const r = await caches.match(e.request);
      if (r) return r;
      const response = await fetch(e.request);
      return response;
    })()
  );
});
