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
  let currentMonth = new Date().getMonth();
  let currentYear = new Date().getFullYear();
  let events = [];

  document.addEventListener('DOMContentLoaded', function() {
      initializeCalendar();
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
          
          const eventOnDay = events.filter(event => new Date(event.date).getDate() === day);
          if (eventOnDay.length > 0) {
              dayCell.classList.add("event-day");
              const emoji = document.createElement("div");
              emoji.classList.add("event-emoji");
              emoji.textContent = "❗";
              dayCell.appendChild(emoji);
          }

          dayCell.addEventListener("click", () => {
              document.getElementById("startDate").value = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
          });
          
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
  function createGiftAnimation() {
    const gift = document.createElement("div");
    gift.textContent = "🎁";
    gift.style.position = "absolute";
    gift.style.fontSize = "40px";
    document.body.appendChild(gift);
    
    function animateGift() {
        let x = Math.random() * (window.innerWidth - 50);
        let y = Math.random() * (window.innerHeight - 50);
        gift.style.left = `${x}px`;
        gift.style.top = `${y}px`;
        gift.style.opacity = "1";
        gift.style.transform = "scale(1)";
        
        gift.animate([
            { transform: "translateX(-5px)" },
            { transform: "translateX(5px)" },
            { transform: "translateX(-5px)" }
        ], {
            duration: 500,
            iterations: 3
        });
        
        setTimeout(() => {
            gift.animate([
                { transform: "scale(1)" },
                { transform: "scale(0)" }
            ], {
                duration: 500,
                fill: "forwards"
            }).onfinish = animateGift;
        }, 1500);
    }
    
    animateGift();
}

createGiftAnimation();

</script>
