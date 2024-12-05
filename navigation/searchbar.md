---
layout: post
title: searchbar
permalink: /searchbar
---
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
            background-color: #f8f9fa;
        }
        .container {
            width: 100%;
            max-width: 600px;
            padding: 20px;
            background: white;
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
            border-color: #007bff;
        }
        #results {
            margin-top: 20px;
            width: 100%;
        }
        .result {
            margin: 5px 0;
            padding: 10px 15px;
            background: #e9ecef;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .result:hover {
            background: #dee2e6;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="search-bar">
            <input type="text" id="searchInput" placeholder="Search for an item..." oninput="searchItems()">
        </div>
        <div id="results"></div>
    </div>
    <script>
        const items = [
            { name: "Teddy Bear", link: "item.link" },
            { name: "Lego Set", link: "item.link" },
            { name: "Remote Control Car", link: "item.link" },
            { name: "Holiday Candles", link: "item.link" },
            { name: "Festive Wreath", link: "item.link" },
            { name: "Decorative Ornaments", link: "item.link" },
            { name: "Wireless Headphones", link: "item.link" },
            { name: "Smartwatch", link: "item.link" },
            { name: "Gaming Console", link: "item.link" },
            { name: "Cozy Holiday Sweater", link: "item.link" },
            { name: "Woolen Scarf", link: "item.link" },
            { name: "Winter Gloves", link: "item.link" },
            { name: "Holiday Cookies", link: "item.link" },
            { name: "Chocolate Gift Box", link: "item.link" },
            { name: "Gourmet Cheese Set", link: "item.link" },
            { name: "Scented Candle", link: "item.link" },
            { name: "Aromatic Diffuser", link: "item.link" },
            { name: "Perfume Gift Set", link: "item.link" }
        ];
        function searchItems() {
            const input = document.getElementById('searchInput').value.toLowerCase();
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = ''; // Clear previous results
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
    </script>
</body>
</html>
