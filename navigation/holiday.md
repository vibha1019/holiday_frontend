---
layout: post
title: Holiday
permalink: /holiday
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

<body>
    <header>
        <h1>✨ Holiday Season Gifts</h1>
    </header>

  <div class="holiday-page">
    <header class="holiday-header">
        <h1>🎁 Happy Holidays Gift List 🎄</h1>
    </header>

    <main class="categories">
        <div class="category-box" id="home-decor">
            <h2>Home Decor</h2>
            <button onclick="location.href='home-decor.html'">Explore Home Decor</button>
        </div>
        <div class="category-box" id="food">
            <h2>Food</h2>
            <button onclick="location.href='food.html'">Explore Food</button>
        </div>
        <div class="category-box" id="clothes">
            <h2>Clothes</h2>
            <button onclick="location.href='clothes.html'">Explore Clothes</button>
        </div>
        <div class="category-box" id="fragrance">
            <h2>Fragrance</h2>
            <button onclick="location.href='fragrance.html'">Explore Fragrance</button>
        </div>
        <div class="category-box" id="electronics">
            <h2>Electronics</h2>
            <button onclick="location.href='electronics.html'">Explore Electronics</button>
        </div>
        <div class="category-box" id="jewelry">
            <h2>Jewelry</h2>
            <button onclick="location.href='jewelry.html'">Explore Jewelry</button>
        </div>
    </main>
</div>

<style>
/* General Page Styles */
.holiday-page {
    background: url('https://images.unsplash.com/photo-1609259122465-e79f1c86c916?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80') no-repeat center center fixed;
    background-size: cover;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    color: #ffffff;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
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

/* Category Grid Styles */
.categories {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    width: 100%;
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
    .holiday-header h1 {
        font-size: 2em;
    }

    .category-box h2 {
        font-size: 1.2em;
    }

    .category-box button {
        font-size: 0.9em;
    }
}
</style>

<div class="custom-background">
    <h1>Welcome to the Holiday Gift List 🎁</h1>
</div>
