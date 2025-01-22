---
layout: post
title: Notifications
permalink: /notif/
author: Kushi Gade
comments: true
---

<!-- Link to the external CSS file -->
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/notif_styles.css">
<h1 class="page-title">Send Notification</h1>
<div class="form-container">
    <form id="notificationForm">
        <label for="content">Notification Content:</label>
        <textarea id="content" name="content" required placeholder="Enter notification content..."></textarea>
        <label for="recipient_id">Recipient:</label>
        <select id="recipient_id" name="recipient_id" required>
            <option value="" disabled selected>Select a user</option>
        </select>
        <button type="submit" class="primary-btn">Send Notification</button>
    </form>
    <div id="message" class="message"></div>
</div>

<h2 class="section-title">Your Notifications</h2>
<div id="notificationsList" class="notifications-container"></div>

<script type="module">
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
  console.log("Notification script loaded");

 // Function to populate the user dropdown
async function populateUserDropdown() {
  try {
    // Call the endpoint that returns users with id and name
   const response = await fetch(`${pythonURI}/api/users/id-name`, {
        ...fetchOptions,
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });


    if (!response.ok) {
      const errorMessage = await response.text();
      throw new Error(`Failed to fetch users: ${response.statusText} - ${errorMessage}`);
    }

    // Get the list of users from the response
    const users = await response.json();

    // Get the dropdown element by ID
    const userDropdown = document.getElementById('recipient_id');

    // Clear the existing options and add a default prompt
    userDropdown.innerHTML = '<option value="" disabled selected>Select a user</option>';

    // Loop through the users and add them as options
    users.forEach(user => {
      const option = document.createElement('option');
      option.value = user.id;  // Use the user's id as the option value
      option.textContent = user.name;  // Use the user's name as the option text
      userDropdown.appendChild(option);
    });
  } catch (error) {
    console.error('Error populating user dropdown:', error);
    alert('Failed to load user list. Please try again.');
  }
}


  // Handle the form submission to create a new notification
  document.getElementById("notificationForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const postData = {
      content: document.getElementById("content").value,
      recipient_id: document.getElementById("recipient_id").value, // Selected user ID
    };
    console.log("Notification Data:", postData);

    try {
      const response = await fetch(`${pythonURI}/api/notification`, {
        ...fetchOptions,
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData)
      });

      if (!response.ok) {
        const errorMessage = await response.text();
        throw new Error(`Failed to send notification: ${response.statusText} - ${errorMessage}`);
      }
      
      alert("Notification sent successfully!");
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to send notification.");
    }
  });

  // Function to fetch notifications
  async function fetchNotifications() {
    try {
      const response = await fetch(`${pythonURI}/api/notifications`, {
        ...fetchOptions,
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        const errorMessage = await response.text();
        throw new Error(`Failed to fetch notifications: ${response.statusText} - ${errorMessage}`);
      }

      const notifications = await response.json();
      displayNotifications(notifications);
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to fetch notifications.");
    }
  }

  // Function to display notifications
  function displayNotifications(notifications) {
    const notificationsList = document.getElementById("notificationsList");
    notificationsList.innerHTML = '';

    if (notifications.length === 0) {
      notificationsList.innerHTML = "<p>No notifications available.</p>";
      return;
    }

    notifications.forEach(notification => {
      const notificationElement = document.createElement("div");
      notificationElement.classList.add("notification-item");

      notificationElement.innerHTML = `
        <p style="color: black;"><strong>Notification:</strong> ${notification.content}</p>
        <p style="color: black;"><small>Received at: ${new Date(notification.created_at).toLocaleString()}</small></p>
      `;

      notificationsList.appendChild(notificationElement);
    });
  }
  // Populate user dropdown on page load
  document.addEventListener('DOMContentLoaded', () => {
    populateUserDropdown(); // Populate the user dropdown
    fetchNotifications(); // Fetch notifications immediately when page loads
  });
</script>
