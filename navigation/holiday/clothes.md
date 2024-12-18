---
layout: post
title: Clothes
permalink: /holiday/clothes/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---
<html lang="en">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clothes Gifts</title>
    <style>
        /* General Page Styles */
        body {
            font-family: Arial, sans-serif;
            background: #111;
            color: #fff;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        header h1 {
            font-size: 2.5em;
            margin: 20px 0;
            background: rgba(0, 0, 0, 0.6);
            padding: 10px 20px;
            border-radius: 10px;
        }
        /* Category Box Styles */
        .category-box {
            display: inline-block;
            width: 200px;
            margin: 20px;
            padding: 20px;
            background: #222;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .category-box:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
        }
        .category-box h2 {
            font-size: 1.5em;
            margin-bottom: 15px;
        }
        button {
            background: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }
        button:hover {
            background: #218838;
        }
        /* Product List */
        .product-list {
            display: none; /* Initially hidden */
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px auto;
            padding: 20px;
            max-width: 800px;
        }
        .product {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .product img {
            max-width: 100%;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .product h3 {
            font-size: 1.2em;
            color: #333;
        }
        .like, .dislike {
            font-size: 1.5em;
            cursor: pointer;
            user-select: none;
            transition: color 0.3s;
        }
        .like { color: black; }
        .like.active { color: red; }
        .dislike { color: black; }
        .dislike.active { color: yellow; }
        .reaction-count {
            font-size: 0.9em;
            color: #333;
        }
        /* Show Active Product List */
        .active {
            display: grid;
        }
    </style>
    <header>
        <h1>👗 Explore Clothes Gifts 🎄</h1>
    </header>
    <!-- Clothes Category -->
    <div class="category-box">
        <h2>Clothes</h2>
        <button onclick="toggleProductList()">Explore Clothes</button>
    </div>
    <!-- Product List -->
    <div id="product-list" class="product-list">
        <div class="product" data-item="Holiday Sweater">
            <img src="{{site.baseurl}}/images/holiday sweater.jpeg" alt="Holiday Sweater">
            <h3>Holiday Sweater</h3>
            <span class="like" onclick="toggleReaction(this, 'like')">❤</span>
            <span class="reaction-count like-count">0</span>
            <span class="dislike" onclick="toggleReaction(this, 'dislike')">👎</span>
            <span class="reaction-count dislike-count">0</span>
        </div>
        <div class="product" data-item="Winter Scarf">
            <img src="{{site.baseurl}}/images/Winter Scarf.jpeg" alt="Winter Scarf">
            <h3>Winter Scarf</h3>
            <span class="like" onclick="toggleReaction(this, 'like')">❤</span>
            <span class="reaction-count like-count">0</span>
            <span class="dislike" onclick="toggleReaction(this, 'dislike')">👎</span>
            <span class="reaction-count dislike-count">0</span>
        </div>
        <div class="product" data-item="Beanie Hat">
            <img src="{{site.baseurl}}/images/Winter Beanie.jpeg" alt="Beanie Hat">
            <h3>Beanie Hat</h3>
            <span class="like" onclick="toggleReaction(this, 'like')">❤</span>
            <span class="reaction-count like-count">0</span>
            <span class="dislike" onclick="toggleReaction(this, 'dislike')">👎</span>
            <span class="reaction-count dislike-count">0</span>
        </div>
    </div>
    <script>
        // Function to toggle product list visibility
        function toggleProductList() {
            const productList = document.getElementById('product-list');
            productList.classList.toggle('active');
        }
        // Like/Dislike functionality
        const likesData = {};
        function toggleReaction(element, reactionType) {
            const productElement = element.closest('.product');
            const productName = productElement.getAttribute('data-item');
            if (!likesData[productName]) {
                likesData[productName] = { likes: 0, dislikes: 0 };
            }
            const isActive = element.classList.contains('active');
            const likeCountElement = productElement.querySelector('.like-count');
            const dislikeCountElement = productElement.querySelector('.dislike-count');
            if (reactionType === 'like') {
                if (isActive) {
                    likesData[productName].likes--;
                    element.classList.remove('active');
                } else {
                    likesData[productName].likes++;
                    element.classList.add('active');
                    productElement.querySelector('.dislike').classList.remove('active');
                    likesData[productName].dislikes = Math.max(0, likesData[productName].dislikes - 1);
                }
            } else if (reactionType === 'dislike') {
                if (isActive) {
                    likesData[productName].dislikes--;
                    element.classList.remove('active');
                } else {
                    likesData[productName].dislikes++;
                    element.classList.add('active');
                    productElement.querySelector('.like').classList.remove('active');
                    likesData[productName].likes = Math.max(0, likesData[productName].likes - 1);
                }
            }
            likeCountElement.textContent = likesData[productName].likes;
            dislikeCountElement.textContent = likesData[productName].dislikes;
            console.log(`Updated reactions for ${productName}:`, likesData[productName]);
        }
    </script>
</html>
        // THIS IS NOW AI CHAT BOX CODE PLS DO NOT MESS WITH IT
    </script>
    <html lang="en">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            position: relative;
            height: 100vh;
            background-color: #f9f9f9;
        }
        #help-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            padding: 10px 20px;
            background-color: #5F9EA0 !important; /* Light blue */
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        #help-button:hover {
            background-color: #63b6e3;
        }
        #chat-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 350px;
            max-height: 500px;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            display: none;
            flex-direction: column;
            overflow: hidden;
        }
        #chat-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            background-color: #333;
            color: white;
            border-bottom: 1px solid #ddd;
        }
        #chat-header h4 {
            margin: 0;
            font-size: 16px;
        }
        #close-chat {
            background: none;
            border: none;
            color: white;
            font-size: 18px;
            cursor: pointer;
        }
        #close-chat:hover {
            color: #ff6666;
        }
        #chat-box {
            flex-grow: 1;
            padding: 10px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
        }
        .message {
            margin: 10px;
            padding: 10px;
            border-radius: 10px;
            max-width: 75%;
            word-wrap: break-word;
            display: inline-block;
        }
        .assistant {
            background-color: #333;
            color: white;
            align-self: flex-start;
            text-align: left;
        }
        .user {
            background-color: #2f4f4f;
            color: white;
            align-self: flex-end;
            text-align: right;
        }
        #input-container {
            display: flex;
            padding: 10px;
            border-top: 1px solid #ddd;
        }
        input[type="text"] {
            flex-grow: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
        }
        button {
            margin-left: 5px;
            padding: 10px;
            background-color: #333;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
        }
        button:hover {
            background-color: #555;
        }
    </style>
    <button id="help-button" onclick="toggleChat()">Need Help?</button>
    <div id="chat-container">
        <div id="chat-header">
            <h4>Giftinator 3000</h4>
            <button id="close-chat" onclick="toggleChat()">×</button>
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
        function toggleChat() {
            chatContainer.style.display = chatContainer.style.display === 'flex' ? 'none' : 'flex';
        }
        async function sendMessage() {
            const message = userInput.value;
            if (!message) return;
            appendMessage('user', message);
            userInput.value = '';
            try {
                const response = await fetch('http://127.0.0.1:8887/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ user_input: message }),
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
            const messageElement = document.createElement('div');
            messageElement.className = `message ${sender}`;
            messageElement.innerText = message;
            chatBox.appendChild(messageElement);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>



