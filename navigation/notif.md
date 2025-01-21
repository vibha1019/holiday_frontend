---
layout: post
title: Check Notifications Here
permalink: /notif/
author: Kushi Gade
comments: true
---

<!-- Link to the external CSS file -->
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/notif_styles.css">

<h1>Send Notification</h1>
<div class="form-container">
    <form id="notificationForm">
        <label for="content">Notification Content:</label>
        <textarea id="content" name="content" required placeholder="Enter notification content..."></textarea>
        <label for="recipient_id">Recipient User ID:</label>
        <input type="number" id="recipient_id" name="recipient_id" required placeholder="Enter recipient's user ID">
        <button type="submit">Send Notification</button>
    </form>
    <div id="message" class="message"></div>
</div>

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
</script>
