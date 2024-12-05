---
layout: post
title: home-decor
permalink: /holiday/home-decor/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

<!-- New Post Form (shown by default) -->
<div class="post-form-container" id="post-form">
  <h2>Post Review</h2>
  <form id="postForm">
    <label for="title">Item Name:</label>
    <input type="text" id="title" name="title" required>
    <p></p>
    <label for="comment">Comment:</label>
    <textarea id="comment" name="comment" required>
Quality:
Usefulness:
</textarea>
    <p></p>

    <!-- Star Rating Section -->
    <label for="star-rating">Rating:</label>
    <div id="star-rating" class="star-rating">
      <span class="star" data-value="1">&#9733;</span>
      <span class="star" data-value="2">&#9733;</span>
      <span class="star" data-value="3">&#9733;</span>
      <span class="star" data-value="4">&#9733;</span>
      <span class="star" data-value="5">&#9733;</span>
    </div>
    <input type="hidden" id="star-rating-value" name="star-rating" value="0" />
    <p></p>

    <!-- Age Range Dropdown -->
    <label for="channel-select">Age Range:</label>
    <select id="channel-select" name="channel">
      <option value="1">Teenage Girls (11-15)</option>
      <option value="2">Teenage Boys (11-15)</option>
      <option value="3">Toddlers</option>
      <option value="4">Adults</option>
    </select>
    <p></p>

    <button type="submit">Add Post</button>
  </form>
</div>

<!-- Embedded JavaScript -->
<script>
  // Handle star rating clicks
  const stars = document.querySelectorAll('.star');
  const ratingValueInput = document.getElementById('star-rating-value');

  stars.forEach(star => {
    star.addEventListener('click', function () {
      const rating = this.getAttribute('data-value');
      // Set the value in the hidden input field
      ratingValueInput.value = rating;

      // Update the star colors based on rating
      stars.forEach(star => {
        star.style.color = (star.getAttribute('data-value') <= rating) ? 'gold' : 'gray';
      });
    });
  });

  // Handle form submission
  document.getElementById('postForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const title = document.getElementById('title').value;
    const comment = document.getElementById('comment').value;
    const channel_id = document.getElementById('channel-select').value; // Get the selected value for age range
    const starRating = ratingValueInput.value; // Get the star rating value

    // Prepare the data to be sent to the backend
    const postData = {
      title: title,
      comment: comment,
      channel_id: channel_id,
      star_rating: starRating
    };

    try {
      const response = await fetch(`${pythonURI}/api/post`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
      });

      if (!response.ok) throw new Error('Failed to add post: ' + response.statusText);
      alert("Post added successfully!");

    } catch (error) {
      console.error('Error adding post:', error);
    }
  });
</script>

<style>
  /* General Post Form Styling */
  .post-form-container {
    background-color: #13292b;
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
    color: #ffffff;
  }

  .post-form-container h2 {
    font-size: 1.8em;
    text-align: center;
    color: #ffd700; /* Gold color */
  }

  .post-form-container label {
    display: block;
    margin-bottom: 8px;
    font-size: 1.1em;
  }

  .post-form-container input,
  .post-form-container textarea,
  .post-form-container select {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
    border: 1px solid #ccc;
    background-color: #f4f4f4;
  }

  .post-form-container button {
    background-color: #ffd700;
    color: #13292b;
    padding: 12px 20px;
    font-size: 1.2em;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    border: none;
  }

  .post-form-container button:hover {
    background-color: #ffcc00;
  }

  /* Styling for star rating */
  .star-rating {
    font-size: 2em;
    cursor: pointer;
    color: gray; /* Default color */
  }

  .star {
    padding: 0 5px;
    transition: color 0.3s ease;
  }
</style>
