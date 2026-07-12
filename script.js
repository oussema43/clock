async function updateClock() {
    const data = await pywebview.api.get_time();

    document.getElementById("time").innerText = data.time;
    document.getElementById("date").innerText = data.date;
}

setInterval(updateClock, 1000);
updateClock();