---
layout: post
title: Profile Settings
permalink: /profile
menu: nav/home.html
search_exclude: true
show_reading_time: false
---
<div class="profile-container">
 <div class="card">
   <form>
     <div>
       <label for="newUid">Enter New UID:</label>
       <input type="text" id="newUid" placeholder="New UID">
     </div>
     <div>
       <label for="newName">Enter New Name:</label>
       <input type="text" id="newName" placeholder="New Name">
     </div>
      <div>
       <label for="newPassword">Enter New Password:</label>
       <input type="text" id="newPassword" placeholder="New Password">
     </div>
     <br>
     <br>
     <label for="profilePicture" class="file-icon"> Upload Profile Picture <i class="fas fa-upload"></i> <!-- Replace this with your desired icon -->
     </label>
     <input type="file" id="profilePicture" accept="image/*" onchange="saveProfilePicture()">
     <div class="image-container" id="profileImageBox">
         <!-- Profile picture will be displayed here -->
     </div>
     <p id="profile-message" style="color: red;"></p>
   </form>
 </div>
</div>

<script type="module">
// Import fetchOptions from config.js
import {pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';
// Import functions from config.js
import { putUpdate, postUpdate, deleteData, logoutUser } from "{{site.baseurl}}/assets/js/api/profile.js";

// Function to update table with fetched data
function updateTableWithData(data) {
   const tableBody = document.getElementById('profileResult');
   tableBody.innerHTML = '';

   data.sections.forEach((section, index) => {
       const tr = document.createElement('tr');
       const themeCell = document.createElement('td');
       const nameCell = document.createElement('td');

       themeCell.textContent = section.theme;
       nameCell.textContent = section.name;

       const trashIcon = document.createElement('i');
       trashIcon.className = 'fas fa-trash-alt trash-icon';
       trashIcon.style.marginLeft = '10px';
       themeCell.appendChild(trashIcon);

       trashIcon.addEventListener('click', async function (event) {
           event.preventDefault();
           const URL = pythonURI + "/api/user/section";
           // Remove the row from the table
           tr.remove();

           const options = {
               URL,
               body: { sections: [section.theme] },
               message: 'profile-message',
           };

           try {
               await deleteData(options);
           } catch (error) {
               console.error('Error deleting section:', error.message);
               document.getElementById('profile-message').textContent = 'Error deleting section: ' + error.message;
           }
       });

      yearCell.classList.add('editable'); // Make year cell editable
      yearCell.innerHTML = `${section.year} <i class="fas fa-pencil-alt edit-icon" style="margin-left: 10px;"></i>`;

       // Make the year cell editable
       yearCell.addEventListener('click', function () {
           const input = document.createElement('input');
           input.type = 'text';
           input.value = section.year;
           input.className = 'edit-input';
           yearCell.innerHTML = '';
           yearCell.appendChild(input);

           input.focus();

           input.addEventListener('blur', async function () {
               const newYear = input.value;
               const URL = pythonURI + "/api/user/section";
               const options = {
                   URL,
                   body: { section: { theme: section.theme, year: newYear } },
                   message: 'profile-message',
               };

               try {
                   await putUpdate(options);
               } catch (error) {
                   console.error('Error updating year:', error.message);
                   document.getElementById('profile-message').textContent = 'Error updating year: ' + error.message;
               }

               yearCell.textContent = newYear;
           });

           input.addEventListener('keydown', function (event) {
               if (event.key === 'Enter') {
                   input.blur();
               }
           });
       });
       tr.appendChild(themeCell);
       tr.appendChild(nameCell);

       tableBody.appendChild(tr);
   });

}

// Function to fetch user profile data
async function fetchUserProfile() {
    const URL = pythonURI + "/api/id/pfp"; // Endpoint to fetch user profile data

    try {
        const response = await fetch(URL, fetchOptions);
        if (!response.ok) {
            throw new Error(`Failed to fetch user profile: ${response.status}`);
        }

        const profileData = await response.json();
        displayUserProfile(profileData);
    } catch (error) {
        console.error('Error fetching user profile:', error.message);
        // Handle error display or fallback mechanism
    }
}

// Function to display user profile data
function displayUserProfile(profileData) {
    const profileImageBox = document.getElementById('profileImageBox');
    if (profileData.pfp) {
        const img = document.createElement('img');
        img.src = `data:image/jpeg;base64,${profileData.pfp}`;
        img.alt = 'Profile Picture';
        profileImageBox.innerHTML = ''; // Clear existing content
        profileImageBox.appendChild(img); // Append new image element
    } else {
        profileImageBox.innerHTML = '<p>No profile picture available.</p>';
    }

    // Display other profile information as needed
    // Example: Update HTML elements with profileData.username, profileData.email
}

// Function to save profile picture
window.saveProfilePicture = async function () {

    const fileInput = document.getElementById('profilePicture');
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function() {
            const profileImageBox = document.getElementById('profileImageBox');
            profileImageBox.innerHTML = `<img src="${reader.result}" alt="Profile Picture">`;
        };
        reader.readAsDataURL(file);
    }

    if (!file) return;

    try {
        const base64String = await convertToBase64(file);
        await sendProfilePicture(base64String);
        console.log('Profile picture uploaded successfully!');

    } catch (error) {
        console.error('Error uploading profile picture:', error.message);
        // Handle error display or fallback mechanism
    }
}

