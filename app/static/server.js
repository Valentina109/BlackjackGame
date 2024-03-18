const express = require('express');
const path = require('path');  // Import the 'path' module
const mysql = require('mysql');
const app = express();
const port = 3000;

// Create MySQL connection pool
const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: '123',
    database: 'blackjack',
});

// Serve HTML page
app.get('/playgame', (req, res) => {
    // Use __dirname and path.join to get the correct file path
    const filePath = path.join(__dirname, 'templates', 'playgame.html');
    res.sendFile(filePath);
});

// Endpoint to get player game history and win percentage
app.get('/statistics', (req, res) => {
    pool.getConnection((err, connection) => {
        if (err) throw err;

        connection.query('SELECT * FROM player_game_history', (error, results, fields) => {
            connection.release();
            if (error) throw error;
            const totalGames = results.length;
            const totalWins = results.filter(result => result.outcome === 'win').length;
            const winPercentage = (totalWins / totalGames) * 100 || 0;

            const statistics = {
                totalGames,
                totalWins,
                winPercentage,
            };
            res.json(statistics);
        });
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});