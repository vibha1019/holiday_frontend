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
    // You can also pass the selected date to the form, for example, by default
    document.getElementById("startDate").value = date;
    document.getElementById("endDate").value = date; // Default end date same as start date
}

// Function to close the modal
function closeModal() {
    document.getElementById("eventModal").style.display = "none";
}

// Handle the form submission to create a new event
document.getElementById("eventForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const eventData = {
        name: document.getElementById("eventName").value,
        location: document.getElementById("eventLocation").value,
        start_date: document.getElementById("startDate").value,  // YYYY-MM-DD format
        end_date: document.getElementById("endDate").value,      // YYYY-MM-DD format
        description: document.getElementById("eventDescription").value // Add the description field
    };

    console.log("Event Data:", eventData);  // Log the event data to check before sending

    // Send the event data to your API endpoint
    fetch('http://127.0.0.1:8887/api/event', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem("token") // Adjust this if using JWT token
        },
        body: JSON.stringify(eventData)
    })
    .then(response => response.json())
    .then(data => {
        alert("Event created successfully!");
        closeModal();
        // Optionally refresh the calendar to show the new event
    })
    .catch(error => {
        console.error("Error creating event:", error);
        alert("Error creating event.");
    });
});

// When the page loads, assign the event listener to each day cell
document.addEventListener("DOMContentLoaded", function() {
    const days = document.querySelectorAll(".day");
    days.forEach(day => {
        day.addEventListener("click", function() {
            const selectedDate = day.textContent; // Use textContent for day
            openModal(selectedDate);
        });
    });
});
