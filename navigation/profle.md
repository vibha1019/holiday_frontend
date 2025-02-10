---
layout: post
title: User Profile
permalink: /profile_page/
author: Spencer Lyons
comments: true
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
    <link rel="stylesheet" href="/socialmedia_frontend/assets/css/profile_style.css">
</head>
<body>
    <div class="profile-header">
        5<img id="link" src="{{ site.baseurl }}/images/logo.png" alt="Profile Picture" />
        <div class="name" id="username">Loading...</div>
        <div class="theme" id="theme-preference">Loading...</div>
        <button id="delete-btn" class="delete-button">Delete Profile</button>
    </div>
    <script>
        const userId = localStorage.getItem("user_id");
        console.log("User ID:", userId);
        const apiUrl = `${pythonURI}/api/1/profile`;
        if (userId) {
            const apiUrl = `${pythonURI}/api/${userID}/profile`; // Adjust for actual user ID
        } else {
            console.log("User ID not found.")
        }
        // Fetch user data and populate the profile
        async function loadProfile() {
            try {
                const response = await fetch(apiUrl, {
                    ...fetchOptions,
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json' }
                });
                const data = await response.json();
                // Populate profile details
                document.getElementById('link').src = data.link || '/images/logo.png';
                document.getElementById('username').textContent = data.name || 'Unknown User';
                document.getElementById('theme-preference').textContent = `Preferred Theme: ${data.theme || 'Light'}`;
            } catch (error) {
                console.error('Error fetching profile data:', error);
            }
        }
        // Load profile on page load
        async function deleteProfile() {
            const confirmation = confirm('Are you sure you want to delete this profile?');
            if (!confirmation) return;
            try {
                const response = await fetch(`${apiUrl}`, {
                    ...fetchOptions,
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ user_id: 1 })
                });
                if (response.ok) {
                    alert('Profile deleted successfully!');
                    document.getElementById('link').src = '/images/logo.png';
                    document.getElementById('username').textContent = 'Unknown User';
                    document.getElementById('theme-preference').textContent = 'Preferred Theme: Light';
                    localStorage.removeItem("user_id");
                } else {
                    const errorData = await response.json();
                    alert(`Error deleting profile: ${errorData.message}`);
                }
            } catch (error) {
                console.error('Error deleting profile:', error);
            }
        }
        // Load profile on page load
        document.addEventListener('DOMContentLoaded', () => {
            loadProfile();
            document.getElementById('delete-btn').addEventListener('click', deleteProfile);
        });
    </script>
</body>
</html>