---
layout: post
title: Holiday
permalink: /holiday
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

<div class="holiday-page">
    <header class="holiday-header">
        <h1>🎁 Holidays Gift List 🎄</h1>
    </header>
    <div class="categories-grid">
        <div class="category-box" id="home-decor">
            <h2>Home Decor</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/home-decor/'">Explore Home Decor</button>
        </div>
        <div class="category-box" id="food">
            <h2>Food</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/food/'">Explore Food</button>
        </div>
        <div class="category-box" id="clothes">
            <h2>Clothes</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/clothes/'">Explore Clothes</button>
        </div>
        <div class="category-box" id="scented">
            <h2>Scented Gifts</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/scented/'">Explore Scented Gifts</button>
        </div>
        <div class="category-box" id="electronics">
            <h2>Electronics</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/electronics/'">Explore Electronics</button>
        </div>
        <div class="category-box" id="toys">
            <h2>Toys</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/toys/'">Explore Toys</button>
        </div>
    </div>
</div>

<style>
/* Reset margin and padding for the whole page */
html, body {
    margin: 0;
    padding: 0;
    width: 100%;
}

/* Apply the background image to the container */
.holiday-page {
    background-image: url('{{ site.baseurl }}/images/greenbackground.png');
    background-size: cover; /* Keeps the image covering the container */
    background-position: center;
    background-attachment: fixed; /* Keeps background fixed on scroll */
    min-height: 100vh;
    width: 68vw; /* Reduces the width of the container to 80% of the viewport */
    margin: 0 auto; /* Centers the container */
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #ffffff;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
    position: relative; /* Ensures it's a stacking context */
}

/* Header Styles */
.holiday-header h1 {
    font-size: 2.5em;
    margin-bottom: 30px;
    text-align: center;
    background: rgba(0, 0, 0, 0.6);
    padding: 10px 20px;
    border-radius: 10px;
}

/* Grid Layout */
.categories-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    width: 90%;
    max-width: 1200px;
}

/* Category Box Styles */
.category-box {
    background: rgba(0, 0, 0, 0.6);
    border: 2px solid rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    text-align: center;
    padding: 20px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    z-index: 2; /* Ensures boxes appear above the background */
}

.category-box h2 {
    margin-bottom: 15px;
    font-size: 1.5em;
}

.category-box button {
    background: #ffffff;
    color: #008080;
    border: none;
    padding: 10px 15px;
    font-size: 1em;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s ease, color 0.2s ease;
}

.category-box button:hover {
    background: #008080;
    color: #ffffff;
}

/* Hover Effect */
.category-box:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
}

/* Responsive Design */
@media (max-width: 768px) {
    .categories-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    .holiday-header h1 {
        font-size: 2em;
    }
}

@media (max-width: 480px) {
    .categories-grid {
        grid-template-columns: 1fr;
    }
    .category-box h2 {
        font-size: 1.2em;
    }
}

/* Snowflake Styling */
.snowflake {
    position: absolute;
    color: white;
    font-size: 1em;
    user-select: none;
    pointer-events: none;
    z-index: 1;
    animation: fall linear infinite;
}

@keyframes fall {
    0% {
        transform: translateY(-10px);
    }
    100% {
        transform: translateY(100vh);
    }
}

/* Animation for snowflakes */
.snowflake:nth-child(odd) {
    animation-duration: 10s;
}

.snowflake:nth-child(even) {
    animation-duration: 15s;
}

/* Adjusting the snowflakes' size and timing */
.snowflake:nth-child(1) {
    font-size: 1.5em;
    animation-duration: 10s;
}

.snowflake:nth-child(2) {
    font-size: 1.3em;
    animation-duration: 12s;
}

.snowflake:nth-child(3) {
    font-size: 1.7em;
    animation-duration: 14s;
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function() {
    // Snowflakes creation
    for (let i = 0; i < 100; i++) {
        let snowflake = document.createElement("div");
        snowflake.classList.add("snowflake");
        snowflake.style.left = `${Math.random() * 100}%`;
        snowflake.style.animationDuration = `${Math.random() * 10 + 5}s`; // random fall time
        snowflake.style.animationDelay = `${Math.random() * 5}s`; // random start time
        snowflake.innerHTML = "❆";
        document.querySelector(".holiday-page").appendChild(snowflake);
    }
});
</script>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giftinator 3000</title>
    <style>
        #chat-container {
            display: none;
            flex-direction: column;
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 300px;
            height: 400px;
            border: 1px solid #ccc;
            border-radius: 8px;
            background: #f9f9f9;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        #chat-header {
            background: #4caf50;
            color: white;
            padding: 10px;
            font-size: 18px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
        #chat-box {
            flex: 1;
            padding: 10px;
            overflow-y: auto;
        }
        #input-container {
            display: flex;
            padding: 10px;
            border-top: 1px solid #ddd;
        }
        #input-container input {
            flex: 1;
            padding: 5px;
            margin-right: 5px;
        }
        #input-container button {
            padding: 5px 10px;
            background: #4caf50;
            color: white;
            border: none;
            cursor: pointer;
        }
        #help-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #4caf50;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <button id="help-button" onclick="toggleChat()">Need Help?</button>
    <div id="chat-container">
        <div id="chat-header">
            <span>Giftinator 3000</span>
            <button onclick="toggleChat()" style="float: right; background: none; border: none; color: white;">×</button>
        </div>
        <div id="chat-box"></div>
        <div id="input-container">
            <input type="text" id="user-input" placeholder="Type your message..." />
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <script>
        const chatBox = document.getElementById('chat-box');
        const userInput = document.getElementById('user-input');
        const chatContainer = document.getElementById('chat-container');
        const userId = 1; // Replace with actual user ID logic
        function toggleChat() {
            chatContainer.style.display = chatContainer.style.display === 'flex' ? 'none' : 'flex';
        }
        async function sendMessage() {
            const message = userInput.value.trim();
            const yesNo = confirm("Is this related to gift suggestions?") ? 1 : 0;
            if (!message) return;
            appendMessage('user', message);
            userInput.value = '';
            try {
                const response = await fetch('/api/gift/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        user_input: message,
                        user_id: userId,
                        yesNo: yesNo,
                    }),
                });
                const data = await response.json();
                if (response.ok) {
                    appendMessage('assistant', data.response);
                } else {
                    appendMessage('assistant', `Error: ${data.error}`);
                }
            } catch (error) {
                appendMessage('assistant', `Error: ${error.message}`);
            }
        }
        function appendMessage(sender, message) {
            const messageDiv = document.createElement('div');
            messageDiv.textContent = `${sender === 'user' ? 'You' : 'Giftinator'}: ${message}`;
            chatBox.appendChild(messageDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
