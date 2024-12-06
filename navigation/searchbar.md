---
layout: post
title: searchbar
permalink: /searchbar
---
<head>
    <title>Search Bar with Clickable Links</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            width: 100%;
            max-width: 600px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        .search-bar {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        #searchInput {
            width: 100%;
            padding: 15px;
            border: 2px solid #ccc;
            border-radius: 25px;
            font-size: 18px;
            box-sizing: border-box;
            outline: none;
            transition: border-color 0.3s;
        }
        #searchInput:focus {
            border-color: #000000;
        }
        #results {
            margin-top: 20px;
            width: 100%;
        }
        .result {
            margin: 5px 0;
            padding: 10px 15px;
            background: #000000;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .result:hover {
            background: #0e1e6e;
        }
    </style>
<div class="container">
    <div class="search-bar">
        <input type="text" id="searchInput" placeholder="Search for an item..." oninput="searchItems()">
    </div>
    <div id="results"></div>
</div>
<script>
    const items = [
        { name: "Teddy Bear", link: "holiday/toys" },
        { name: "Lego Set", link: "holiday/toys" },
        { name: "Remote Control Car", link: "holiday/toys" },
        { name: "Holiday Candles", link: "holiday/home-decor" },
        { name: "Festive Wreath", link: "holiday/home-decor" },
        { name: "Decorative Ornaments", link: "holiday/home-decor" },
        { name: "Wireless Headphones", link: "holiday/electronics" },
        { name: "Smartwatch", link: "holiday/electronics" },
        { name: "Gaming Console", link: "holiday/electronics" },
        { name: "Cozy Holiday Sweater", link: "holiday/clothes" },
        { name: "Woolen Scarf", link: "holiday/clothes" },
        { name: "Winter Gloves", link: "holiday/clothes" },
        { name: "Holiday Cookies", link: "holiday/food" },
        { name: "Chocolate Gift Box", link: "holiday/food" },
        { name: "Gourmet Cheese Set", link: "holiday/food" },
        { name: "Scented Candle", link: "holiday/scented" },
        { name: "Aromatic Diffuser", link: "holiday/scented" },
        { name: "Perfume Gift Set", link: "holiday/scented" }
    ];
    function searchItems() {
        const input = document.getElementById('searchInput').value.toLowerCase();
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = ''; // Clear previous results
        if (input.trim() !== "") {
            items.forEach(item => {
                if (item.name.toLowerCase().includes(input)) {
                    const resultDiv = document.createElement('div');
                    resultDiv.className = 'result';
                    resultDiv.textContent = item.name;
                    resultDiv.onclick = () => window.location.href = item.link;
                    resultsDiv.appendChild(resultDiv);
                }
            });
        }
    }
</script>