// Function to convert file to base64
async function convertToBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result.split(',')[1]); // Remove the prefix part of the result
        reader.onerror = error => reject(error);
        reader.readAsDataURL(file);
    });
}

// Function to send profile picture to server
async function sendProfilePicture(base64String) {
   const URL = pythonURI + "/api/id/pfp"; // Adjust endpoint as needed

   // Create options object for PUT request
   const options = {
       URL,
       body: { pfp: base64String },
       message: 'profile-message', // Adjust the message area as needed
       callback: () => {
           console.log('Profile picture uploaded successfully!');
           // Handle success response as needed
       }
   };

   try {
       await putUpdate(options);
   } catch (error) {
       console.error('Error uploading profile picture:', error.message);
       document.getElementById('profile-message').textContent = 'Error uploading profile picture: ' + error.message;
   }
}
  // Function to update UI with new UID and change placeholder
window.updateUidField = function(newUid) {
  const uidInput = document.getElementById('newUid');
  uidInput.value = newUid;
  uidInput.placeholder = newUid;
}

// Function to update UI with new Name and change placeholder
window.updateNameField = function(newName) {
  const nameInput = document.getElementById('newName');
  nameInput.value = newName;
  nameInput.placeholder = newName;
}

// Function to change UID
window.changeUid = async function(uid) {
   if (uid) {
       const URL = pythonURI + "/api/user"; // Adjusted endpoint

       const options = {
           URL,
           body: { uid },
           message: 'uid-message', // Adjust the message area as needed
           callback: () => {
               alert("You updated your Github ID, so you will automatically be logged out. Be sure to remember your new github id to log in!");
               console.log('UID updated successfully!');
               window.updateUidField(uid);
               window.location.href = '/portfolio_2025/login'
           }
       };

       try {
           await putUpdate(options);
       } catch (error) {
           console.error('Error updating UID:', error.message);
           document.getElementById('uid-message').textContent = 'Error updating UID: ' + error.message;
       }
   }
}

window.changePassword = async function(password) {
   if (password) {
       const URL = pythonURI + "/api/user"; // Adjusted endpoint

       const options = {
           URL,
           body: { password },
           message: 'password-message', // Adjust the message area as needed
           callback: () => {
               console.log('Password updated successfully!');
               window.location.href = '/portfolio_2025/login'

           }
       };

       try {
            alert("You updated your password, so you will automatically be logged out. Be sure to remember your password!");
           await putUpdate(options);
           await logoutUser();
       } catch (error) {
           console.error('Error updating password:', error.message);
           document.getElementById('password-message').textContent = 'Error updating password: ' + error.message;
       }
   }
}

