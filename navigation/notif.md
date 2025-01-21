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
        <label for="recipient_id">Recipient User ID:</label>
        <input type="number" id="recipient_id" name="recipient_id" required placeholder="Enter recipient's user ID">
        <button type="submit" class="primary-btn">Send Notification</button>
    </form>
    <div id="message" class="message"></div>
</div>

<h2 class="section-title">Your Notifications</h2>
<div id="notificationsList" class="notifications-container"></div>
<button id="fetchNotifications" class="primary-btn">Fetch Notifications</button>

<script type="module">
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
  console.log("Notification script loaded");

  // Handle the form submission to create a new notification
  document.getElementById("notificationForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const postData = {
      content: document.getElementById("content").value,
      recipient_id: document.getElementById("recipient_id").value,  // User ID to notify
    };
    console.log("Notification Data:", postData);  // Log the notification data to check before sending

    try {
      const response = await fetch(`${pythonURI}/api/notification`, {
        ...fetchOptions,
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData)
      });

      // Check if the response is not OK and provide a more specific error message
      if (!response.ok) {
        const errorMessage = await response.text(); // Extract error message from response
        throw new Error(`Failed to send notification: ${response.statusText} - ${errorMessage}`);
      }
      
      alert("Notification sent successfully!");
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to send notification.");
    }
  });

  // Function to fetch notifications for the current user
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
        const errorMessage = await response.text();  // Extract error message from response
        throw new Error(`Failed to fetch notifications: ${response.statusText} - ${errorMessage}`);
      }

      const notifications = await response.json();
      displayNotifications(notifications);
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to fetch notifications.");
    }
  }

  // Function to display notifications in the UI
  function displayNotifications(notifications) {
    const notificationsList = document.getElementById("notificationsList");
    notificationsList.innerHTML = '';  // Clear the current notifications list

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

  // Fetch notifications when the "Fetch Notifications" button is clicked
  document.getElementById("fetchNotifications").addEventListener("click", fetchNotifications);
</script>
