---
layout: post
title: Event Calendar
permalink: /holiday/event_calendar/
author: Vibha Mandayam
comments: true
---

<!-- 
AP COMPUTER SCIENCE PRINCIPLES - CREATE PERFORMANCE TASK
Event Calendar Application

Program Requirements Demonstrated:
1. INPUT: User input through form submission and calendar interactions
2. LIST: events array manages collection of event data
3. PROCEDURES: renderCalendar, deleteEvent, renderSidebar with parameters
4. ALGORITHMS: Sequencing, selection, iteration in renderCalendar
5. OUTPUT: Visual display of calendar and events

All code written by student with debugging assistance from ChatGPT for timezone handling.
-->


<div class="main-content">
    <!-- Calendar Display Section -->
    <div class="calendar-container">
        <div class="calendar-header">
            <button id="prev-month">&#10094;</button>
            <div class="month-year" id="month-year"></div>
            <button id="next-month">&#10095;</button>
        </div>
        <div class="calendar-grid">
            <!-- Day headers -->
            <div class="day-name">Sun</div>
            <div class="day-name">Mon</div>
            <div class="day-name">Tue</div>
            <div class="day-name">Wed</div>
            <div class="day-name">Thu</div>
            <div class="day-name">Fri</div>
            <div class="day-name">Sat</div>
        </div>
        <!-- Calendar days populated by JavaScript -->
        <div class="calendar-days" id="calendar-days"></div>
    </div>

    <!-- Upcoming Events Sidebar -->
    <div class="upcoming-events">
        <h3 style="color: black; font-size: 24px; font-weight: bold;">Upcoming Events</h3>
        <div id="event-list">
            <!-- Events populated by JavaScript -->
        </div>
    </div>
</div>

<!-- Event Creation Modal -->
<div id="eventModal" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal()">&times;</span>
        <h3>Add Event</h3>
        <!-- USER INPUT FORM -->
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

<script type="module">
/* 
 * MAIN PROGRAM CODE
 * Implements interactive event calendar with:
 * - Month navigation
 * - Event creation/deletion
 * - Visual calendar display
 */

// Import API configuration (assuming config.js exists)
import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

// GLOBAL VARIABLES
let events = [];  // LIST: Stores all event objects
let currentMonth = new Date().getMonth(); // Tracks current displayed month

// EVENT LISTENER: Form submission for new events
document.getElementById("eventForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    // ALGORITHM: Process form data (sequencing)
    const postData = {
        name: document.getElementById("eventName").value,
        location: document.getElementById("eventLocation").value,
        date: document.getElementById("startDate").value, // No timezone adjustment
    };
    
    // Send to server
    const response = await fetch(`${pythonURI}/api/event`, {
        ...fetchOptions,
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
    });
    
    // Error handling
    if (!response.ok) {
        const errorMessage = await response.text();
        throw new Error(`Failed to add event: ${response.statusText} - ${errorMessage}`);
    }
    
    // Update UI with new event
    const createdEvent = await response.json();
    if (createdEvent.id) {
        events.push(createdEvent); 
        renderSidebar(events);  // OUTPUT: Update event list
        renderCalendar(events); // OUTPUT: Update calendar
        closeModal();
    }
});

// INITIALIZATION: Load when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Load user data
    getUserId(pythonURI)
        .then(userId => {
            if (userId) {
                getUserEvents(userId)
                    .then(fetchedEvents => {
                        events = fetchedEvents;
                        renderCalendar(events);
                        renderSidebar(events);
                    });
            }
        });
    
    // INPUT: Month navigation event listeners
    document.getElementById('prev-month').addEventListener('click', () => changeMonth(-1));
    document.getElementById('next-month').addEventListener('click', () => changeMonth(1));
});

/* 
 * PROCEDURE: deleteEvent(eventId, eventElement)
 * Purpose: Deletes an event from server and UI
 * Parameters:
 *   - eventId: string - ID of event to delete
 *   - eventElement: DOM element - The event card to remove
 */
async function deleteEvent(eventId, eventElement) {
    try {
        // Confirm deletion
        const confirmDelete = confirm("Are you sure you want to delete this event?");
        if (!confirmDelete) return;
        
        // Send delete request
        const response = await fetch(`${pythonURI}/api/event/${eventId}`, {
            ...fetchOptions,
            method: 'DELETE'
        });
        
        if (!response.ok) throw new Error(`Delete failed`);
        
        // ALGORITHM: Update data and UI
        events = events.filter(event => event.id !== eventId); // Remove from list
        
        if (eventElement) eventElement.remove(); // Remove from DOM
        
        renderCalendar(events); // Update calendar
    } catch (error) {
        alert(`Error deleting event: ${error.message}`);
    }
}

