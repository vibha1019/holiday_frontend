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
    <!-- Age Range Dropdown -->
    <label for="channel-select">Age Range:</label>
    <select id="channel-select" name="channel">
        <option value="1" data-channel-id="5">Teenage Girls (11-15)</option>
        <option value="2" data-channel-id="6">Teenage Boys (11-15)</option>
        <option value="3" data-channel-id="7">Toddlers</option>
        <option value="4" data-channel-id="8">Adults</option>
    </select>
    <p></p>
    <button type="submit">Add Post</button>
  </form>
</div>

<script>
  // Handle item selection
  function selectItem(button, category) {
      // Show the post form
      const formContainer = document.getElementById('post-form');
      formContainer.style.display = 'block';

      // Pre-fill form data based on the selected category
      document.getElementById('title').value = `${category}`;  // Set the item name (category as placeholder)
      document.getElementById('comment').value = `I selected ${button.innerText} because`;  // Pre-fill the comment

      // Get the channel ID from the selected category
      const channelSelect = document.getElementById('channel-select');
      let selectedChannelId = '';

      // Match category to the corresponding channel ID
      if (category === 'Teenage Girls') {
          selectedChannelId = '5';
      } else if (category === 'Teenage Boys') {
          selectedChannelId = '6';
      } else if (category === 'Toddlers') {
          selectedChannelId = '7';
      } else if (category === 'Adults') {
          selectedChannelId = '8';
      }
      // Set the correct value in the dropdown and store the channel ID
      channelSelect.value = selectedChannelId;  // Select the right option in the dropdown
      document.getElementById('postForm').setAttribute('data-channel-id', selectedChannelId); // Save the channel ID to the form
  }
</script>

<script type="module">
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

  // Fetch all arguments for a specific channel
  async function fetchArguments(channelId) {
    try {
      const response = await fetch(`${pythonURI}/api/posts/filter`, {
        ...fetchOptions,
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ channel_id: channelId })
      });

      if (!response.ok) throw new Error('Failed to fetch arguments: ' + response.statusText);

      const argumentsData = await response.json();
      argumentContainer.innerHTML = ""; // Clear existing arguments

      argumentsData.forEach(arg => {
        const card = document.createElement("div");
        card.classList.add("argument-card");

        const text = document.createElement("p");
        text.innerHTML = `<strong>${arg.user_name}:</strong> ${arg.comment}`; // Adjusted to match backend response structure

        card.appendChild(text);
        argumentContainer.appendChild(card);
      });
    } catch (error) {
      console.error('Error fetching arguments:', error);
    }
  }

  // Handle item selection
  function selectItem(button, type, category) {
    const color = type === 'most' ? 'green' : 'red';
    button.style.backgroundColor = color;
    button.style.color = 'white';

    // Create a post when an item is selected
    if (type === 'most') {
      document.getElementById('group-select').value = "Dnero Store";
      document.getElementById('channel-select').value = category;

      const postForm = document.getElementById('post-form');
      postForm.style.display = "block"; // Display post form
    }
  }

  // Handle form submission
  document.getElementById('postForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const title = document.getElementById('title').value;
    const comment = document.getElementById('comment').value;
    const group = document.getElementById('group-select').value;
    const channel = document.getElementById('channel-select').value;
    const channelID = document.getElementById('postForm').getAttribute('data-channel-id'); // Retrieve the saved channel ID
    const postData = {
      title: title,
      comment: comment,
      channel_id: channelID
    }

    try {
      const response = await fetch(`${pythonURI}/api/post`, {
        ...fetchOptions,
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
    transition: color 0.3s;
  }
</style>
