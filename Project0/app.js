// Import the http module
const http = require('http');

// Define the port and hostname
const port = 3000;
const hostname = '127.0.0.1';

// Create the server
const server = http.createServer((req, res) => {
  res.statusCode = 200; // Set status code to 200 (OK)
  res.setHeader('Content-Type', 'text/plain'); // Set content type to plain text
  res.end('Hello, World!\n'); // Send response
});

// Start the server
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
