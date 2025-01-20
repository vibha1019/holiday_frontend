---
layout: post
title: Event Calendar
permalink: /holiday/event_calendar/
author: Vibha Mandayam
comments: true
---

<div class="main-content">
    <!-- Calendar on the left -->
    <div class="calendar-container">
        <div class="calendar-header">
            <button class="prev-month" onclick="changeMonth(-1)">&#10094;</button>
            <div class="month-year" id="month-year"></div>
            <button class="next-month" onclick="changeMonth(1)">&#10095;</button>
        </div>
        <div class="calendar-grid">
            <div class="day-name">Sun</div>
            <div class="day-name">Mon</div>
            <div class="day-name">Tue</div>
            <div class="day-name">Wed</div>
            <div class="day-name">Thu</div>
            <div class="day-name">Fri</div>
            <div class="day-name">Sat</div>
        </div>
        <div class="calendar-days" id="calendar-days"></div>
    </div>
    <!-- Sidebar for Upcoming Events on the right -->
    <div class="upcoming-events">
        <h3>Upcoming Events</h3>
        <div id="event-list">
            <!-- Event cards will be dynamically populated here -->
        </div>
    </div>
</div>

<!-- Modal for Event Form -->
<div id="eventModal" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal()">&times;</span>
        <h3>Add Event</h3>
        <form id="eventForm">
            <label for="eventName" style="color: black;">Event Name:</label>
            <input type="text" id="eventName" name="eventName" required><br><br>
            <label for="eventLocation" style="color: black;">Location:</label>
            <input type="text" id="eventLocation" name="eventLocation" required><br><br>
            <label for="startDate" style="color: black;">Date:</label>
            <input type="date" id="startDate" name="startDate" required><br><br>
            <button type="submit">Save Event</button>
        </form>
    </div>
</div>

<!-- Link to external styles.css -->
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/styles.css">

