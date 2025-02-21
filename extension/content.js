console.log("ChatGPT Hallucination Checker content script loaded");

// Function to extract the latest ChatGPT response
function extractChatData() {
    let messages = document.querySelectorAll('[data-message-author-role="assistant"] .markdown p'); // Get all ChatGPT responses
    
    if (messages.length > 0) {
        let latestMessage = messages[messages.length - 1].innerText.trim(); // Get last response
        console.log("Extracted ChatGPT response:", latestMessage);
        return latestMessage;
    }
    
    console.warn("No ChatGPT response found.");
    return null;
}

// Listen for messages from popup.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getChatData") {
        let responseText = extractChatData();
        
        if (responseText) {
            sendResponse({ chatData: [responseText] });
        } else {
            sendResponse({ chatData: [] });
        }
    }
});
