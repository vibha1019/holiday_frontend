---
layout: post
title: Electronics
permalink: /holiday/electronics/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Electronics Gifts</title>
    <style>
        /* General Page Styles */
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
        /* Category Box Styles */
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
        /* Product List */
        .product-list {
            display: none; /* Hidden by default */
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
        /* Show Active Product List */
        .active {
            display: grid;
        }
    </style>
</head>
<body>
    <header>
        <h1>🎁 Explore Electronics Gifts 🎄</h1>
    </header>
    <!-- Electronics Category -->
    <div class="category-box">
        <h2>Electronics</h2>
        <button onclick="toggleElectronicsProducts()">Explore Electronics</button>
    </div>
    <!-- Electronics Products -->
    <div id="electronics-products" class="product-list">
        <div class="product">
            <img src="{{site.baseurl}}/images/wireless headphones.jpeg" alt="Wireless Headphones">
            <h3>Wireless Headphones</h3>
            <p>High-quality noise-cancelling headphones for music lovers.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/smartwatch.jpeg" alt="Smartwatch">
            <h3>Smartwatch</h3>
            <p>Stay connected with the latest smartwatch technology.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/gaming console.jpeg" alt="Gaming Console">
            <h3>Gaming Console</h3>
            <p>The perfect gift for gamers with the latest hardware.</p>
        </div>
    </div>
    <!-- JavaScript -->
    <script>
        function toggleElectronicsProducts() {
            const electronicsProducts = document.getElementById("electronics-products");
            if (electronicsProducts.style.display === "none" || electronicsProducts.style.display === "") {
                electronicsProducts.style.display = "grid";
            } else {
                electronicsProducts.style.display = "none";
            }
        }
    </script>
</body>
</html>