// Function to change Name
window.changeName = async function(name) {
   if (name) {
       const URL = pythonURI + "/api/user";
       const options = {
           URL,
           body: { name },
           message: 'name-message',
           callback: () => {
               console.log('Name updated successfully!');
               window.updateNameField(name);
           }
       };
       try {
           await putUpdate(options);
       } catch (error) {
           console.error('Error updating Name:', error.message);
           document.getElementById('name-message').textContent = 'Error updating Name: ' + error.message;
       }
   }
}

// Event listener to trigger updateUid function when UID field is changed
document.getElementById('newUid').addEventListener('change', function() {
    const uid = this.value;
    window.changeUid(uid);

});

// Event listener to trigger updateName function when Name field is changed
document.getElementById('newName').addEventListener('change', function() {
    const name = this.value;
    window.changeName(name);

});

document.getElementById('newPassword').addEventListener('change', function() {
    const password = this.value;
    window.changePassword(password);

});

// Function to fetch Name from backend
window.fetchName = async function() {
    const URL = pythonURI + "/api/user"; // Adjusted endpoint

    try {
        const response = await fetch(URL, fetchOptions);
        if (!response.ok) {
            throw new Error(`Failed to fetch Name: ${response.status}`);
        }

        const data = await response.json();
        return data.name;
    } catch (error) {
        console.error('Error fetching Name:', error.message);
        return null;
    }
};

// Function to set placeholders for UID and Name
window.setPlaceholders = async function() {
    const uidInput = document.getElementById('newUid');
    const nameInput = document.getElementById('newName');

    try {
        const uid = await window.fetchUid();
        const name = await window.fetchName();

        if (uid !== null) {
            uidInput.placeholder = uid;
        }
        if (name !== null) {
            nameInput.placeholder = name;
        }
    } catch (error) {
        console.error('Error setting placeholders:', error.message);
    }
};

// Call and initializeProfileSetup when DOM content is loaded
document.addEventListener('DOMContentLoaded', async function () {
    try {
        await fetchUserProfile(); // Fetch user profile data
        await setPlaceholders();
    } catch (error) {
        console.error('Initialization error:', error.message);
        // Handle initialization error gracefully
    }
});

</script>



