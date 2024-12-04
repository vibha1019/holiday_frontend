---
layout: post
title: home-decor
permalink: /holiday/home-decor/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

<!-- Button to trigger the form display -->
<button id="showFormButton">Create a Post</button>

<!-- New Post Form (hidden initially) -->
<div class="post-form-container" id="post-form" style="display: none;">
  <h2>Create a Post</h2>
  <form id="postForm">
    <label for="title">Gift Recommendation Title:</label>
    <input type="text" id="title" name="title" required>
    <p></p>
    <label for="comment">Comment:</label>
    <textarea id="comment" name="comment" required></textarea>
    <!-- Dropdown for Age Range Selection -->
    <label for="age-range-select">Age Range:</label>
    <select id="age-range-select" name="age-range">
      <option value="Teenage Girls">Teenage Girls (11-15)</option>
      <option value="Teenage Boys">Teenage Boys (11-15)</option>
      <option value="Toddlers">Toddlers</option>
      <option value="Adults">Adults</option>
    </select>
    <button type="submit">Add Post</button>
  </form>
</div>

<!-- Embedded JavaScript -->
<script>
  document.getElementById('showFormButton').addEventListener('click', function() {
    const formContainer = document.getElementById('post-form');
    formContainer.style.display = 'block';  // Show the form
  });
</script>
