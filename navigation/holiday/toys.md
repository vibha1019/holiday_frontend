---
layout: post
title: Toys
permalink: /holiday/toys/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toy Gifts</title>
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
        <h1>🧸 Explore Toy Gifts 🎁</h1>
    </header>
    <!-- Toys Category -->
    <div class="category-box">
        <h2>Toys</h2>
        <button onclick="toggleToyProducts()">Explore Toys</button>
    </div>
    <!-- Toy Products -->
    <div id="toy-products" class="product-list">
        <div class="product">
            <img src="{{site.baseurl}}/images/teddybear.jpeg" alt="Teddy Bear">
            <h3>Teddy Bear</h3>
            <p>A cuddly plush bear, perfect for kids of all ages.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/lego set.jpeg" alt="LEGO Set">
            <h3>Lego Set</h3>
            <p>A creative building set for endless fun.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/remote control car.jpeg" alt="Remote Control Car">
            <h3>Remote Control Car</h3>
            <p>An exciting toy for racing enthusiasts.</p>
        </div>
    </div>
    <!-- JavaScript -->
    <script>
        function toggleToyProducts() {
            const toyProducts = document.getElementById("toy-products");
            if (toyProducts.style.display === "none" || toyProducts.style.display === "") {
                toyProducts.style.display = "grid";
            } else {
                toyProducts.style.display = "none";
            }
        }
    </script>
</body>
</html>