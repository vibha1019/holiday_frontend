---
layout: post
title: Event Calendar
permalink: /holiday/event_calendar/
author: Vibha Mandayam
comments: true
---

<div id="calendar"></div>

<!-- Include FullCalendar CSS -->
<link href="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.7/main.min.css" rel="stylesheet" />

<!-- Include FullCalendar JS -->
<script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.7/main.min.js"></script>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      events: async function(fetchInfo, successCallback, failureCallback) {
        try {
          const response = await fetch('/api/events'); // Replace with your API endpoint
          const events = await response.json();
          // Transform events into FullCalendar format
          const formattedEvents = events.map(event => ({
            id: event.event_id,
            title: event.name,
            start: event.start_date,
            end: event.end_date
          }));
          successCallback(formattedEvents);
        } catch (error) {
          failureCallback(error);
        }
      }
    });
    calendar.render();
  });
</script>
