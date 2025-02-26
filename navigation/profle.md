---
layout: post
title: User Profile
permalink: /profile_page/
author: Spencer Lyons
comments: true
---

<link rel="stylesheet" href="/holiday_frontend/assets/css/profile_style.css">
<!-- Profile Header -->
<!-- <div class="profile-header">
  <h1>User Profile</h1>
</div> -->

<!-- Profile Content -->
<link rel="stylesheet" href="/holiday_frontend/assets/css/profile_style.css">
<!-- Profile Content -->
<div class="profile-container">
  <!-- Profile Picture -->
  <div class="profile-picture">
    <img id="link" src="{{ site.baseurl }}/images/profile.jpg" width="100" height="100" alt="Profile Picture" />
  </div>
  
  <!-- Username -->
  <div class="name" id="username">default_user</div>

  <!-- Theme Preference -->
  <div class="theme" id="theme-preference">Preferred Theme: Dark</div>

  <!-- Theme buttons (with symbols) -->
  <div class="theme-buttons">
    <button id="light-mode-btn" title="Light Mode"><span class="symbol">&#x2600;</span></button> <!-- Sun symbol for Light Mode -->
    <button id="dark-mode-btn" title="Dark Mode"><span class="symbol">&#x263D;</span></button> <!-- Moon symbol for Dark Mode -->
  </div>

  <!-- Delete Profile Button -->
  <div class="delete-container">
    <button id="delete-btn" class="delete-button" title="Delete Profile"><span class="trash-icon">&#x1F5D1;</span></button> <!-- Trash icon -->
  </div>
</div>
<script type="module">
  import { getCredentials } from '{{ site.baseurl }}/assets/js/api/login.js';
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
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
      const profilePic = document.getElementById('link');
      const usernameElement = document.getElementById('username');
      const themeElement = document.getElementById('theme-preference');
      if (!profilePic || !usernameElement || !themeElement) {
        console.error("Profile elements not found in DOM.");
        return;
      }
      usernameElement.textContent = credentials.name || 'Unknown User';
      const theme = credentials.theme || 'Dark';
      themeElement.textContent = `Preferred Theme: ${theme}`;
      applyThemeColors(theme);
      if (credentials.pfp) {
        if (credentials.pfp.startsWith("data:image")) {
          profilePic.src = credentials.pfp;
        } else if (credentials.pfp.startsWith("/") || credentials.pfp.includes("http")) {
          profilePic.src = credentials.pfp;
        } else {
          profilePic.src = `/user-images/${credentials.pfp}`;
        }
      } else {
        profilePic.src = '{{ site.baseurl }}/images/profile.jpg';
      }
      profilePic.onerror = function () {
        this.src = '{{ site.baseurl }}/images/profile.jpg';
      };
    } catch (error) {
      console.error('Error fetching profile data:', error);
    }
  }

  async function updateTheme(theme) {
    const themeElement = document.getElementById('theme-preference');
    themeElement.textContent = `Preferred Theme: ${theme}`;
    applyThemeColors(theme);
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
        document.getElementById('link').src = '{{ site.baseurl }}/images/profile.jpg';
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
    document.getElementById('light-mode-btn').addEventListener('click', function() {
      updateTheme('Light');
    });
    document.getElementById('dark-mode-btn').addEventListener('click', function() {
      updateTheme('Dark');
    });
  });
</script>
