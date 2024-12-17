---
layout: post
title: Holiday
permalink: /holiday
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

<div class="holiday-page">
    <header class="holiday-header">
        <h1>🎁 Happy Holidays Gift List 🎄</h1>
    </header>
    <div class="categories-grid">
        <div class="category-box" id="home-decor">
            <h2>Home Decor</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/home-decor/'">Explore Home Decor</button>
        </div>
        <div class="category-box" id="food">
            <h2>Food</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/food/'">Explore Food</button>
        </div>
        <div class="category-box" id="clothes">
            <h2>Clothes</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/clothes/'">Explore Clothes</button>
        </div>
        <div class="category-box" id="scented">
            <h2>Scented Gifts</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/scented/'">Explore Scented Gifts</button>
        </div>
        <div class="category-box" id="electronics">
            <h2>Electronics</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/electronics/'">Explore Electronics</button>
        </div>
        <div class="category-box" id="toys">
            <h2>Toys</h2>
            <button onclick="location.href='{{ site.baseurl }}/holiday/toys/'">Explore Toys</button>
        </div>
    </div>
</div>

<style>
/* Reset margin and padding for the whole page */
html, body {
    margin: 0;
    padding: 0;
    width: 100%;
}

/* Apply the background image to the container */
.holiday-page {
    background-image: url('{{ site.baseurl }}/images/greenbackground.png');
    background-size: 100% auto; /* Ensure the image spans full width */
    background-position: center;
    background-attachment: fixed; /* Keeps background fixed on scroll */
    min-height: 100vh;
    width: 100vw; /* Full viewport width */
    margin: 0; /* Remove any margins */
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #ffffff;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
    position: relative; /* Ensures it's a stacking context */
}

/* Header Styles */
.holiday-header h1 {
    font-size: 2.5em;
    margin-bottom: 30px;
    text-align: center;
    background: rgba(0, 0, 0, 0.6);
    padding: 10px 20px;
    border-radius: 10px;
}

/* Grid Layout */
.categories-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    width: 90%;
    max-width: 1200px;
}

/* Category Box Styles */
.category-box {
    background: rgba(0, 0, 0, 0.6);
    border: 2px solid rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    text-align: center;
    padding: 20px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    z-index: 2; /* Ensures boxes appear above the background */
}

.category-box h2 {
    margin-bottom: 15px;
    font-size: 1.5em;
}

.category-box button {
    background: #ffffff;
    color: #008080;
    border: none;
    padding: 10px 15px;
    font-size: 1em;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s ease, color 0.2s ease;
}

.category-box button:hover {
    background: #008080;
    color: #ffffff;
}

/* Hover Effect */
.category-box:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
}

/* Responsive Design */
@media (max-width: 768px) {
    .categories-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    .holiday-header h1 {
        font-size: 2em;
    }
}

@media (max-width: 480px) {
    .categories-grid {
        grid-template-columns: 1fr;
    }
    .category-box h2 {
        font-size: 1.2em;
    }
}
</style>