/* 
 * PROCEDURE: renderCalendar(events)
 * Purpose: Renders calendar grid with events
 * Contains:
 *   - Sequencing: Steps to build calendar
 *   - Selection: Highlighting current day
 *   - Iteration: Looping through days
 */
function renderCalendar(events) {
    const monthNames = ["January", "February", "March", "April", "May", "June", 
                       "July", "August", "September", "October", "November", "December"];
    const currentDate = new Date();
    const monthYear = document.getElementById("month-year");
    const calendarDays = document.getElementById("calendar-days");
    
    // OUTPUT: Display current month/year
    monthYear.textContent = `${monthNames[currentMonth]} ${currentDate.getFullYear()}`;
    
    // Calculate calendar dates
    const firstDay = new Date(currentDate.getFullYear(), currentMonth, 1);
    const lastDate = new Date(currentDate.getFullYear(), currentMonth + 1, 0);
    const totalDays = lastDate.getDate();
    
    // Clear existing days
    calendarDays.innerHTML = "";
    
    // Add empty cells for days before first day of month
    for (let i = 0; i < firstDay.getDay(); i++) {
        calendarDays.appendChild(document.createElement("div").classList.add("day"));
    }
    
    // Create day cells
    for (let day = 1; day <= totalDays; day++) {
        const dayCell = document.createElement("div");
        dayCell.classList.add("day");
        
        // SELECTION: Highlight current day
        if (day === currentDate.getDate() && currentMonth === new Date().getMonth()) {
            dayCell.classList.add("current-day");
        }
        
        // Check for events on this day
        const eventDateString = `${currentDate.getFullYear()}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
        if (events.some(event => event.date === eventDateString)) {
            const dot = document.createElement("span");
            dot.classList.add("event-dot");
            dayCell.appendChild(dot);
        }
        
        dayCell.textContent = day;
        // INPUT: Make days clickable
        dayCell.addEventListener("click", () => openModal(day));
        calendarDays.appendChild(dayCell);
    }
}

/* 
 * PROCEDURE: renderSidebar(events)
 * Purpose: Displays list of upcoming events
 */
function renderSidebar(events) {
    const upcomingEventsContainer = document.getElementById("event-list");
    upcomingEventsContainer.innerHTML = "";
    
    // Sort events by date
    const sortedEvents = [...events].sort((a, b) => new Date(a.date) - new Date(b.date));
    
    // Create event cards
    sortedEvents.forEach(event => {
        const eventItem = document.createElement("div");
        eventItem.classList.add("event-item");
        
        // Event name
        const eventName = document.createElement("div");
        eventName.classList.add("event-name");
        eventName.textContent = event.name;
        
        // Event location
        const eventLocation = document.createElement("div");
        eventLocation.classList.add("event-location");
        eventLocation.textContent = event.location;
        
        // Event date (no timezone correction)
        const eventDate = document.createElement("div");
        eventDate.classList.add("event-date");
        eventDate.textContent = new Date(event.date).toLocaleDateString();
        
        // Delete button
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", () => {
            deleteEvent(event.id, eventItem);
        });
        
        // OUTPUT: Add all elements to card
        eventItem.append(eventName, eventLocation, eventDate, deleteButton);
        upcomingEventsContainer.appendChild(eventItem);
    });
}

// HELPER FUNCTIONS //
function openModal(date) {
    document.getElementById("eventModal").style.display = "block";
    const currentYear = new Date().getFullYear();
    document.getElementById("startDate").value = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(date).padStart(2, '0')}`;
}

function closeModal() {
    document.getElementById("eventModal").style.display = "none";
    document.getElementById("eventForm").reset();
}

function changeMonth(direction) {
    currentMonth += direction;
    if (currentMonth < 0) currentMonth = 11;
    if (currentMonth > 11) currentMonth = 0;
    renderCalendar(events);
}

// Close modal when clicking outside
window.addEventListener("click", function(event) {
    const modal = document.getElementById("eventModal");
    if (event.target === modal) {
        closeModal();
    }
});

// API HELPER FUNCTIONS //
function getUserId(baseurl) {
    return fetch(baseurl + '/api/id', fetchOptions)
        .then(response => {
            if (!response.ok) return null;
            return response.json();
        })
        .then(data => data?.id || null);
}

function getUserEvents(userId) {
    return fetch(`${pythonURI}/api/events/user/${userId}`, fetchOptions)
        .then(response => {
            if (!response.ok) return [];
            return response.json();
        });
}
</script>