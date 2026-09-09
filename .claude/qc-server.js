// Servidor estatico minimo, solo para revisar paginas en el navegador durante el QC.
// No forma parte de ningun entregable ni se publica en la tienda.
const http = require('http');
const fs = require('fs');
const path = require('path');
const raiz = path.join(__dirname, '..');
const tipos = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript',
  '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg' };
http.createServer((req, res) => {
  const rel = decodeURIComponent(req.url.split('?')[0]).replace(/^\/+/, '');
  const destino = path.join(raiz, rel);
  if (!destino.startsWith(raiz)) { res.writeHead(403).end('no'); return; }
  fs.readFile(destino, (err, buf) => {
    if (err) { res.writeHead(404, { 'Content-Type': 'text/plain' }).end('404 ' + rel); return; }
    res.writeHead(200, { 'Content-Type': tipos[path.extname(destino)] || 'text/plain',
      'Cache-Control': 'no-store' });
    res.end(buf);
  });
}).listen(4173, () => console.log('QC en http://localhost:4173'));
