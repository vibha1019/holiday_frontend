---
layout: post
title: Calendar
permalink: /calendar
menu: nav/home.html
search_exclude: true
show_reading_time: false
---

<style>
    body {
        background-image: url('images/greenbg.png');
        background-size: cover;
        font-family: 'Segoe UI', sans-serif;
        margin: 0;
        padding: 20px;
    }
    
    .container {
        display: flex;
        justify-content: space-between;
        width: 90%;
        max-width: 1200px;
        margin: 0 auto;
        gap: 25px;
    }
    
    .calendar-container, .event-container {
        background: rgba(255, 255, 255, 0.96);
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12);
    }
    
    .calendar-container {
        width: 60%;
    }
    
    .event-container {
        width: 40%;
    }
    
    .calendar-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    
    .calendar-header button {
        background: #4a6fa5;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        cursor: pointer;
        font-size: 16px;
        transition: all 0.2s;
    }
    
    .calendar-header button:hover {
        background: #3a5a8f;
        transform: translateY(-2px);
    }
    
    .month-year {
        font-size: 22px;
        font-weight: 600;
        color: #2c3e50;
    }
    
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 8px;
        padding: 10px;
    }
    
    .day-name {
        text-align: center;
        padding: 12px 0;
        font-weight: 600;
        color: #2c3e50;
        background: #f1f5f9;
        border-radius: 8px;
    }
    
    .day {
        text-align: center;
        padding: 15px 0;
        font-size: 16px;
        color: #2c3e50;
        border: 1px solid #e2e8f0;
        cursor: pointer;
        background: white;
        border-radius: 8px;
        transition: all 0.2s;
        min-height: 50px;
        position: relative;
    }
    
    .day:hover {
        background: #f1f5f9 !important;
        transform: scale(1.03);
    }
    
    .event-day {
        background: #e8f5e9 !important;
    }
    
    .today {
        border: 3px solid #4a6fa5 !important;
        font-weight: bold;
    }
    
    .event-emoji {
        font-size: 14px;
        color: #4a6fa5;
        position: absolute;
        bottom: 5px;
        right: 5px;
    }
    
    .event-container h3 {
        color: #2c3e50;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #e2e8f0;
    }
    
    .event-container label {
        display: block;
        margin-bottom: 8px;
        font-weight: 500;
        color: #4a5568;
    }
    
    .event-container input {
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        font-size: 15px;
    }
    
    .event-container button[type="submit"] {
        width: 100%;
        padding: 12px;
        background: #4a6fa5;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .event-container button[type="submit"]:hover {
        background: #3a5a8f;
        transform: translateY(-2px);
    }
    
    .search-box {
        margin: 25px 0 15px 0;
    }
    
    .search-box input {
        width: 100%;
        padding: 10px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
    }
    
    .event-item {
    padding: 15px;
    margin: 12px 0;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    border-left: 4px solid #4a6fa5;
    position: relative;
    animation: fadeIn 0.3s ease-out;
    color: #333 !important; /* This is the critical line */
}

.event-item strong {
    color: #2c3e50 !important;
    display: block;
    margin-bottom: 5px;
}

