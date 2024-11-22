---
layout: post
title: Flocker Social Media Site 
search_exclude: true
description: Login and explore our social media hub for everything DNHS 
hide: true
menu: nav/home.html
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giftinator 3000</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .chat-box { max-width: 600px; margin: auto; }
        .messages { margin-bottom: 20px; max-height: 400px; overflow-y: auto; border: 1px solid #ddd; padding: 10px; }
        .message { padding: 10px; margin: 5px 0; border-radius: 5px; }
        .user { background-color: #d1e7fd; text-align: right; }
        .assistant { background-color: #f8d7da; text-align: left; }
        input { width: calc(100% - 20px); padding: 10px; }
    </style>
</head>
<body>
    <div class="chat-box">
        <div class="messages" id="messages"></div>
        <input id="userInput" type="text" placeholder="Type your message here..." onkeypress="handleEnter(event)">
    </div>
    <script>
        async function sendMessage(message) {
            const response = await fetch("http://127.0.0.1:5000/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ user_input: message })
            });
            const data = await response.json();
            return data.response || data.error;
        }
        async function handleEnter(event) {
            if (event.key === "Enter") {
                const userInput = document.getElementById("userInput");
                const userMessage = userInput.value.trim();
                if (userMessage === "") return;
                // Add user's message to the chat
                const messagesDiv = document.getElementById("messages");
                const userDiv = document.createElement("div");
                userDiv.textContent = userMessage;
                userDiv.className = "message user";
                messagesDiv.appendChild(userDiv);
                // Get the bot's response
                const botResponse = await sendMessage(userMessage);
                const botDiv = document.createElement("div");
                botDiv.textContent = botResponse;
                botDiv.className = "message assistant";
                messagesDiv.appendChild(botDiv);
                // Clear the input
                userInput.value = "";
                messagesDiv.scrollTop = messagesDiv.scrollHeight;
            }
        }
    </script>
</body>
</html>
