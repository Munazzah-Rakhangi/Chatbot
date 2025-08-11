// script.js (replace entire file)

function toggleChat() {
    const chat = document.getElementById("chat-container");
    const icon = document.getElementById("chat-icon");
    const opened = chat.classList.toggle("visible");

    if (opened) {
        // Wait until the animation ends before hiding the icon
        setTimeout(() => {
            icon.style.display = "none";
            document.getElementById("user-input")?.focus();
        }, 220); // match your animation duration
    } else {
        icon.style.display = "flex";
    }
}

function appendMessage(senderClass, messageHtml) {
    const chatBox = document.getElementById("chat-box");
    const wrapper = document.createElement("div");
    wrapper.className = senderClass;
    wrapper.innerHTML = messageHtml;
    chatBox.appendChild(wrapper);
    // keep newest visible
    chatBox.scrollTop = chatBox.scrollHeight + 200;
}

/* escape user text so that typed content is shown as text (server responses are HTML) */
function escapeHtml(str) {
    const p = document.createElement('p');
    p.appendChild(document.createTextNode(str));
    return p.innerHTML;
}

function sendMessage() {
    const userInputEl = document.getElementById("user-input");
    const userInput = userInputEl.value.trim();
    if (userInput === "") return;

    // Show user message (escaped)
    appendMessage("user-message", `<div class="message-content">${escapeHtml(userInput)}</div>`);

    // Typing indicator (three dots)
    const typingId = Date.now();
    appendMessage("bot-message", `<span class="typing-dot" id="typing-${typingId}"><span></span><span></span><span></span></span>`);

    // Send to backend
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Remove typing indicator
        const typingEl = document.getElementById(`typing-${typingId}`);
        if (typingEl && typingEl.parentElement) typingEl.parentElement.remove();

        // Server replies are HTML (safe-ish because server intends to produce HTML)
        appendMessage("bot-message", data.reply);
    })
    .catch(err => {
        const typingEl = document.getElementById(`typing-${typingId}`);
        if (typingEl && typingEl.parentElement) typingEl.parentElement.remove();
        appendMessage("bot-message", "⚠️ Error connecting to server.");
        console.error(err);
    });

    // Clear input
    userInputEl.value = "";
}

// Allow sending message by pressing Enter
document.addEventListener("DOMContentLoaded", function () {
    const userInputEl = document.getElementById("user-input");
    userInputEl.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });
});
