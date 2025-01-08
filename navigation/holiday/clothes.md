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
        .comment-box {
            display: none;
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
    <div id="comment-box" class="comment-box">
    <div class="container">
                <div class="form-container">
                    <h2>Tell Us Why You Liked This Post!</h2>
                    <form id="selectionForm">
                        <label for="group_id">Group:</label>
                        <select id="group_id" name="group_id" required>
                            <option value="">Select a category</option>
                        </select>
                        <label for="channel_id">Channel:</label>
                        <select id="channel_id" name="channel_id" required>
                            <option value="">Select an Age Range</option>
                        </select>
                        <button type="submit">Select</button>
                    </form>
                </div>
            </div>
            <div class="container">
                <div class="form-container">
                    <h2>Add New Post</h2>
                    <form id="postForm">
                        <label for="title">Gift Title:</label>
                        <input type="text" id="title" name="title" required>
                        <label for="comment">Description:</label>
                        <textarea id="comment" name="comment" required></textarea>
                        <button type="submit">Add Post</button>
                    </form>
                </div>
            </div>
        </div>
    <script>
        // Function to toggle product list visibility
        function toggleProductList() {
            const productList = document.getElementById('product-list');
            productList.classList.toggle('active');
            const commentBox = document.getElementById('comment-box');
            commentBox.classList.toggle('active');
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
<script type="module">
    // Import server URI and standard fetch options
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
    /**
     * Fetch groups for dropdown selection
     * User picks from dropdown
     */
    async function fetchGroups() {
        try {
            const response = await fetch(`${pythonURI}/api/groups/filter`, {
                ...fetchOptions,
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ section_name: "Holiday" }) // Adjust the section name if needed
            });
            if (!response.ok) {
                throw new Error('Failed to fetch groups: ' + response.statusText);
            }
            const groups = await response.json();
            const groupSelect = document.getElementById('group_id');
            groups.forEach(group => {
                const option = document.createElement('option');
                option.value = group.name; // Use group name for payload
                option.textContent = group.name;
                groupSelect.appendChild(option);
            });
        } catch (error) {
            console.error('Error fetching groups:', error);
        }
    }
    /**
     * Fetch channels based on selected group
     * User picks from dropdown
     */
    async function fetchChannels(groupName) {
        try {
            const response = await fetch(`${pythonURI}/api/channels/filter`, {
                ...fetchOptions,
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ group_name: groupName }) // Pass selected group name here
            });
            if (!response.ok) {
                throw new Error('Failed to fetch channels: ' + response.statusText);
            }
            const channels = await response.json();
            const channelSelect = document.getElementById('channel_id');
            channelSelect.innerHTML = '<option value="">Select a channel</option>'; // Reset channels
            channels.forEach(channel => {
                const option = document.createElement('option');
                option.value = channel.id;
                option.textContent = channel.name;
                channelSelect.appendChild(option);
            });
        } catch (error) {
            console.error('Error fetching channels:', error);
        }
    }
    /**
     * Handle group selection change
     * Channel Dropdown refresh to match group_id change
     */
    document.getElementById('group_id').addEventListener('change', function() {
        const groupName = this.value;
        if (groupName) {
            fetchChannels(groupName);  // Fetch channels for the selected group
        } else {
            document.getElementById('channel_id').innerHTML = '<option value="">Select a channel</option>'; // Reset channels
        }
    });
    /**
     * Handle form submission for selection
     * Select Button: Computer fetches and displays posts
     */
    document.getElementById('selectionForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const groupId = document.getElementById('group_id').value;
        const channelId = document.getElementById('channel_id').value;
        if (groupId && channelId) {
            fetchData(channelId);
        } else {
            alert('Please select both group and channel.');
        }
    });
    /**
     * Handle form submission for adding a post
     * Add Form Button: Computer handles form submission with request
     */
    document.getElementById('postForm').addEventListener('submit', async function(event) {
        event.preventDefault();
        // Extract data from form
        const title = document.getElementById('title').value;
        const comment = document.getElementById('comment').value;
        const channelId = document.getElementById('channel_id').value;
        // Create API payload
        const postData = {
            title: title,
            comment: comment,
            channel_id: channelId
        };
        // Trap errors
        try {
            // Send POST request to backend, purpose is to write to database
            const response = await fetch(`${pythonURI}/api/post`, {
                ...fetchOptions,
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(postData)
            });
            if (!response.ok) {
                throw new Error('Failed to add post: ' + response.statusText);
            }
            // Successful post
            const result = await response.json();
            alert('Post added successfully!');
            document.getElementById('postForm').reset();
            fetchData(channelId);
        } catch (error) {
            // Present alert on error from backend
            console.error('Error adding post:', error);
            alert('Error adding post: ' + error.message);
        }
    });
    /**
     * Fetch posts based on selected channel
     * Handle response: Fetch and display posts
     */
    async function fetchData(channelId) {
        try {
            const response = await fetch(`${pythonURI}/api/posts/filter`, {
                ...fetchOptions,
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ channel_id: channelId })
            });
            if (!response.ok) {
                throw new Error('Failed to fetch posts: ' + response.statusText);
            }
            // Parse the JSON data
            const postData = await response.json();
            // Extract posts count
            const postCount = postData.length || 0;
            // Update the HTML elements with the data
            document.getElementById('count').innerHTML = `<h2>Count ${postCount}</h2>`;
            // Get the details div
            const detailsDiv = document.getElementById('details');
            detailsDiv.innerHTML = ''; // Clear previous posts
            // Iterate over the postData and create HTML elements for each item
            postData.forEach(postItem => {
                const postElement = document.createElement('div');
                postElement.className = 'post-item';
                postElement.innerHTML = `
                    <h3>${postItem.title}</h3>
                    <p><strong>Channel:</strong> ${postItem.channel_name}</p>
                    <p><strong>User:</strong> ${postItem.user_name}</p>
                    <p>${postItem.comment}</p>
                `;
                detailsDiv.appendChild(postElement);
            });
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
    // Fetch groups when the page loads
    fetchGroups();
</script>

