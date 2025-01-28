---
layout: post
title: User Profile
permalink: /profile_page/
author: Spencer Lyons
comments: true
---

<!-- Link to the external CSS file -->
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/profile_style.css">
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
    <link rel="stylesheet" href="/socialmedia_frontend/assets/css/profile_style.css">
</head>
<body>
    <div class="profile-header">
        <img src="/images/logo.png" alt="Profile Picture" class="profile-picture" />
        <div class="username" id="username">Loading...</div>
        <div class="theme-preference" id="theme-preference">Loading...</div>
    </div>
    <script>
        // API Endpoint
        const apiUrl = 'http://127.0.0.1:8887/api/user_profile'; // Replace with your API URL
        // Fetch user data and populate the profile
        async function loadProfile() {
            try {
                const response = await fetch(`${apiUrl}`);
                const data = await response.json();
                // Populate profile details
                document.getElementById('link').src = data.link || '/images/logo.png';
                document.getElementById('name').textContent = data.name || 'Unknown User';
                document.getElementById('theme').textContent = `Preferred Theme: ${data.theme || 'Light'}`;
            } catch (error) {
                console.error('Error fetching profile data:', error);
            }
        }
        // Load profile on page load
        document.addEventListener('DOMContentLoaded', loadProfile);
    </script>
</body>
</html>