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
        import { getCredentials } from '{{ site.baseurl }}/assets/js/api/login.js';
        import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
        async function loadProfile() {
            try {
                const credentials = await getCredentials();
                console.log("Retrieved Credentials:", credentials);
                if (!credentials || !credentials.name) {
                    console.log("No credentials found, redirecting to login.");
                    window.location.href = '{{ site.baseurl }}/login.html';
                    return;
                }
                // Get elements
                const profilePic = document.getElementById('link');
                const usernameElement = document.getElementById('username');
                const themeElement = document.getElementById('theme-preference');
                if (!profilePic || !usernameElement || !themeElement) {
                    console.error("Profile elements not found in DOM.");
                    return;
                }
                // Apply profile data
                usernameElement.textContent = credentials.name || 'Unknown User';
                themeElement.textContent = `Preferred Theme: ${credentials.theme || 'Dark'}`;
                // Determine how to load the profile picture
                if (credentials.pfp) {
                    if (credentials.pfp.startsWith("data:image")) {
                        // Already a Base64 image
                        profilePic.src = credentials.pfp;
                    } else if (credentials.pfp.startsWith("/") || credentials.pfp.includes("http")) {
                        // Direct URL or relative path
                        profilePic.src = credentials.pfp;
                    } else {
                        // Assume it's a filename that needs to be fetched from the server
                        profilePic.src = `/user-images/${credentials.pfp}`; // Adjust path as needed
                    }
                } else {
                    profilePic.src = '/images/gifitinatorlogo.png'; // Fallback
                }
                // Fallback if the image fails to load
                profilePic.onerror = function () {
                    this.src = '/images/gifitinatorlogo.png';
                };
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
