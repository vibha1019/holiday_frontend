---
layout: post
title: home-decor
permalink: /holiday/home-decor/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

<!-- New Post Form (shown by default) -->
<div class="post-form-container" id="post-form">
  <h2>Post Review</h2>
  <form id="postForm">
    <label for="title">Item Name:</label>
    <input type="text" id="title" name="title" required>
    <p></p>
    <label for="comment">Comment:</label>
    <textarea id="comment" name="comment" required>
Quality:
Usefulness:
</textarea>
    <p></p>

    <!-- Star Rating Section -->
    <label for="star-rating">Rating:</label>
    <div id="star-rating" class="star-rating">
      <span class="star" data-value="1">&#9733;</span>
      <span class="star" data-value="2">&#9733;</span>
      <span class="star" data-value="3">&#9733;</span>
      <span class="star" data-value="4">&#9733;</span>
      <span class="star" data-value="5">&#9733;</span>
    </div>
    <input type="hidden" id="star-rating-value" name="star-rating" value="0" />
    <p></p>

    <!-- Age Range Dropdown -->
    <label for="channel-select">Age Range:</label>
    <select id="channel-select" name="channel">
      <option value="1">Teenage Girls (11-15)</option>
      <option value="2">Teenage Boys (11-15)</option>
      <option value="3">Toddlers</option>
      <option value="4">Adults</option>
    </select>
    <p></p>

    <button type="submit">Add Post</button>
  </form>
</div>

<!-- Embedded JavaScript -->
<script>
  // Handle star rating clicks
  const stars = document.querySelectorAll('.star');
  const ratingValueInput = document.getElementById('star-rating-value');

  stars.forEach(star => {
    star.addEventListener('click', function () {
      const rating = this.getAttribute('data-value');
      // Set the value in the hidden input field
      ratingValueInput.value = rating;

      // Update the star colors based on rating
      stars.forEach(star => {
        star.style.color = (star.getAttribute('data-value') <= rating) ? 'gold' : 'gray';
      });
    });
  });

  // Handle form submission
  document.getElementById('postForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const title = document.getElementById('title').value;
    const comment = document.getElementById('comment').value;
    const channel_id = document.getElementById('channel-select').value; // Get the selected value for age range
    const starRating = ratingValueInput.value; // Get the star rating value

    // Prepare the data to be sent to the backend
    const postData = {
      title: title,
      comment: comment,
      channel_id: channel_id,
      star_rating: starRating
    };

    try {
      const response = await fetch(`${pythonURI}/api/post`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
      });

      if (!response.ok) throw new Error('Failed to add post: ' + response.statusText);
      alert("Post added successfully!");

    } catch (error) {
      console.error('Error adding post:', error);
    }
  });
</script>

<style>
  /* General Post Form Styling */
  .post-form-container {
    background-color: #13292b;
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
    color: #ffffff;
  }

  .post-form-container h2 {
    font-size: 1.8em;
    text-align: center;
    color: #ffd700; /* Gold color */
  }

  .post-form-container label {
    display: block;
    margin-bottom: 8px;
    font-size: 1.1em;
  }

  .post-form-container input,
  .post-form-container textarea,
  .post-form-container select {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
    border: 1px solid #ccc;
    background-color: #f4f4f4;
  }

  .post-form-container button {
    background-color: #ffd700;
    color: #13292b;
    padding: 12px 20px;
    font-size: 1.2em;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    border: none;
  }

  .post-form-container button:hover {
    background-color: #ffcc00;
  }

  /* Styling for star rating */
  .star-rating {
    font-size: 2em;
    cursor: pointer;
    color: gray; /* Default color */
  }

  .star {
    padding: 0 5px;
    transition: color 0.3s ease;
  }
  /* THIS IS NOW AI CHAT BOX CODE, DO NOT MESS IT UP PLS */
