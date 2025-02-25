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
  <style>
    /* Header styling matching your index page */
    .holiday-header {
      width: 100%;
      text-align: center;
      padding: 20px 0;
      background: rgba(0, 0, 0, 0.6);
      color: white;
    }
    .holiday-header h1 {
      font-size: 2.5em;
      margin: 20px 0;
      border-radius: 10px;
    }
    /* Container for profile content for spacing */
    .profile-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 15px;
      margin: 20px;
    }
    /* Style adjustments for theme buttons */
    .theme-buttons button {
      margin: 5px;
      padding: 10px 15px;
      font-size: 14px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <header class="holiday-header">
    <h1>User Profile</h1>
  </header>
  <section class="profile-container">
    <img id="link" src="{{ site.baseurl }}/images/gifitinatorlogo.png" width="50" height="50" alt="Profile Picture" /> 
    <div class="name" id="username">default_user</div>
    <div class="theme" id="theme-preference">Preferred Theme: Dark</div>
    <!-- Theme buttons -->
    <div class="theme-buttons">
      <button id="light-mode-btn">Light Mode</button>
      <button id="dark-mode-btn">Dark Mode</button>
    </div>
    <button id="delete-btn" class="delete-button">Delete Profile</button>
  </section>
  <script type="module">
    import { getCredentials } from '{{ site.baseurl }}/assets/js/api/login.js';
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
    // Function to update colors on the page based on theme.
    function applyThemeColors(theme) {
      if (theme.toLowerCase() === 'light') {
        document.body.style.setProperty('background-color', 'white', 'important');
        document.body.style.setProperty('color', 'black', 'important');
        const header = document.querySelector('.holiday-header');
        if (header) {
          header.style.setProperty('color', 'black', 'important');
        }
      } else {
        document.body.style.setProperty('background-color', 'black', 'important');
        document.body.style.setProperty('color', 'white', 'important');
        const header = document.querySelector('.holiday-header');
        if (header) {
          header.style.setProperty('color', 'white', 'important');
        }
      }
    }
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
        const theme = credentials.theme || 'Dark';
        themeElement.textContent = `Preferred Theme: ${theme}`;
        // Apply the background and text colors based on theme
        applyThemeColors(theme);
        // Determine how to load the profile picture
        if (credentials.pfp) {
          if (credentials.pfp.startsWith("data:image")) {
            profilePic.src = credentials.pfp;
          } else if (credentials.pfp.startsWith("/") || credentials.pfp.includes("http")) {
            profilePic.src = credentials.pfp;
          } else {
            profilePic.src = `/user-images/${credentials.pfp}`; // Adjust path as needed
          }
        } else {
          profilePic.src = '/images/gifitinatorlogo.png'; // Fallback
        }
        profilePic.onerror = function () {
          this.src = '/images/gifitinatorlogo.png';
        };
      } catch (error) {
        console.error('Error fetching profile data:', error);
      }
    }
    // Function to update the theme both in the UI and on the server
    async function updateTheme(theme) {
      const themeElement = document.getElementById('theme-preference');
      themeElement.textContent = `Preferred Theme: ${theme}`;
      // Update background and text colors with !important
      applyThemeColors(theme);
      // Persist the theme change to the server (ensure your API supports this)
      try {
        const response = await fetch(`${pythonURI}/api/user_profile/update`, {
          ...fetchOptions,
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ user_id: 1, theme: theme })
        });
        if (!response.ok) {
          const errorData = await response.json();
          alert(`Error updating theme: ${errorData.message}`);
        }
      } catch (error) {
        console.error('Error updating theme:', error);
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
          applyThemeColors('Light');
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
      // Add event listeners for theme buttons to update theme and background/text colors
      document.getElementById('light-mode-btn').addEventListener('click', function() {
        updateTheme('Light');
      });
      document.getElementById('dark-mode-btn').addEventListener('click', function() {
        updateTheme('Dark');
      });
    });
  </script>
</body>
</html>