.event-item div {
    color: #4a5568 !important;
}
    
    .delete-icon {
        position: absolute;
        top: 15px;
        right: 15px;
        color: #e53e3e;
        cursor: pointer;
        font-size: 18px;
        transition: all 0.2s;
    }
    
    .delete-icon:hover {
        color: #c53030;
        transform: scale(1.1);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @media (max-width: 900px) {
        .container {
            flex-direction: column;
        }
        .calendar-container, 
        .event-container {
            width: 100%;
        }
    }
</style>

<div class="container">
    <!-- Calendar Section -->
    <div class="calendar-container">
        <div class="calendar-header">
            <button id="prev-month" onclick="changeMonth(-1)">‹ Previous</button>
            <div class="month-year" id="month-year"></div>
            <button id="next-month" onclick="changeMonth(1)">Next ›</button>
        </div>
        <div class="calendar-grid" id="calendar-days"></div>
    </div>
    
    <!-- Event Form & List -->
    <div class="event-container">
        <h3>Add Event</h3>
        <form id="eventForm">
            <label for="eventName">Event Name:</label>
            <input type="text" id="eventName" required>
            
            <label for="eventLocation">Location:</label>
            <input type="text" id="eventLocation" required>
            
            <label for="startDate">Date:</label>
            <input type="date" id="startDate" required>
            
            <button type="submit">Save Event</button>
        </form>
        
        <div class="search-box">
            <h3>Your Events</h3>
            <input type="text" id="searchInput" placeholder="Search events...">
        </div>
        <div id="event-list"></div>
    </div>
</div>

<script type="module">
    /* AP CSP Create Task - Event Calendar  
    * Developed by V.M.
    * All code written by student except:  
    * - fetch API template provided by teacher  
    */

  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

  class EventManager {
    constructor() {
      this.events = [];
    }

    formatDate(date) {
      const d = new Date(date);
      return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
    }

    sortEvents() {
      this.events.sort((a, b) => new Date(a.date) - new Date(b.date));
    }

    filterEvents(keyword) {
      const searchTerm = keyword.toLowerCase();
      return this.events.filter(event => 
        event.location.toLowerCase().includes(searchTerm) ||
        event.name.toLowerCase().includes(searchTerm)
      );
    }

    async fetchEvents(month, year) {
      try {
        const response = await fetch(`${pythonURI}/api/events?month=${month}&year=${year}`, { 
          ...fetchOptions, 
          method: 'GET' 
        });
        if (!response.ok) throw new Error("Failed to fetch events.");
        this.events = await response.json();
        this.sortEvents();
      } catch (error) {
        console.error("Fetch error:", error);
        alert("Could not load events. Please try again later.");
      }
    }

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

  const eventManager = new EventManager();
  let currentMonth = new Date().getMonth();
  let currentYear = new Date().getFullYear();

  document.addEventListener('DOMContentLoaded', () => {
    renderCalendar();
    eventManager.fetchEvents(currentMonth + 1, currentYear);
    setupEventListeners();
  });

  function isValidDate(date) {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    return new Date(date) >= today;
  }

  function renderCalendar() {
    const monthYear = document.getElementById("month-year");
    const calendarDays = document.getElementById("calendar-days");
    monthYear.textContent = `${new Date(currentYear, currentMonth).toLocaleString('default', { month: 'long' })} ${currentYear}`;
    calendarDays.innerHTML = "";

    const firstDay = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    const today = new Date();

    // Day names
    ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].forEach(day => {
      const dayNameCell = document.createElement("div");
      dayNameCell.classList.add("day-name");
      dayNameCell.textContent = day;
      calendarDays.appendChild(dayNameCell);
    });

    // Empty cells
    for (let i = 0; i < firstDay; i++) {
      calendarDays.appendChild(document.createElement("div"));
    }

    // Days
    for (let day = 1; day <= daysInMonth; day++) {
      const dayCell = document.createElement("div");
      dayCell.classList.add("day");
      dayCell.textContent = day;

      // Highlight today
      if (currentYear === today.getFullYear() && 
          currentMonth === today.getMonth() && 
          day === today.getDate()) {
        dayCell.classList.add("today");
      }

      const formattedDate = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
      const eventsOnDay = eventManager.events.filter(event => 
        eventManager.formatDate(event.date) === formattedDate
      );

      if (eventsOnDay.length > 0) {
        dayCell.classList.add("event-day");
        const emoji = document.createElement("div");
        emoji.classList.add("event-emoji");
        emoji.textContent = "🔹";
        emoji.title = eventsOnDay.map(e => `${e.name} @ ${e.location}`).join('\n');
        dayCell.appendChild(emoji);
      }

      dayCell.addEventListener("click", () => {
        document.getElementById("startDate").value = formattedDate;
      });

      calendarDays.appendChild(dayCell);
    }
  }

  function displayEvents(events = eventManager.events) {
    const eventList = document.getElementById("event-list");
    eventList.innerHTML = "";

    if (events.length === 0) {
      eventList.innerHTML = `<p style="color: #718096; text-align: center;">No events found</p>`;
      return;
    }

    events.forEach(event => {
      const eventItem = document.createElement("div");
      eventItem.classList.add("event-item");
      eventItem.innerHTML = `
        <strong>${eventManager.formatDate(event.date)}</strong>
        <div>${event.name} @ ${event.location}</div>
        <span class="delete-icon" data-id="${event.event_id}">✕</span>
      `;
      eventList.appendChild(eventItem);
    });
  }

  function setupEventListeners() {
    document.getElementById("eventForm").addEventListener("submit", async (e) => {
      e.preventDefault();
      const dateInput = document.getElementById("startDate").value;

      if (!isValidDate(dateInput)) {
        alert("Event date must be today or in the future!");
        return;
      }

      const success = await eventManager.addEvent({
        name: document.getElementById("eventName").value,
        location: document.getElementById("eventLocation").value,
        date: dateInput
      });

      if (success) {
        renderCalendar();
        displayEvents();
        e.target.reset();
      }
    });

    document.getElementById("searchInput").addEventListener("input", (e) => {
      const filtered = eventManager.filterEvents(e.target.value);
      displayEvents(filtered);
    });

    document.getElementById("event-list").addEventListener("click", async (e) => {
      if (e.target.classList.contains("delete-icon")) {
        const eventId = e.target.dataset.id;
        const event = eventManager.events.find(ev => ev.event_id == eventId);
        if (confirm(`Delete "${event.name}" event?`)) {
          const success = await eventManager.deleteEvent(eventId);
          if (success) {
            renderCalendar();
            displayEvents();
          }
        }
      }
    });
  }

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