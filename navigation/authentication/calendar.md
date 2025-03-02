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
        grid-template-columns: repeat(7, 1fr); /* Ensure each column takes equal width */
        gap: 5px;
        padding: 10px;
        box-sizing: border-box;
        grid-auto-rows: 1fr; /* Ensure all rows are the same height */
    }

    .day {
        border: 1px solid #ddd;
        cursor: pointer;
        background: white;
        border-radius: 5px;
        width: 100%; /* Ensures the day cell takes full available space */
        height: 100%; /* Ensures cells are square-shaped */
        box-sizing: border-box; /* Includes padding and border in height/width calculation */
        display: flex;
        justify-content: center;
        align-items: center;  /* Center content in the cell */
        overflow: hidden; /* Hide overflow */
    }

    .day-name, .day {
        text-align: center;
        padding: 5px;  /* Adjust padding to make it more compact */
        font-size: 14px;  /* Decrease font size to fit better */
        color: black;
        box-sizing: border-box;  /* Ensure border and padding are included in width/height calculation */
        word-wrap: break-word; /* Prevent text from overflowing */
        overflow: hidden; /* Prevent overflow */
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
    .calendar-header-days {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 5px;
        padding: 10px;
        background-color: #8B0000;
        border-radius: 5px;
        margin-bottom: 5px;
    }

    .day-name {
        text-align: center;
        font-weight: bold;
        color: white;
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

<script type="module">
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

  let currentMonth = new Date().getMonth();
  let currentYear = new Date().getFullYear();
  let events = [];

  document.addEventListener('DOMContentLoaded', function() {
      initializeCalendar();
      fetchEvents(); // Load existing events from database
  });

  function initializeCalendar() {
      renderCalendar();
  }

  function renderCalendar() {
    const monthYear = document.getElementById("month-year");
    const calendarDays = document.getElementById("calendar-days");
    monthYear.textContent = `${new Date(currentYear, currentMonth).toLocaleString('default', { month: 'long' })} ${currentYear}`;
    calendarDays.innerHTML = "";

    // Weekday names to display at the top
    const weekdayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

    // Create and append the weekday names header row
    const weekdayHeader = document.createElement("div");
    weekdayHeader.classList.add("calendar-header-days");
    weekdayNames.forEach(dayName => {
        const dayHeaderCell = document.createElement("div");
        dayHeaderCell.classList.add("day-name");
        dayHeaderCell.textContent = dayName;
        weekdayHeader.appendChild(dayHeaderCell);
    });
    calendarDays.appendChild(weekdayHeader);

    // Calculate the first day of the month and the number of days in the month
    const firstDay = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

    // Add empty cells to align the first day of the month correctly
    for (let i = 0; i < firstDay; i++) {
        calendarDays.appendChild(document.createElement("div"));
    }

    // Add day cells for the days in the month
    for (let day = 1; day <= daysInMonth; day++) {
        const dayCell = document.createElement("div");
        dayCell.classList.add("day");
        dayCell.textContent = day;

        const formattedDate = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
        const eventsOnDay = events.filter(event => new Date(event.date).toISOString().split("T")[0] === formattedDate);

        if (eventsOnDay.length > 0) {
            dayCell.classList.add("event-day");

            eventsOnDay.forEach(event => {
                const emoji = document.createElement("div");
                emoji.classList.add("event-emoji");
                emoji.textContent = "❗";
                emoji.title = `${event.name} @ ${event.location}`; // Tooltip when hovering
                dayCell.appendChild(emoji);
            });
        }

        dayCell.addEventListener("click", () => {
            document.getElementById("startDate").value = formattedDate;
        });

        calendarDays.appendChild(dayCell);
    }
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
    fetchEvents(); // Fetch events for the new month
    renderCalendar(); // Update the calendar view immediately
};


  document.getElementById("eventForm").addEventListener("submit", async function(event) {
      event.preventDefault();

      const postData = {
          name: document.getElementById("eventName").value,
          location: document.getElementById("eventLocation").value,
          date: document.getElementById("startDate").value,  // YYYY-MM-DD format
      };

      console.log("Event Data:", postData);  // Log event data for debugging

      try {
          const response = await fetch(`${pythonURI}/api/event`, {
              ...fetchOptions,
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(postData)
          });

          if (!response.ok) {
              const errorMessage = await response.text();
              throw new Error(`Failed to add event: ${response.statusText} - ${errorMessage}`);
          }

          const createdEvent = await response.json();
          alert("Event added successfully!");

          if (createdEvent.id) {
              events.push(createdEvent);
              renderCalendar(); // Update calendar display
              displayEvents(); // Show updated event list
          } else {
              console.error("Error: Event created but no ID returned from API");
          }

          this.reset(); // Clear the form
      } catch (error) {
          console.error("Error:", error);
          alert("Error adding event. Please try again.");
      }
  });

  function displayEvents() {
      const eventList = document.getElementById("event-list");
      eventList.innerHTML = "";
      events.forEach(event => {
          const eventItem = document.createElement("div");
          eventItem.textContent = `${event.date}: ${event.name} @ ${event.location}`;
          eventList.appendChild(eventItem);
      });
  }

async function fetchEvents() {
    try {
        const response = await fetch(`${pythonURI}/api/events?month=${currentMonth + 1}&year=${currentYear}`, { ...fetchOptions, method: 'GET' });

        if (!response.ok) {
            throw new Error(`Failed to fetch events: ${response.statusText}`);
        }

        events = await response.json();
        renderCalendar(); // Now render calendar with the updated events
        displayEvents();
    } catch (error) {
        console.error("Error fetching events:", error);
    }
}

</script>
