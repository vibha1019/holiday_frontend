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
            <label for="startDate" style="color: black;">Start Date:</label>
            <input type="datetime-local" id="startDate" name="startDate" required><br><br>
            <label for="endDate" style="color: black;">End Date:</label>
            <input type="datetime-local" id="endDate" name="endDate" required><br><br>
            <label for="eventDescription" style="color: black;">Description:</label>
            <textarea id="eventDescription" name="eventDescription" required></textarea><br><br>
            <button type="submit">Save Event</button>
        </form>
    </div>
</div>

<!-- Link to external styles.css -->
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/styles.css">

<!-- Link to external script.js -->
<script src="{{ site.baseurl }}/assets/js/script.js"></script>
