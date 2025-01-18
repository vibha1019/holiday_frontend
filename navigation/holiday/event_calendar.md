---
layout: post
title: Event Calendar
permalink: /holiday/event_calendar/
author: Vibha Mandayam
comments: true
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Calendar</title>
    <link rel="stylesheet" href="{{ site.baseurl }}/assets/css/styles.css">
</head>
<body>
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

    <script src="{{ site.baseurl }}/assets/js/script.js"></script>
</body>
</html>
