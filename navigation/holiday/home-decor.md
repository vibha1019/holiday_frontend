---
layout: post
title: home-decor
permalink: /holiday/home-decor/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

<!-- Button to trigger the form display -->
<button id="showFormButton">Create a Post</button>

<!-- New Post Form (hidden initially) -->
<div class="post-form-container" id="post-form" style="display: none;">
  <h2>Create a Post</h2>
  <form id="postForm">
    <label for="title">Item Name:</label>
    <input type="text" id="title" name="title" required>
    <p></p>
    <label for="comment">Comment:</label>
    <textarea id="comment" name="comment" required></textarea>
    <p></p>
    <!-- Dropdown for Age Range (acting as channel_id) -->
    <label for="channel-select">Age Range:</label>
    <select id="channel-select" name="channel">
      <option value="1">Teenage Girls (11-15)</option>
      <option value="2">Teenage Boys (11-15)</option>
      <option value="3">Toddlers</option>
      <option value="4">Adults</option>
    </select>
    <button type="submit">Add Post</button>
  </form>
</div>

<!-- Embedded JavaScript -->
<script>
  document.getElementById('showFormButton').addEventListener('click', function () {
    const formContainer = document.getElementById('post-form');
    formContainer.style.display = 'block';  // Show the form
  });

  // Handle form submission
  document.getElementById('postForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const title = document.getElementById('title').value;
    const comment = document.getElementById('comment').value;
    const channel_id = document.getElementById('channel-select').value; // Use the selected value as channel_id

    // Prepare the data to be sent to the backend
    const postData = {
      title: title,
      comment: comment,
      channel_id: channel_id
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

  /* Button to trigger the form */
  #showFormButton {
    background-color: #008080;
    color: white;
    padding: 10px 20px;
    font-size: 1.1em;
    border-radius: 5px;
    cursor: pointer;
    border: none;
  }

  #showFormButton:hover {
    background-color: #006f6f;
  }
</style>
