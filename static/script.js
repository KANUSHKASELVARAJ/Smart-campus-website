// Append message to chat box
function appendMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");
    const msgDiv = document.createElement("div");
    msgDiv.className = "message " + sender;
    msgDiv.innerHTML = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Append image (graph / pie chart)
function appendImage(imgSrc) {
    const chatBox = document.getElementById("chat-box");
    const img = document.createElement("img");
    img.src = imgSrc;
    img.style.maxWidth = "400px";
    img.style.display = "block";
    img.style.marginTop = "10px";
    chatBox.appendChild(img);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send user message to Flask
function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;

    appendMessage("user", `<strong>You:</strong> ${message}`);
    input.value = "";

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        // Text response
        if (data.response) {
            appendMessage("bot", `<strong>Bot:</strong> ${data.response}`);
        }

        // Line graph
        if (data.graph) {
            appendImage(data.graph);
        }

        // Pie chart
        if (data.pie) {
            appendImage(data.pie);
        }
    })
    .catch(err => {
        appendMessage("bot", "⚠️ Error: Could not reach server");
        console.error(err);
    });
}

// Enter key support
document.getElementById("user-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

// Send button
document.getElementById("send-btn").addEventListener("click", sendMessage);
