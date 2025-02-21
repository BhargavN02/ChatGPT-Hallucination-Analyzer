document.addEventListener("DOMContentLoaded", () => {
    const scoreElement = document.getElementById("score");
    const checkButton = document.getElementById("checkButton");

    checkButton.addEventListener("click", () => {
        scoreElement.innerText = "Checking...";
        scoreElement.className = ""; // Reset color class

        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            console.log("Sending request to content.js...");
            chrome.tabs.sendMessage(tabs[0].id, { action: "getChatData" }, (response) => {
                if (response && response.chatData && response.chatData.length > 0) {
                    const chatgptResponse = response.chatData[0];
                    console.log("ChatGPT Response Retrieved:", chatgptResponse);

                    chrome.runtime.sendMessage(
                        { action: "calculateHallucination", text: chatgptResponse },
                        (bgResponse) => {
                            console.log("Received response from background.js:", bgResponse);
                            if (bgResponse && typeof bgResponse.score !== "undefined") {
                                scoreElement.innerText = `Hallucination: ${bgResponse.score}%`;
                            } else {
                                scoreElement.innerText = "Error calculating score.";
                            }
                        }
                    );
                } else {
                    console.log("No ChatGPT response found.");
                    scoreElement.innerText = "No ChatGPT data found.";
                }
            });
        });
    });
});