<div class="main-content">
    <!-- Calendar on the left -->
    <div class="calendar-container">
        <div class="calendar-header">
            <button id="prev-month">&#10094;</button>
            <div class="month-year" id="month-year"></div>
            <button id="next-month">&#10095;</button>
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
        <h3 style="color: black; font-size: 24px; font-weight: bold;">Upcoming Events</h3>
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
  // Handle the form submission to create a new event
  document.getElementById("eventForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    const postData = {
        name: document.getElementById("eventName").value,
        location: document.getElementById("eventLocation").value,
        date: document.getElementById("startDate").value,  // This will be in YYYY-MM-DD format
    };
    console.log("Event Data:", postData);  // Log the event data to check before sending
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
        const createdEvent = await response.json(); // Assuming API returns the full event
        alert("Event added successfully!");
        // Ensure the event has an ID before pushing it to events
       // Ensure the event has an ID before pushing it to events
        if (createdEvent.id) {
            events.push(createdEvent); 
        } else {
            console.error("Error: Event created but no ID returned from API");
        }
        renderSidebar(events);
        renderCalendar(events);
        closeModal();
    });
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
                          renderSidebar(events);   // Pass events to the sidebar
                      })
                      .catch(err => console.error("Error fetching events: ", err));
              }
          })
          .catch(err => {
              console.error("Error fetching user ID: ", err);
          });
      // Attach event listeners for month navigation buttons
      document.getElementById('prev-month').addEventListener('click', function() {
          changeMonth(-1);  // Go to the previous month
      });
      document.getElementById('next-month').addEventListener('click', function() {
          changeMonth(1);   // Go to the next month
      });
  });
  // Function to delete an event
    async function deleteEvent(eventId) {
        try {
            const response = await fetch(`${pythonURI}/api/event/${eventId}`, {
                ...fetchOptions,
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' },
            });
            if (!response.ok) {
                const errorMessage = await response.text();
                throw new Error(`Failed to delete event: ${response.statusText} - ${errorMessage}`);
            }
            alert("Event deleted successfully!");
            events = events.filter(event => event.id !== eventId);  // Remove from local array
            renderSidebar(events);
            renderCalendar(events);
        } catch (error) {
            console.error('Error deleting event:', error.message);
            alert(`Error deleting event: ${error.message}`);
        }
    }
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
        if (events.some(event => event.date === eventDateString)) {
            const dot = document.createElement("span");
            dot.classList.add("event-dot");  // Add a class for styling blue dots
            dayCell.appendChild(dot);
        }
        dayCell.textContent = day;
        // When a day is clicked, open the modal and prefill the date
        dayCell.addEventListener("click", function() {
            openModal(day);
        });
        calendarDays.appendChild(dayCell);
    }
  }
  function renderSidebar(events) {
    const upcomingEventsContainer = document.getElementById("event-list");
    upcomingEventsContainer.innerHTML = "";  // Clear existing events
    const sortedEvents = events.slice().sort((a, b) => new Date(a.date) - new Date(b.date));
    sortedEvents.forEach(event => {
        const eventItem = document.createElement("div");
        eventItem.classList.add("event-item");
        eventItem.style.padding = "15px";
        eventItem.style.border = "1px solid #ddd";
        eventItem.style.marginBottom = "15px";
        eventItem.style.borderRadius = "8px";
        eventItem.style.backgroundColor = "#f9f9f9";
        // Event Name
        const eventName = document.createElement("div");
        eventName.classList.add("event-name");
        eventName.textContent = event.name;
        eventName.style.fontWeight = "bold";
        eventName.style.color = "black";
        // Event Location
        const eventLocation = document.createElement("div");
        eventLocation.classList.add("event-location");
        eventLocation.textContent = event.location;
        eventLocation.style.color = "black";
        // Event Date
        const eventDate = document.createElement("div");
        eventDate.classList.add("event-date");
        const eventDateObject = new Date(event.date);
        eventDate.textContent = eventDateObject.toLocaleDateString();
        eventDate.style.color = "black";
        // Delete Button
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.style.backgroundColor = "#ff4d4d";
        deleteButton.style.color = "white";
        deleteButton.style.border = "none";
        deleteButton.style.padding = "5px 10px";
        deleteButton.style.marginTop = "5px";
        deleteButton.style.cursor = "pointer";
        deleteButton.style.borderRadius = "5px";
        // Add event listener for delete action
        deleteButton.addEventListener("click", async () => {
            const confirmDelete = confirm(`Are you sure you want to delete "${event.name}"?`);
            if (confirmDelete) {
                await deleteEvent(event.id);
            }
        });
        eventItem.appendChild(eventName);
        eventItem.appendChild(eventLocation);
        eventItem.appendChild(eventDate);
        eventItem.appendChild(deleteButton);  // Append delete button
        upcomingEventsContainer.appendChild(eventItem);
    });
}
  function openModal(date) {
    document.getElementById("eventModal").style.display = "block";
    const currentYear = new Date().getFullYear(); // Keep current year constant
    const formattedDate = new Date(currentYear, currentMonth, date).toISOString().split('T')[0];
    document.getElementById("startDate").value = formattedDate;
}
  function closeModal() {
    document.getElementById("eventModal").style.display = "none";
    document.getElementById("eventForm").reset();
  }
  function changeMonth(direction) {
      currentMonth += direction;
      if (currentMonth < 0) currentMonth = 11;
      if (currentMonth > 11) currentMonth = 0;
      renderCalendar(events);  // Re-render the calendar with the updated month
  }
  window.addEventListener("click", function(event) {
    const modal = document.getElementById("eventModal");
    if (event.target === modal) {
        closeModal();
    }
});
</script>
