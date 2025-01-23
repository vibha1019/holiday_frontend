---
layout: post
title: User Profile
permalink: /profile_page/
author: Spencer Lyons
comments: true
---

<!-- Link to the external CSS file -->
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/profile_style.css">
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to the CSS file -->
</head>
<body>
    <div class="profile-header">
        <img src="" alt="Profile Picture" class="profile-picture" id="profile-picture" />
        <div class="username" id="username">Loading...</div>
        <div class="theme-preference" id="theme-preference">Loading...</div>
    </div>
    <div class="posts-container">
        <div class="posts-title">My Posts</div>
        <div class="posts-list" id="posts-list">
            <!-- Posts will be loaded here dynamically -->
        </div>
    </div>
    <script>
        // API Endpoint
        const apiUrl = 'https://127.0.0.1/profile'; // Replace with your API URL
        // Fetch user data and populate the profile
        async function loadProfile() {
            try {
                const response = await fetch(`${apiUrl}`);
                const data = await response.json();
                // Populate profile details
                document.getElementById('profile-picture').src = data.profilePicture || 'default-pic.jpg';
                document.getElementById('username').textContent = data.username || 'Unknown User';
                document.getElementById('theme-preference').textContent = `Preferred Theme: ${data.theme || 'Light'}`;
                // Populate posts
                const postsList = document.getElementById('posts-list');
                postsList.innerHTML = ''; // Clear any existing content
                data.posts.forEach(post => {
                    const postItem = document.createElement('div');
                    postItem.className = 'post-item';
                    postItem.innerHTML = `
                        <div class="post-title">${post.title}</div>
                        <div class="post-date">${new Date(post.date).toLocaleDateString()}</div>
                    `;
                    postsList.appendChild(postItem);
                });
            } catch (error) {
                console.error('Error fetching profile data:', error);
            }
        }
        // Load profile on page load
        document.addEventListener('DOMContentLoaded', loadProfile);
    </script>
</body>
</html>

