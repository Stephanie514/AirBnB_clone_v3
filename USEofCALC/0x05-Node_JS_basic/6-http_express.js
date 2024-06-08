// Importing the Express framework
const express = require('express');

// Express application
const app = express();

// Defining the port number
const PORT = 1245;

// handle GET requests to the root endpoint '/'
app.get('/', (_, res) => {
  // Send response with message
  res.send('Hello Holberton School!');
});

// Starting the server and listening on the specified port
app.listen(PORT, () => {
  // Logging a message to the console when the server starts
  console.log(`Server listening on port ${PORT}`);
});

// Exporting the Express application
module.exports = app;
