---
layout: post
title: Calendar and Notifications
permalink: /calendar
menu: nav/home.html
search_exclude: true
show_reading_time: false
---

<div class="profile-container">
 <div class="card">
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
 </div>
</div>

<script type="module">
import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

async function populateUserDropdown() {
  try {
    const response = await fetch(`${pythonURI}/api/users/id-name`, {
      ...fetchOptions,
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    });

    if (!response.ok) throw new Error(`Failed to fetch users: ${await response.text()}`);

    const users = await response.json();
    const userDropdown = document.getElementById('recipient_id');
    userDropdown.innerHTML = '<option value="" disabled selected>Select a user</option>';

    users.forEach(user => {
      const option = document.createElement('option');
      option.value = user.id;
      option.textContent = user.name;
      userDropdown.appendChild(option);
    });
  } catch (error) {
    console.error('Error populating user dropdown:', error);
    alert('Failed to load user list. Please try again.');
  }
}

document.getElementById("notificationForm").addEventListener("submit", async function(event) {
  event.preventDefault();
  const postData = {
    content: document.getElementById("content").value,
    recipient_id: document.getElementById("recipient_id").value,
  };
  try {
    const response = await fetch(`${pythonURI}/api/notification`, {
      ...fetchOptions,
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(postData)
    });
    if (!response.ok) throw new Error(`Failed to send notification: ${await response.text()}`);
    alert("Notification sent successfully!");
  } catch (error) {
    console.error("Error:", error);
    alert("Failed to send notification.");
  }
});

async function fetchNotifications() {
  try {
    const response = await fetch(`${pythonURI}/api/notifications`, {
      ...fetchOptions,
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    });
    if (!response.ok) throw new Error(`Failed to fetch notifications: ${await response.text()}`);
    const notifications = await response.json();
    displayNotifications(notifications);
  } catch (error) {
    console.error("Error:", error);
    alert("Failed to fetch notifications.");
  }
}

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

document.addEventListener('DOMContentLoaded', () => {
  populateUserDropdown();
  fetchNotifications();
});
</script>

<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/notif_styles.css">
