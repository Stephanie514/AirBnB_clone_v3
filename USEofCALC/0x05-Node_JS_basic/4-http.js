const http = require('http');

const serverPort = 1245;
const serverHost = 'localhost';

const server = http.createServer((req, res) => {
  const respText = 'Hello Holberton School!';

  res.setHeader('Content-Type', 'text/plain');
  res.setHeader('Content-Length', Buffer.byteLength(respText)); // Correctly calculated byte length
  res.statusCode = 200;
  res.end(respText); // response is properly ended
});

server.listen(serverPort, serverHost, () => {
  process.stdout.write(`Server listening at -> http://${serverHost}:${serverPort}\n`);
});

module.exports = server;
