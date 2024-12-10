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




