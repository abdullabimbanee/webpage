// Simulate fetching health data
function generateRandomValue(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function updateVitals() {
    const heartRate = generateRandomValue(60, 100);
    const systolic = generateRandomValue(100, 130);
    const diastolic = generateRandomValue(70, 90);
    const oxygen = generateRandomValue(95, 100);
    const temperature = (Math.random() * (37.5 - 36) + 36).toFixed(1);

    document.getElementById("heartRateValue").textContent = heartRate;
    document.getElementById("bpValue").textContent = `${systolic}/${diastolic}`;
    document.getElementById("oxygenValue").textContent = oxygen;
    document.getElementById("tempValue").textContent = temperature;
}

// Initial update
updateVitals();

// Update vitals every 5 seconds
setInterval(updateVitals, 5000);
