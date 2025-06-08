const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const PORT = 3000;
const dataFile = path.join(__dirname, 'leaderboard.json');

app.use(express.json());

function loadData() {
    if (!fs.existsSync(dataFile)) return {};
    return JSON.parse(fs.readFileSync(dataFile));
}

function saveData(data) {
    fs.writeFileSync(dataFile, JSON.stringify(data, null, 2));
}

app.get('/api/leaderboard', (req, res) => {
    const data = loadData();
    const sorted = Object.entries(data).sort((a, b) => b[1] - a[1]).slice(0, 10);
    res.json(sorted.map(([name, rating]) => ({ name, rating })));
});

app.post('/api/result', (req, res) => {
    const { winner, loser } = req.body;
    if (!winner || !loser) return res.status(400).end();
    const data = loadData();
    if (!data[winner]) data[winner] = 1000;
    if (!data[loser]) data[loser] = 1000;
    data[winner] += 10;
    data[loser] = Math.max(100, data[loser] - 10);
    saveData(data);
    res.json({ success: true });
});

app.use(express.static(__dirname));

app.listen(PORT, () => {
    console.log(`Chomp server running on http://localhost:${PORT}`);
});
