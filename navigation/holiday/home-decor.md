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

<!DOCTYPE html>
<html lang="en">
<script>
    /* General Page Styles */
    const style = document.createElement('style');
    style.innerHTML = `
        body {
            font-family: Arial, sans-serif;
            background: #111;
            color: #fff;
            margin: 0;
            padding: 0;
            text-align: center;
        }
        header h1 {
            font-size: 2.5em;
            margin: 20px 0;
            background: rgba(0, 0, 0, 0.6);
            padding: 10px 20px;
            border-radius: 10px;
        }
        .category-box {
            display: inline-block;
            width: 200px;
            margin: 20px;
            padding: 20px;
            background: #222;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .category-box:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
        }
        .category-box h2 {
            font-size: 1.5em;
            margin-bottom: 15px;
        }
        .category-box button {
            background: #fff;
            color: #000;
            border: 1px solid #555;
            padding: 10px 15px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }
        .category-box button:hover {
            background: #008080;
            color: #fff;
            border-color: #008080;
        }
        .product-list {
            display: none; 
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px auto;
            padding: 20px;
            max-width: 800px;
        }
        .product {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .product img {
            max-width: 100%;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .product h3 {
            font-size: 1.2em;
            color: #333;
        }
        .product p {
            font-size: 0.9em;
            color: #555;
        }
        .product:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }
        .active {
            display: grid;
        }
    `;
    document.head.appendChild(style);
</script>
<script>
    function toggleHomeDecorProducts() {
        const homeDecorProducts = document.getElementById("home-decor-products");
        if (homeDecorProducts.style.display === "none" || homeDecorProducts.style.display === "") {
            homeDecorProducts.style.display = "grid";
        } else {
            homeDecorProducts.style.display = "none";
        }
    }
</script>
<div>
    <header>
        <h1>🕯️ Explore Home Decor Gifts 🎄</h1>
    </header>
    <div class="category-box">
        <h2>Home Decor</h2>
        <button onclick="toggleHomeDecorProducts()">Explore Home Decor</button>
    </div>
    <div id="home-decor-products" class="product-list">
        <div class="product">
            <img src="{{site.baseurl}}/images/holiday candles.jpeg" alt="Holiday Candles">
            <h3>Holiday Candles</h3>
            <p>Beautiful scented candles for a cozy holiday atmosphere.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/festive wreath.jpeg" alt="Festive Wreath">
            <h3>Festive Wreath</h3>
            <p>A stunning wreath to brighten up your front door.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/decorative ornaments.jpeg" alt="Decorative Ornaments">
            <h3>Decorative Ornaments</h3>
            <p>Charming ornaments to add sparkle to your holiday decor.</p>
        </div>
    </div>
</div>
