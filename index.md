---
layout: post
title: Holiday Giftinator
search_exclude: true
description: Login and explore our social media hub for everything DNHS 
hide: true
menu: nav/home.html
---


<html lang="en">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Chat</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        #chat-box {
            width: 90%;
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            background-color: #ffffff;
            overflow-y: auto;
            max-height: 400px;
            display: flex;
            flex-direction: column;
        }
        .message {
            margin: 15px 0;
            padding: 10px;
            border-radius: 10px;
            max-width: 80%;
            word-wrap: break-word;
            display: inline-block;
            clear: both;
        }
        .user {
            background-color: #2f4f4f; /* Darker background */
            color: white;
            align-self: flex-end; /* Align to the right */
            text-align: right;
        }
        .assistant {
            background-color: #333; /* Darker background */
            color: white;
            align-self: flex-start; /* Align to the left */
            text-align: left;
        }
        input[type="text"] {
            width: 80%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        button {
            padding: 10px;
            width: 15%;
            background-color: #333;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #555;
        }
    </style>
    <div id="chat-box"></div>
    <div style="width: 90%; max-width: 600px; display: flex; justify-content: space-between;">
        <input type="text" id="user-input" placeholder="Type your message..." />
        <button onclick="sendMessage()">Send</button>
    </div>
    <script>
        const chatBox = document.getElementById('chat-box');
        const userInput = document.getElementById('user-input');
        async function sendMessage() {
            const message = userInput.value;
            if (!message) return;
            // Append user message to the chat box
            appendMessage('user', message);
            userInput.value = '';
            try {
                // Send user input to the Flask backend
                const response = await fetch('http://127.0.0.1:8887/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ user_input: message }),
                });
                const data = await response.json();
                if (response.ok) {
                    // Append assistant's response to the chat box
                    appendMessage('assistant', data.response);
                } else {
                    appendMessage('assistant', `Error: ${data.error}`);
                }
            } catch (error) {
                appendMessage('assistant', `Error: ${error.message}`);
            }
        }
        function appendMessage(sender, message) {
            const messageElement = document.createElement('div');
            messageElement.className = `message ${sender}`;
            messageElement.innerText = message;
            chatBox.appendChild(messageElement);
            chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
        }
    </script>

<div style="text-align: center; padding: 20px; background-color: #e6f7ff; border-radius: 10px;">
  <h1 style="color: #1a73e8; font-family: 'Brush Script MT', cursive;">🎁 Holiday Giftinator ❄️</h1>
  <p style="font-size: 18px; color: #2c3e50; margin: 10px 0;">
    Celebrate the holidays with our amazing gift recommendations! 
    Explore, recommend, and find the perfect gifts for everyone on your list. 
  </p>
  <img src="{{ site.baseurl }}/images/giftimage.jpeg" alt="Gift Image" style="width: 80%; height: auto; border: 5px solid #1a73e8; border-radius: 10px; margin: 20px auto;">
  
  <a href="https://vibha1019.github.io/socialmedia_frontend/holiday" 
     style="display: inline-block; padding: 15px 30px; font-size: 18px; background-color: #1a73e8; color: white; text-decoration: none; border-radius: 5px; margin-top: 20px;">
    ❄️ Shop Here!
  </a>
</div>


