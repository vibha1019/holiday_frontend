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
    <link rel="stylesheet" href="/holiday_frontend/assets/css/profile_style.css">
</head>
<body>
    <div class="profile-header">
        <img id="link" src="{{ site.baseurl }}/images/gifitinatorlogo.png" width="50" height="50" alt="Profile Picture" /> 
        <div class="name" id="username">default_user</div>
        <div class="theme" id="theme-preference">dark</div>
        <button id="delete-btn" class="delete-button">Delete Profile</button>
    </div>
    <script>
        // Fetch user data and populate the profile
        async function loadProfile(username) {
            const apiUrl = `${pythonURI}/api/user_profile/${username}`;
            try {
                const response = await fetch(apiUrl, {
                    ...fetchOptions,
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json' }
                });
                const data = await response.json();
                if (!data.user_id) {
                    console.log("User ID not found.")
                } else {
                    // Populate profile details
                    document.getElementById('link').src = data.link || '/images/gifitinatorlogo.png';
                    document.getElementById('username').textContent = data.name || 'Unknown User';
                    document.getElementById('theme-preference').textContent = `Preferred Theme: ${data.theme || 'Light'}`;
                }
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
                    document.getElementById('link').src = '/images/gifitinatorlogo.png';
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
        document.addEventListener('DOMContentLoaded', async function() {
            const isAuthenticated = localStorage.getItem('authenticated') === 'true';
            const baseurl = document.querySelector('.trigger').getAttribute('data-baseurl');
            const loginArea = document.getElementById('profile-header');
            if (isAuthenticated) {
                const username = await getCredentials(baseurl);
                loadProfile(username); // Fetch user ID based on username
                document.getElementById('delete-btn').addEventListener('click', deleteProfile);
                loginArea.innerHTML = `<a href="${baseurl}/profile/${username}">${username}</a>`;
            } else {
                loginArea.innerHTML = `<a href="${baseurl}/login">Login</a>`;
                localStorage.setItem('authenticated', 'false');
            }
        });
    </script>
</body>
</html>