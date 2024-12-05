---
layout: post
title: Clothes
permalink: /holiday/clothes/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clothes Gifts</title>
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
        <h1>👗 Explore Clothes Gifts 🎄</h1>
    </header>
    <!-- Clothes Category -->
    <div class="category-box">
        <h2>Clothes</h2>
        <button onclick="toggleClothesProducts()">Explore Clothes</button>
    </div>
    <!-- Clothes Products -->
    <div id="clothes-products" class="product-list">
        <div class="product">
            <img src="{{site.baseurl}}/images/holiday sweater.jpeg" alt="Cozy Holiday Sweater">
            <h3>Cozy Holiday Sweater</h3>
            <p>Warm and festive sweater perfect for the holiday season.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/wool scarf.jpeg" alt="Woolen Scarf">
            <h3>Woolen Scarf</h3>
            <p>Soft and stylish scarf to keep you warm and chic.</p>
        </div>
        <div class="product">
            <img src="{{site.baseurl}}/images/winter gloves.jpeg" alt="Winter Gloves">
            <h3>Winter Gloves</h3>
            <p>Comfortable and warm gloves, ideal for chilly weather.</p>
        </div>
    </div>
    <!-- JavaScript -->
    <script>
        function toggleClothesProducts() {
            const clothesProducts = document.getElementById("clothes-products");
            if (clothesProducts.style.display === "none" || clothesProducts.style.display === "") {
                clothesProducts.style.display = "grid";
            } else {
                clothesProducts.style.display = "none";
            }
        }
    </script>
</body>
</html>


<html>
    <style>
        /* Styling for the button */
        button {
            padding: 10px 20px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        /* Styling for the post area */
        #postArea {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #ccc;
            background-color: #f8f9fa;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            font-family: monospace;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
    <button onclick="addPost()">Add Post</button>
    <div id="postArea">
        <p id="placeholder"></p>
    </div>
    <script>
        function addPost() {
            // Get the post area and replace its content with a code input area
            const postArea = document.getElementById('postArea');
            postArea.innerHTML = `
                <textarea placeholder="Write your code here..."></textarea>
                <button onclick="savePost()">Save Post</button>
            `;
        }
        function savePost() {
            const textarea = document.querySelector('#postArea textarea');
            const codeContent = textarea.value;
            // Replace the textarea with the submitted code content
            const postArea = document.getElementById('postArea');
            postArea.innerHTML = `
                <pre style="background-color: #f1f1f1; padding: 10px; border: 1px solid #ccc; border-radius: 5px;">${codeContent}</pre>
            `;
        }
    </script>

