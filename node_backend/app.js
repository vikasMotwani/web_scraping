const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// Serve the HTML file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Serve the JSON file
app.get('/data.json', (req, res) => {
    res.sendFile(path.join(__dirname, '../json_data/company_careers.json'));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
