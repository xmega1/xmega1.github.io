setInterval(() => {
    const most = new Date();
    document.getElementById("date").innerText = most.toLocaleTimeString();
}, 1000);