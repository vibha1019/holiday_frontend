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
    <script type="module">
        import getCredentials from './login.js';
        import { pythonURI, fetchOptions } from './config.js';
        async function loadProfile() {
            try {
                const credentials = await getCredentials();
                if (!credentials) {
                    console.log("No credentials found, redirecting to login.");
                    window.location.href = '/login.html';
                    return;
                }
                // const apiUrl = `${pythonURI}/api/user_profile/${credentials.name}`;
                // const response = await fetch(apiUrl, {
                //     ...fetchOptions,
                //     method: 'GET',
                //     headers: { 'Content-Type': 'application/json' }
                // });
                const data = credentials;
                if (!data.id) {
                    console.log("User ID not found.");
                } else {
                    document.getElementById('link').src = data.pfp || '/images/gifitinatorlogo.png';
                    document.getElementById('username').textContent = data.name || 'Unknown User';
                    document.getElementById('theme-preference').textContent = `Preferred Theme: ${data.theme || 'Light'}`;
                }
            } catch (error) {
                console.error('Error fetching profile data:', error);
            }
        }
        async function deleteProfile() {
            const confirmation = confirm('Are you sure you want to delete this profile?');
            if (!confirmation) return;
            try {
                const response = await fetch(`${pythonURI}/api/user_profile/delete`, {
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
        document.addEventListener('DOMContentLoaded', function() {
            loadProfile();
            document.getElementById('delete-btn').addEventListener('click', deleteProfile);
        });
    </script>
</body>
</html>
