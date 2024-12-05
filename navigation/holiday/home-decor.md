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
