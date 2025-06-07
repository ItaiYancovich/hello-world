function isPrime(n) {
    if (n < 2) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    const limit = Math.floor(Math.sqrt(n)) + 1;
    for (let i = 3; i <= limit; i += 2) {
        if (n % i === 0) return false;
    }
    return true;
}

function generatePrimes(limit) {
    const primes = [];
    for (let num = 2; num <= limit; num++) {
        if (isPrime(num)) primes.push(num);
    }
    return primes;
}

function primeFactors(n) {
    const factors = [];
    let num = n;
    for (let p = 2; p <= Math.floor(Math.sqrt(num)); p++) {
        while (num % p === 0) {
            factors.push(p);
            num = Math.floor(num / p);
        }
    }
    if (num > 1) factors.push(num);
    return factors;
}

function nthPrime(n) {
    if (n < 1) throw new Error('n must be >= 1');
    let count = 0;
    let num = 1;
    while (count < n) {
        num += 1;
        if (isPrime(num)) count += 1;
    }
    return num;
}

function primePi(limit) {
    return generatePrimes(limit).length;
}

let chart;
function checkPrime() {
    const n = parseInt(document.getElementById('prime-input').value);
    const result = isPrime(n);
    document.getElementById('prime-result').innerText = result ? `${n} is prime` : `${n} is not prime`;
}

function showFactors() {
    const n = parseInt(document.getElementById('factor-input').value);
    const factors = primeFactors(n);
    document.getElementById('factor-result').innerText = `Factors: ${factors.join(', ')}`;
}

function listPrimes() {
    const limit = parseInt(document.getElementById('list-limit').value);
    const primes = generatePrimes(limit);
    document.getElementById('list-result').innerText = `Primes (${primes.length}): ${primes.join(', ')}`;

    const ctx = document.getElementById('prime-chart').getContext('2d');
    const data = {
        labels: primes.map((_, i) => i + 1),
        datasets: [{
            label: 'Prime Value',
            data: primes,
            pointRadius: 3,
            showLine: false,
            backgroundColor: 'rgba(54, 162, 235, 0.6)'
        }]
    };
    if (chart) chart.destroy();
    chart = new Chart(ctx, {type: 'scatter', data: data, options: {scales: {x: {title: {display: true, text: 'Index'}}, y: {title: {display: true, text: 'Prime'}}}}});
}

function showNthPrime() {
    const n = parseInt(document.getElementById('nth-input').value);
    const prime = nthPrime(n);
    document.getElementById('nth-result').innerText = `${n}-th prime is ${prime}`;
}

// --- Animated Prime Spiral ---
// Draw primes in a spiral pattern reminiscent of 3Blue1Brown-style visuals.
function primeSpiralAnimation(limit = 1000) {
    const canvas = document.getElementById('prime-animation');
    if (!canvas || !canvas.getContext) return;
    const ctx = canvas.getContext('2d');

    const primes = generatePrimes(limit);
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const scale = 4; // distance between successive spiral arms

    ctx.fillStyle = '#111';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    let idx = 0;
    function drawNext() {
        if (idx >= primes.length) return;
        const p = primes[idx];
        const r = Math.sqrt(p) * scale;
        const angle = p * 0.15;
        const x = centerX + r * Math.cos(angle);
        const y = centerY + r * Math.sin(angle);

        ctx.fillStyle = '#f0b90b';
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, 2 * Math.PI);
        ctx.fill();

        idx += 1;
        requestAnimationFrame(drawNext);
    }
    drawNext();
}

window.onload = function() {
    primeSpiralAnimation();
};
