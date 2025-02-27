---
layout: post
title: Calendar and Notifications
permalink: /calendar
menu: nav/home.html
search_exclude: true
show_reading_time: false
---

<style>
    .container {
        display: flex;
        justify-content: space-between;
        width: 90%;
        margin: auto;
        padding: 20px;
    }
    .calendar-container {
        width: 60%;
        text-align: center;
        padding: 20px;
        background: #007BFF;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .event-container {
        width: 35%;
        padding: 20px;
        background: #007BFF;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 5px;
        padding: 10px;
    }
    .day-name, .day {
        text-align: center;
        padding: 10px;
        font-size: 16px;
        color: black;
    }
    .day {
        border: 1px solid #ddd;
        cursor: pointer;
        background: #87CEFA;
        border-radius: 5px;
    }
    .day:hover {
        background: #0056b3;
    }
    .event-day {
        background-color: #0056b3;
    }
    .event-item {
        background: #87CEFA;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
    }
    .notifications-container {
        width: 70%;
        margin: auto;
        text-align: center;
        padding: 20px;
        background: #007BFF;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
</style>

<div class="container">
    <!-- Calendar Section -->
    <div class="calendar-container">
        <div class="calendar-header">
            <button id="prev-month" onclick="changeMonth(-1)">&#10094;</button>
            <div class="month-year" id="month-year"></div>
            <button id="next-month" onclick="changeMonth(1)">&#10095;</button>
        </div>
        <div class="calendar-grid" id="calendar-days"></div>
    </div>
    <!-- Event Form & List -->
    <div class="event-container">
        <h3 style="color: black;">Add Event</h3>
        <form id="eventForm">
            <label for="eventName" style="color: black;">Event Name:</label>
            <input type="text" id="eventName" required><br><br>
            <label for="eventLocation" style="color: black;">Location:</label>
            <input type="text" id="eventLocation" required><br><br>
            <label for="startDate" style="color: black;">Date:</label>
            <input type="date" id="startDate" required><br><br>
            <button type="submit">Save Event</button>
        </form>
        <h3 style="color: black; margin-top: 20px;">Your Events</h3>
        <div id="event-list"></div>
    </div>
</div>

<!-- Notifications Section -->
<div class="notifications-container">
    <h1 class="page-title" style="color: black;">Send Notification</h1>
    <form id="notificationForm">
        <label for="content" style="color: black;">Notification Content:</label>
        <textarea id="content" required placeholder="Enter notification content..."></textarea>
        <label for="recipient_id" style="color: black;">Recipient:</label>
        <select id="recipient_id" required>
            <option value="" disabled selected>Select a user</option>
        </select>
        <button type="submit">Send Notification</button>
    </form>
    <h2 style="color: black;">Your Notifications</h2>
    <div id="notificationsList"></div>
</div>

<script type="module">
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

  let currentMonth = new Date().getMonth();
  let currentYear = new Date().getFullYear();
  let events = [];

  document.addEventListener('DOMContentLoaded', function() {
      initializeCalendar();
      populateUserDropdown();
      fetchNotifications();
  });

  function initializeCalendar() {
      renderCalendar();
  }

  function renderCalendar() {
      const monthYear = document.getElementById("month-year");
      const calendarDays = document.getElementById("calendar-days");
      monthYear.textContent = `${new Date(currentYear, currentMonth).toLocaleString('default', { month: 'long' })} ${currentYear}`;
      calendarDays.innerHTML = "";
      
      const firstDay = new Date(currentYear, currentMonth, 1).getDay();
      const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
      
      for (let i = 0; i < firstDay; i++) {
          calendarDays.appendChild(document.createElement("div"));
      }
      
      for (let day = 1; day <= daysInMonth; day++) {
          const dayCell = document.createElement("div");
          dayCell.classList.add("day");
          dayCell.textContent = day;
          dayCell.addEventListener("click", () => document.getElementById("startDate").value = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`);
          calendarDays.appendChild(dayCell);
      }
  }

  function changeMonth(direction) {
      currentMonth += direction;
      if (currentMonth < 0) {
          currentMonth = 11;
          currentYear--;
      } else if (currentMonth > 11) {
          currentMonth = 0;
          currentYear++;
      }
      renderCalendar();
  }

  async function populateUserDropdown() {
      try {
          const response = await fetch(`${pythonURI}/api/users/id-name`, fetchOptions);
          if (!response.ok) {
              throw new Error('Failed to fetch users');
          }
          const users = await response.json();
          const recipientSelect = document.getElementById("recipient_id");
          recipientSelect.innerHTML = '<option value="" disabled selected>Select a user</option>';
          users.forEach(user => {
              const option = document.createElement("option");
              option.value = user.id;
              option.textContent = user.name;
              recipientSelect.appendChild(option);
          });
      } catch (error) {
          console.error("Error fetching users:", error);
      }
  }

  document.getElementById("notificationForm").addEventListener("submit", async function(event) {
      event.preventDefault();
      
      const content = document.getElementById("content").value;
      const recipient_id = document.getElementById("recipient_id").value;
      
      if (!content || !recipient_id) {
          alert("Please fill in all fields.");
          return;
      }
      
      const notificationData = {
          content: content,
          recipient_id: recipient_id
      };
      
      try {
          const response = await fetch(`${pythonURI}/api/notification`, {
              ...fetchOptions,
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(notificationData),
          });
          if (!response.ok) {
              throw new Error('Failed to send notification');
          }
          alert('Notification sent!');
          document.getElementById("notificationForm").reset();
          fetchNotifications();
      } catch (error) {
          console.error("Error sending notification:", error);
      }
  });

  async function fetchNotifications() {
      try {
          const response = await fetch(`${pythonURI}/api/notifications`, fetchOptions);
          if (!response.ok) {
              throw new Error('Failed to fetch notifications');
          }
          const notifications = await response.json();
          const notificationsList = document.getElementById("notificationsList");
          notificationsList.innerHTML = notifications.map(n => `<p><strong>${n.sender}:</strong> ${n.content}</p>`).join('');
      } catch (error) {
          console.error("Error fetching notifications:", error);
      }
  }
</script>