<script type="module">
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

  console.log("Event Calendar script loaded");

  let currentMonth = new Date().getMonth(); // Track the current month
  let events = [];  // Store the events globally

  document.addEventListener('DOMContentLoaded', function() {
      console.log("Base URL:", pythonURI);  // Debugging line

      // Fetch the user ID and then get the events for the user
      getUserId(pythonURI)  // Get user ID first
          .then(userId => {
              if (userId) {
                  getUserEvents(userId)  // Fetch events based on user ID
                      .then(fetchedEvents => {
                          events = fetchedEvents;  // Store events globally
                          renderCalendar(events);  // Pass events to the calendar
                      })
                      .catch(err => console.error("Error fetching events: ", err));
              }
          })
          .catch(err => {
              console.error("Error fetching user ID: ", err);
          });
  });

  function getUserId(baseurl) {
      const URL = baseurl + '/api/id';  // Endpoint to get the user info (including user ID)
      
      return fetch(URL, fetchOptions)
          .then(response => {
              if (response.status !== 200) {
                  console.error("HTTP status code: " + response.status);
                  return null;
              }
              return response.json();
          })
          .then(data => {
              if (data && data.id) {
                  console.log("User ID fetched:", data.id);
                  return data.id;  // Return the user ID
              }
              return null;
          })
          .catch(err => {
              console.error("Error fetching user ID:", err);
              return null;
          });
  }

  function getUserEvents(userId) {
      const URL = pythonURI + '/api/events/user/' + userId;  // Get events for the specific user
      return fetch(URL, fetchOptions)
          .then(response => {
              if (response.status !== 200) {
                  console.error("HTTP status code: " + response.status);
                  return [];
              }
              return response.json();
          })
          .then(events => {
              console.log("Events fetched:", events);
              return events;  // Return the events data
          })
          .catch(err => {
              console.error("Error fetching events:", err);
              return [];
          });
  }

  function renderCalendar(events) {
    const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let currentDate = new Date();
    const monthYear = document.getElementById("month-year");
    const calendarDays = document.getElementById("calendar-days");

    // Set the month and year at the top
    monthYear.textContent = `${monthNames[currentMonth]} ${currentDate.getFullYear()}`;

    // Get the first day of the month
    const firstDay = new Date(currentDate.getFullYear(), currentMonth, 1);
    const lastDate = new Date(currentDate.getFullYear(), currentMonth + 1, 0);
    const totalDays = lastDate.getDate();
    
    // Clear existing days
    calendarDays.innerHTML = "";

    // Fill in the empty cells before the first day
    for (let i = 0; i < firstDay.getDay(); i++) {
        const emptyCell = document.createElement("div");
        emptyCell.classList.add("day");
        calendarDays.appendChild(emptyCell);
    }

    // Fill in the days of the month
    for (let day = 1; day <= totalDays; day++) {
        const dayCell = document.createElement("div");
        dayCell.classList.add("day");

        // Highlight the current day
        if (day === currentDate.getDate() && currentMonth === new Date().getMonth() && currentDate.getFullYear() === new Date().getFullYear()) {
            dayCell.classList.add("current-day");
        }

        // Check if the current day has an event
        const eventDateString = `${currentDate.getFullYear()}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
        console.log("Checking date:", eventDateString);  // Log the day being checked
        console.log("Event dates:", events.map(event => event.date));  // Log all event dates

        if (events.some(event => event.date === eventDateString)) {
            console.log(`Event found on ${eventDateString}`);
            const dot = document.createElement("span");
            dot.classList.add("event-dot");  // Add a class for styling blue dots
            dayCell.appendChild(dot);
        }

        dayCell.textContent = day;

        // When a day is clicked, open the modal and prefill the date
        dayCell.addEventListener("click", function() {
            openModal(day); // Pass the clicked day to the modal
        });

        calendarDays.appendChild(dayCell);
    }
}

    function renderSidebar(events) {
        const eventList = document.getElementById("event-list");
        eventList.innerHTML = ""; // Clear existing events

        const upcomingEvents = events.filter(event => {
            const eventDate = new Date(event.date);
            return eventDate >= new Date(); // Only show future or current events
        });

        if (upcomingEvents.length === 0) {
            eventList.innerHTML = "<p>No upcoming events.</p>";
            return;
        }

        upcomingEvents.forEach(event => {
            const eventCard = document.createElement("div");
            eventCard.classList.add("event-card");

            const eventDate = document.createElement("div");
            eventDate.classList.add("event-date");
            const [year, month, day] = event.date.split("-");
            eventDate.innerHTML = `<span>${day}</span><span>${month}</span>`;

            const eventDetails = document.createElement("div");
            eventDetails.classList.add("event-details");
            eventDetails.innerHTML = `
                <p class="event-title">${event.name}</p>
                <p class="event-location">${event.location}</p>
            `;

            eventCard.appendChild(eventDate);
            eventCard.appendChild(eventDetails);
            eventList.appendChild(eventCard);
        });
    }


  function openModal(date) {
      document.getElementById("eventModal").style.display = "block";  // Show the modal
      // Prefill the date field with the selected date in YYYY-MM-DD format
      const currentDate = new Date();
      const formattedDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), date).toISOString().split('T')[0];
      document.getElementById("startDate").value = formattedDate;  // Populate the date input
  }

  function closeModal() {
    const modal = document.getElementById("eventModal");
    if (modal) {
        modal.style.display = "none"; // Hide the modal
    } else {
        console.error("Modal element not found!");
    }
}
    // Close modal when clicking outside the modal content
    window.addEventListener("click", function(event) {
        const modal = document.getElementById("eventModal");
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });


  // Handle the form submission to create a new event
  document.getElementById("eventForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const postData = {
        name: document.getElementById("eventName").value,
        location: document.getElementById("eventLocation").value,
        date: document.getElementById("startDate").value,  // This will be in YYYY-MM-DD format
    };

    console.log("Event Data:", postData);  // Log the event data to check before sending

    try {
      const response = await fetch(`${pythonURI}/api/event`, {
        ...fetchOptions,
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
      });

      // Check if the response is not OK and provide a more specific error message
      if (!response.ok) {
        const errorMessage = await response.text(); // Extract error message from response
        throw new Error(`Failed to add event: ${response.statusText} - ${errorMessage}`);
      }

      alert("Event added successfully!");

    } catch (error) {
      // Catch errors and provide more useful information
      console.error('Error adding event:', error.message);
      alert(`Error adding event: ${error.message}`);
    }
  });

  // Function to change the month
  function changeMonth(offset) {
    currentMonth += offset;
    if (currentMonth < 0) {
        currentMonth = 11; // Wrap around to December
    } else if (currentMonth > 11) {
        currentMonth = 0; // Wrap around to January
    }
    renderCalendar(events);  // Re-render calendar with the updated month
    renderSidebar(events);

  }
</script>
