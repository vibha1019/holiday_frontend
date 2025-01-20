---
layout: post
title: Event Calendar
permalink: /holiday/event_calendar/
author: Vibha Mandayam
comments: true
---

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

<script>
    console.log("Script loaded");  // Check in the console if this message appears

    const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let currentDate = new Date();

    function renderCalendar() {
        const monthYear = document.getElementById("month-year");
        const calendarDays = document.getElementById("calendar-days");

        // Set the month and year at the top
        monthYear.textContent = `${monthNames[currentDate.getMonth()]} ${currentDate.getFullYear()}`;

        // Get the first day of the month
        const firstDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
        const lastDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);
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
            if (day === currentDate.getDate() && currentDate.getMonth() === new Date().getMonth() && currentDate.getFullYear() === new Date().getFullYear()) {
                dayCell.classList.add("current-day");
            }

            dayCell.textContent = day;
            dayCell.addEventListener("click", function() {
                openModal(day); // Pass the correct day to the modal
            });

            calendarDays.appendChild(dayCell);
        }
    }

    function changeMonth(offset) {
        currentDate.setMonth(currentDate.getMonth() + offset);
        renderCalendar();
    }

    // Initialize the calendar
    renderCalendar();

    // Function to open the event form modal
    function openModal(date) {
        document.getElementById("eventModal").style.display = "block";
        // Prefill the date field with the selected date in YYYY-MM-DD format
        const formattedDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), date).toISOString().split('T')[0];
        document.getElementById("startDate").value = formattedDate;
    }

    // Function to close the modal
    function closeModal() {
        document.getElementById("eventModal").style.display = "none";
    }

    // Handle the form submission to create a new event
    document.getElementById("eventForm").addEventListener("submit", async function(event) {
        event.preventDefault();

        const eventData = {
            name: document.getElementById("eventName").value,
            location: document.getElementById("eventLocation").value,
            date: document.getElementById("startDate").value,  // This will be in YYYY-MM-DD format
        };

        console.log("Event Data:", eventData);  // Log the event data to check before sending

        try {
            const response = await fetch(`http://127.0.0.1:8887/api/event`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(eventData),
            });

            if (!response.ok) throw new Error('Failed to add event: ' + response.statusText);

            const data = await response.json();
            alert("Event created successfully!");
            closeModal();
            // Optionally refresh the calendar to show the new event
        } catch (error) {
            console.error('Error creating event:', error);
            alert("Error creating event.");
        }
    });
</script>
