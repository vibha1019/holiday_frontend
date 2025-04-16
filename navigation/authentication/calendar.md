---
layout: post
title: Calendar
permalink: /calendar
menu: nav/home.html
search_exclude: true
show_reading_time: false
author: nora + vibha
---
<style>
    body {
        background-image: url('images/greenbg.png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
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
        background: #8B0000;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .event-container {
        width: 35%;
        padding: 20px;
        background: #8B0000;
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
        background: white;
        border-radius: 5px;
    }
    .day:hover {
        background: #800000;
    }
    .event-day {
        background-color: #800000;
    }
    .event-emoji {
        font-size: 20px;
        color: red;
        margin-top: 5px;
    }
    .event-container button {
        background: white;
        color: black;
        border: none;
        padding: 10px 15px;
        border-radius: 5px;
        cursor: pointer;
    }
    .event-container button:hover {
        background: #CD5C5C;
    }
    .event-item {
        position: relative;
        padding: 10px;
        margin: 10px 0;
        background-color: #8B0000;
        border-radius: 5px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
    }
    .delete-icon {
        position: absolute;
        top: 5px;
        right: 5px;
        font-size: 20px;
        color: red;
        cursor: pointer;
    }
    .delete-icon:hover {
        color: darkred;
    }
    /* NEW: Search/filter UI */
    .search-box {
        margin-bottom: 15px;
    }
    .search-box input {
        padding: 8px;
        width: 70%;
        border-radius: 5px;
        border: 1px solid #ddd;
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
        <div class="search-box">
            <h3 style="color: black;">Your Events</h3>
            <input type="text" id="searchInput" placeholder="Search by location...">
        </div>
        <div id="event-list"></div>
    </div>
</div>

<script type="module">
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

  // ================== NEW: EVENT MANAGER CLASS (ABSTRACTION) ==================
  class EventManager {
    constructor() {
      this.events = [];
    }

    // Helper: Format date as YYYY-MM-DD
    formatDate(date) {
      const d = new Date(date);
      return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
    }

    // NEW: Sort events by date (ALGORITHM: SORTING)
    sortEvents() {
      this.events.sort((a, b) => new Date(a.date) - new Date(b.date));
    }

    // NEW: Filter events by location (ALGORITHM: SEARCHING)
    filterEvents(keyword) {
      return this.events.filter(event => 
        event.location.toLowerCase().includes(keyword.toLowerCase())
      );
    }

    // Fetch events from API
    async fetchEvents(month, year) {
      try {
        const response = await fetch(`${pythonURI}/api/events?month=${month}&year=${year}`, { 
          ...fetchOptions, 
          method: 'GET' 
        });
        if (!response.ok) throw new Error("Failed to fetch events.");
        this.events = await response.json();
        this.sortEvents(); // Sort after fetching
      } catch (error) {
        console.error("Fetch error:", error);
        alert("Could not load events. Check console.");
      }
    }

    // Add new event
    async addEvent(eventData) {
      try {
        const response = await fetch(`${pythonURI}/api/event`, {
          ...fetchOptions,
          method: 'POST',
          body: JSON.stringify(eventData),
        });
        if (!response.ok) throw new Error("Failed to save event.");
        const newEvent = await response.json();
        this.events.push(newEvent);
        this.sortEvents();
        return true;
      } catch (error) {
        console.error("Error:", error);
        alert(`Error: ${error.message}`);
        return false;
      }
    }

    // Delete event
    async deleteEvent(eventId) {
      try {
        const response = await fetch(`${pythonURI}/api/event`, {
          ...fetchOptions,
          method: 'DELETE',
          body: JSON.stringify({ event_id: eventId }),
        });
        if (!response.ok) throw new Error("Failed to delete event.");
        this.events = this.events.filter(event => event.event_id !== eventId);
        return true;
      } catch (error) {
        console.error("Error:", error);
        alert(`Error: ${error.message}`);
        return false;
      }
    }
  }

  // ================== MAIN APP ==================
  const eventManager = new EventManager();
  let currentMonth = new Date().getMonth();
  let currentYear = new Date().getFullYear();

  // Initialize the app
  document.addEventListener('DOMContentLoaded', () => {
    renderCalendar();
    eventManager.fetchEvents(currentMonth + 1, currentYear);
    setupEventListeners();
  });

  // NEW: Validate date (must be today or future)
  function isValidDate(date) {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    return new Date(date) >= today;
  }

  // Render the calendar grid
  function renderCalendar() {
    const monthYear = document.getElementById("month-year");
    const calendarDays = document.getElementById("calendar-days");
    monthYear.textContent = `${new Date(currentYear, currentMonth).toLocaleString('default', { month: 'long' })} ${currentYear}`;
    calendarDays.innerHTML = "";

    const firstDay = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

    // Day names header
    const dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    dayNames.forEach(day => {
      const dayNameCell = document.createElement("div");
      dayNameCell.classList.add("day-name");
      dayNameCell.textContent = day;
      calendarDays.appendChild(dayNameCell);
    });

    // Empty cells for days before the 1st
    for (let i = 0; i < firstDay; i++) {
      calendarDays.appendChild(document.createElement("div"));
    }

    // Days of the month
    for (let day = 1; day <= daysInMonth; day++) {
      const dayCell = document.createElement("div");
      dayCell.classList.add("day");
      dayCell.textContent = day;

      const formattedDate = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
      const eventsOnDay = eventManager.events.filter(event => 
        eventManager.formatDate(event.date) === formattedDate
      );

      if (eventsOnDay.length > 0) {
        dayCell.classList.add("event-day");
        eventsOnDay.forEach(event => {
          const emoji = document.createElement("div");
          emoji.classList.add("event-emoji");
          emoji.textContent = "❗";
          emoji.title = `${event.name} @ ${event.location}`;
          dayCell.appendChild(emoji);
        });
      }

      dayCell.addEventListener("click", () => {
        document.getElementById("startDate").value = formattedDate;
      });

      calendarDays.appendChild(dayCell);
    }
  }

  // Display events in the sidebar
  function displayEvents(events = eventManager.events) {
    const eventList = document.getElementById("event-list");
    eventList.innerHTML = "";

    if (events.length === 0) {
      eventList.innerHTML = "<p>No events found.</p>";
      return;
    }

    events.forEach(event => {
      const eventItem = document.createElement("div");
      eventItem.classList.add("event-item");
      eventItem.innerHTML = `
        <strong>${eventManager.formatDate(event.date)}</strong><br>
        ${event.name} @ ${event.location}
        <span class="delete-icon" data-id="${event.event_id}">❌</span>
      `;
      eventList.appendChild(eventItem);
    });
  }

  // Event listeners
  function setupEventListeners() {
    // Form submission
    document.getElementById("eventForm").addEventListener("submit", async (e) => {
      e.preventDefault();
      const dateInput = document.getElementById("startDate").value;

      if (!isValidDate(dateInput)) {
        alert("Event date must be today or later!");
        return;
      }

      const success = await eventManager.addEvent({
        name: document.getElementById("eventName").value,
        location: document.getElementById("eventLocation").value,
        date: dateInput,
      });

      if (success) {
        renderCalendar();
        displayEvents();
        e.target.reset();
      }
    });

    // Search/filter
    document.getElementById("searchInput").addEventListener("input", (e) => {
      const filtered = eventManager.filterEvents(e.target.value);
      displayEvents(filtered);
    });

    // Delete event (delegated)
    document.getElementById("event-list").addEventListener("click", (e) => {
      if (e.target.classList.contains("delete-icon")) {
        if (confirm("Delete this event?")) {
          eventManager.deleteEvent(e.target.dataset.id)
            .then(() => {
              renderCalendar();
              displayEvents();
            });
        }
      }
    });
  }

  // Month navigation
  window.changeMonth = function (direction) {
    currentMonth += direction;
    if (currentMonth < 0) {
      currentMonth = 11;
      currentYear--;
    } else if (currentMonth > 11) {
      currentMonth = 0;
      currentYear++;
    }
    eventManager.fetchEvents(currentMonth + 1, currentYear);
    renderCalendar();
  };
</script>