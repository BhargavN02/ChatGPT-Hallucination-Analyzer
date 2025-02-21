chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log("Received message in background.js:", message);

    if (message.action === "calculateHallucination") {
        fetch("http://127.0.0.1:5000/check", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ response: message.text })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Hallucination Score from API:", data);
            chrome.storage.local.set({ hallucination_score: data.score });
        })
        .catch(error => {
            console.error("Error fetching hallucination score:", error);
            chrome.storage.local.set({ hallucination_score: "Error" });
        });
    }
});
