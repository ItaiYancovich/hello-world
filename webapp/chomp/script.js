const rows = 4;
const cols = 6;
let board = [];
let currentPlayer = 0; // 0 or 1
let players = [];

function initBoard() {
    board = [];
    for (let r = 0; r < rows; r++) {
        const row = [];
        for (let c = 0; c < cols; c++) {
            row.push(true); // true = cookie present
        }
        board.push(row);
    }
    renderBoard();
}

function renderBoard() {
    const boardDiv = document.getElementById('board');
    boardDiv.innerHTML = '';
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            if (r === 0 && c === 0) cell.classList.add('poison');
            if (!board[r][c]) cell.style.visibility = 'hidden';
            cell.dataset.row = r;
            cell.dataset.col = c;
            cell.onclick = onCellClick;
            boardDiv.appendChild(cell);
        }
    }
}

function onCellClick(event) {
    const r = parseInt(event.target.dataset.row);
    const c = parseInt(event.target.dataset.col);
    if (!board[r][c]) return;
    for (let i = r; i < rows; i++) {
        for (let j = c; j < cols; j++) {
            board[i][j] = false;
        }
    }
    if (r === 0 && c === 0) {
        endGame(1 - currentPlayer);
    } else if (isBoardEmpty()) {
        endGame(currentPlayer);
    } else {
        currentPlayer = 1 - currentPlayer;
        updateStatus();
        renderBoard();
    }
}

function isBoardEmpty() {
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (board[r][c]) return false;
        }
    }
    return true;
}

function updateStatus() {
    document.getElementById('status').innerText = `${players[currentPlayer]}'s turn`;
}

function endGame(winner) {
    document.getElementById('status').innerText = `${players[winner]} wins!`;
    updateRatings(winner);
    populateLeaderboard();
    document.querySelectorAll('.cell').forEach(c => c.onclick = null);
}

function resetGame() {
    currentPlayer = 0;
    initBoard();
    updateStatus();
}

function startGame() {
    const name = document.getElementById('player-name').value.trim();
    if (!name) return;
    players = [name, 'Computer'];
    currentPlayer = 0;
    document.getElementById('login').style.display = 'none';
    document.getElementById('game-container').style.display = 'block';
    initBoard();
    updateStatus();
}

async function updateRatings(winnerIndex) {
    const winner = players[winnerIndex];
    const loser = players[1 - winnerIndex];
    await fetch('api/result', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ winner, loser })
    });
}

async function populateLeaderboard() {
    const list = document.getElementById('leaderboard');
    list.innerHTML = '';
    const res = await fetch('api/leaderboard');
    const entries = await res.json();
    for (const entry of entries) {
        const li = document.createElement('li');
        li.innerText = `${entry.name}: ${entry.rating}`;
        list.appendChild(li);
    }
}

window.onload = populateLeaderboard;