</style>

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
<script>
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
        .category-box button {
            background: #fff;
            color: #000;
            border: 1px solid #555;
            padding: 10px 15px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .category-box button:hover {
            background: #008080;
            color: #fff;
            border-color: #008080;
        }
        /* Product List */
        .product-list {
            display: none; /* Hidden by default */
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
        .product p {
            font-size: 0.9em;
            color: #555;
        }
        .product:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
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
        <button onclick="toggleClothesProducts()">Explore Clothes</button>
    </div>
    <!-- Clothes Products -->
    <div id="clothes-products" class="product-list">
        <div class="product">
            <img src="{{site.baseurl}}/images/holiday sweater.jpeg" alt="Cozy Holiday Sweater">
            <h3>Cozy Holiday Sweater</h3>
            <p>Warm and festive sweater perfect for the holiday season.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/wool scarf.jpeg" alt="Woolen Scarf">
            <h3>Woolen Scarf</h3>
            <p>Soft and stylish scarf to keep you warm and chic.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/winter gloves.jpeg" alt="Winter Gloves">
            <h3>Winter Gloves</h3>
            <p>Comfortable and warm gloves, ideal for chilly weather.</p>
        </div>
    </div>
    <!-- JavaScript -->
    <script>
        function toggleClothesProducts() {
            const clothesProducts = document.getElementById("clothes-products");
            if (clothesProducts.style.display === "none" || clothesProducts.style.display === "") {
                clothesProducts.style.display = "grid";
            } else {
                clothesProducts.style.display = "none";
            }
        }
    </script>
</html>

<html>
    <style>
        /* Styling for the button */
        button {
            padding: 10px 20px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        /* Styling for the post area */
        #postArea {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #ccc;
            background-color: #f8f9fa;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            font-family: monospace;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
    <button onclick="addPost()">Add Post</button>
    <div id="postArea">
        <p id="placeholder"></p>
    </div>
    <script>
        function addPost() {
            // Get the post area and replace its content with a code input area
            const postArea = document.getElementById('postArea');
            postArea.innerHTML = `
                <textarea placeholder="Write your code here..."></textarea>
                <button onclick="savePost()">Save Post</button>
            `;
        }
        function savePost() {
            const textarea = document.querySelector('#postArea textarea');
            const codeContent = textarea.value;
            // Replace the textarea with the submitted code content
            const postArea = document.getElementById('postArea');
            postArea.innerHTML = `
                <pre style="background-color: #f1f1f1; padding: 10px; border: 1px solid #ccc; border-radius: 5px;">${codeContent}</pre>
            `;
        }
    // Add styles dynamically
    const style = document.createElement('style');
    style.innerHTML = `
        .product-list {
            display: grid;
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
        .like, .dislike {
            font-size: 1.5em;
            cursor: pointer;
            transition: color 0.3s;
            user-select: none;
        }
        .like {
            color: black;
        }
        .like.active {
            color: red;
        }
        .dislike {
            color: black;
        }
        .dislike.active {
            color: yellow;
        }
        .reaction-count {
            font-size: 0.9em;
            color: #333;
        }
    `;
    document.head.appendChild(style);
    // Add products dynamically
    document.body.innerHTML = `
        <div id="home-decor-products" class="product-list">
            <div class="product" data-item="Holiday Candles">
                <img src="{{site.baseurl}}/images/holiday candles.jpeg" alt="Holiday Candles">
                <h3>Holiday Candles</h3>
                <span class="like" onclick="toggleReaction(this, 'like')">❤</span>
                <span class="reaction-count like-count">0</span>
                <span class="dislike" onclick="toggleReaction(this, 'dislike')">👎</span>
                <span class="reaction-count dislike-count">0</span>
            </div>
            <div class="product" data-item="Festive Wreath">
                <img src="{{site.baseurl}}/images/festive wreath.jpeg" alt="Festive Wreath">
                <h3>Festive Wreath</h3>
                <span class="like" onclick="toggleReaction(this, 'like')">❤</span>
                <span class="reaction-count like-count">0</span>
                <span class="dislike" onclick="toggleReaction(this, 'dislike')">👎</span>
                <span class="reaction-count dislike-count">0</span>
            </div>
            <div class="product" data-item="Decorative Ornaments">
                <img src="{{site.baseurl}}/images/decorative ornaments.jpeg" alt="Decorative Ornaments">
                <h3>Decorative Ornaments</h3>
                <span class="like" onclick="toggleReaction(this, 'like')">❤</span>
                <span class="reaction-count like-count">0</span>
                <span class="dislike" onclick="toggleReaction(this, 'dislike')">👎</span>
                <span class="reaction-count dislike-count">0</span>
            </div>
        </div>
    `;
    // Backend simulation and reaction functionality
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
        // Simulate sending data to the backend
        console.log('Updated reactions for', productName, likesData[productName]);
    }
</script>
</html>
