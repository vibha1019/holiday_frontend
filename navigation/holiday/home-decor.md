---
layout: post
title: home-decor
permalink: /holiday/home-decor/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

<div class="container">
  <div class="category-box">
    <div class="category-row" onclick="toggleItems('holiday-items')">
      <h3>Home Decor</h3>
      <div id="holiday-items" class="item-list-container" style="display: none;">
        <p>Please select the category that applies:</p>
        <div class="item-list">
          <button onclick="selectItem(this, 'Holiday')" data-channel-id="5">Teenage Girl (11-15)</button>
          <button onclick="selectItem(this, 'Holiday')" data-channel-id="6">Teenage Boy (11-15)</button>
          <button onclick="selectItem(this, 'Holiday')" data-channel-id="7">Toddler</button>
          <button onclick="selectItem(this, 'Holiday')" data-channel-id="8">Adult</button>
        </div>
      </div>
      <div id="holiday-posts" class="category-posts"></div>
    </div>
  </div>

  <!-- New Post Form -->
  <div class="post-form-container" id="post-form" style="display: none;">
    <h2>Create a Post</h2>
    <form id="postForm">
      <label for="title">Title:</label>
      <input type="text" id="title" name="title" required>
      <p></p>
      <label for="comment">Comment:</label>
      <textarea id="comment" name="comment" required></textarea>
      <!-- Dropdowns for Group and Channel Selection -->
      <div class="dropdown-container">
        <label for="group-select">Group:</label>
        <select id="group-select" name="group">
          <option value="Holiday">Holiday</option>
        </select>
        <label for="channel-select">Channel:</label>
        <select id="channel-select" name="channel">
          <option value="Teenage Girl (11-15)">Teenage Girl (11-15)</option>
          <option value="Teenage Boy (11-15)">Teenage Boy (11-15)</option>
          <option value="Toddler">Toddler</option>
          <option value="Adult">Adult</option>
        </select>
      </div>
      <button type="submit">Add Post</button>
    </form>
  </div>
</div>

<script>
  // Toggle visibility of item lists
  function toggleItems(id) {
    const selectedItem = document.getElementById(id);
    const currentState = selectedItem.style.display;
    selectedItem.style.display = currentState === 'none' ? 'block' : 'none';
  }

  // Handle item selection
  function selectItem(button, group) {
    button.style.backgroundColor = 'green';
    button.style.color = 'white';

    // Show the post form
    const formContainer = document.getElementById('post-form');
    formContainer.style.display = 'block';

    // Pre-fill form data based on the selected category
    document.getElementById('title').value = "";
    document.getElementById('comment').value = "";
    document.getElementById('group-select').value = group;

    // Set the category for the dropdown
    const categoryName = button.textContent;
    document.getElementById('channel-select').value = categoryName;

    // Save the channel ID to the form
    const channelID = button.getAttribute('data-channel-id');
    document.getElementById('postForm').setAttribute('data-channel-id', channelID);
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
      channel_id: channelID,
    };

    try {
      const response = await fetch(`${pythonURI}/api/post`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData),
      });

      if (!response.ok) throw new Error('Failed to add post: ' + response.statusText);
      alert("Post added successfully!");
    } catch (error) {
      console.error('Error adding post:', error);
    }
  });
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
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 1200px;
    padding: 20px;
    box-sizing: border-box;
  }

  .category-box {
    width: 100%;
    max-width: 800px;
    background-color: #000000;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin: 10px 0;
  }

  .category-box h3 {
    text-align: center;
    background-color: #007BFF;
    color: white;
    padding: 10px;
  }

  .item-list button {
    margin: 5px;
    padding: 10px;
    background-color: #f1f1f1;
    border: 1px solid #007BFF;
    cursor: pointer;
  }

  .post-form-container {
    background-color: #020b40;
    border: 2px solid #007BFF;
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
  }

  body {
    background-image: url("{{ site.baseurl }}/images/dnerostore/bkgd.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }
</style>
