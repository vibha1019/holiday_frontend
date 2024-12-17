---
layout: post
title: Clothes
permalink: /holiday/clothes/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---
<html lang="en">
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
        button {
            background: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            font-size: 1em;
            border-radius: 5px;
            cursor: pointer;
            transition: all 0.3s;
        }
        button:hover {
            background: #218838;
        }
        /* Product List */
        .product-list {
            display: none; /* Initially hidden */
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
        .like, .dislike {
            font-size: 1.5em;
            cursor: pointer;
            user-select: none;
            transition: color 0.3s;
        }
        .like { color: black; }
        .like.active { color: red; }
        .dislike { color: black; }
        .dislike.active { color: yellow; }
        .reaction-count {
            font-size: 0.9em;
            color: #333;
        }
        /* Show Active Product List */
        .active {
            display: grid;
        }
    </style>
    <header>
        <h1>👗 Explore Clothes Gifts 🎄</h1>
    </header>
    <!-- Clothes Category -->
    <div class="category-box">
        <h2>Clothes</h2>
        <button onclick="toggleProductList()">Explore Clothes</button>
    </div>
    <!-- Product List -->
    <div id="product-list" class="product-list">
        <div class="product" data-item="Holiday Sweater">
            <img src="{{site.baseurl}}/images/holiday sweater.jpeg" alt="Holiday Sweater">
            <h3>Holiday Sweater</h3>
            <span class="like" onclick="toggleReaction(this, 'like')">❤</span>
            <span class="reaction-count like-count">0</span>
            <span class="dislike" onclick="toggleReaction(this, 'dislike')">👎</span>
            <span class="reaction-count dislike-count">0</span>
        </div>
        <div class="product" data-item="Winter Scarf">
            <img src="{{site.baseurl}}/images/Winter Scarf.jpeg" alt="Winter Scarf">
            <h3>Winter Scarf</h3>
            <span class="like" onclick="toggleReaction(this, 'like')">❤</span>
            <span class="reaction-count like-count">0</span>
            <span class="dislike" onclick="toggleReaction(this, 'dislike')">👎</span>
            <span class="reaction-count dislike-count">0</span>
        </div>
        <div class="product" data-item="Beanie Hat">
            <img src="{{site.baseurl}}/images/Winter Beanie.jpeg" alt="Beanie Hat">
            <h3>Beanie Hat</h3>
            <span class="like" onclick="toggleReaction(this, 'like')">❤</span>
            <span class="reaction-count like-count">0</span>
            <span class="dislike" onclick="toggleReaction(this, 'dislike')">👎</span>
            <span class="reaction-count dislike-count">0</span>
        </div>
    </div>
    <script>
        // Function to toggle product list visibility
        function toggleProductList() {
            const productList = document.getElementById('product-list');
            productList.classList.toggle('active');
        }
        // Like/Dislike functionality
        const likesData = {};
        function toggleReaction(element, reactionType) {
            const productElement = element.closest('.product');
            const productName = productElement.getAttribute('data-item');
            if (!likesData[productName]) {
                likesData[productName] = { likes: 0, dislikes: 0 };
            }
            const isActive = element.classList.contains('active');
            const likeCountElement = productElement.querySelector('.like-count');
            const dislikeCountElement = productElement.querySelector('.dislike-count');
            if (reactionType === 'like') {
                if (isActive) {
                    likesData[productName].likes--;
                    element.classList.remove('active');
                } else {
                    likesData[productName].likes++;
                    element.classList.add('active');
                    productElement.querySelector('.dislike').classList.remove('active');
                    likesData[productName].dislikes = Math.max(0, likesData[productName].dislikes - 1);
                }
            } else if (reactionType === 'dislike') {
                if (isActive) {
                    likesData[productName].dislikes--;
                    element.classList.remove('active');
                } else {
                    likesData[productName].dislikes++;
                    element.classList.add('active');
                    productElement.querySelector('.like').classList.remove('active');
                    likesData[productName].likes = Math.max(0, likesData[productName].likes - 1);
                }
            }
            likeCountElement.textContent = likesData[productName].likes;
            dislikeCountElement.textContent = likesData[productName].dislikes;
            console.log(`Updated reactions for ${productName}:`, likesData[productName]);
        }
    </script>
</html>
       