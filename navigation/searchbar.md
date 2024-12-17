---
layout: post
title: searchbar
permalink: /searchbar
---
<div style="font-family: Arial, sans-serif; margin: 0; padding: 0;">
    <!-- Search Section -->
    <div class="content">
        <div class="container">
            <h1 class="title" style="color: darkred;">Find Your Holiday Gifts 🎁</h1>
            <div class="search-bar">
                <input 
                    type="text" 
                    id="searchInput" 
                    placeholder="Search for an item..." 
                    oninput="searchItems()"
                >
            </div>
            <div id="results"></div>
        </div>
    </div>
</div>

<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: white;
    }
    
    /* Content Section */
    .content {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 90vh;
    }
    .container {
        width: 100%;
        max-width: 600px;
        padding: 30px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        border-radius: 12px;
        background-color: white;
        text-align: center;
    }
    .title {
        font-size: 28px;
        color: darkred;
        margin-bottom: 20px;
    }
    .search-bar {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    #searchInput {
        width: 100%;
        padding: 12px;
        border: 2px solid #ddd;
        border-radius: 25px;
        font-size: 16px;
        box-sizing: border-box;
        outline: none;
        transition: border-color 0.3s, box-shadow 0.3s;
    }
    #searchInput:focus {
        border-color: green;
        box-shadow: 0 0 10px rgba(255, 255, 0, 0.5);
    }
    #results {
        margin-top: 20px;
        text-align: left;
        max-height: 300px;
        overflow-y: auto;
    }
    .result {
        margin: 5px 0;
        padding: 10px 15px;
        background: green;
        color: white;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.2s;
    }
    .result:hover {
        background: darkred;
        transform: translateY(-2px);
    }
</style>

<script>
    var items = [
        { name: "Teddy Bear", link: "holiday/toys", tags: ["all","teddy","bear","toys"] },   
        { name: "Lego Set", link: "holiday/toys", tags: ["all", "lego", "set", "toys"] },
        { name: "Remote Control Car", link: "holiday/toys", tags: ["all","remote","control","car", "toys"] },
        { name: "Holiday Candles", link: "holiday/home-decor", tags: ["all","holiday","candles","home-decor"]},
        { name: "Festive Wreath", link: "holiday/home-decor", tags: ["all","festive","wreath","home-decor"] },
        { name: "Decorative Ornaments", link: "holiday/home-decor", tags: ["all","decorative","ornaments","home-decor"] },
        { name: "Wireless Headphones", link: "holiday/electronics", tags: ["all","wireless","headphones","electronics"]},
        { name: "Smartwatch", link: "holiday/electronics", tags: ["all","smartwatch", "electronics"] },
        { name: "Gaming Console", link: "holiday/electronics", tags: ["all","gaming","console", "electronics"] },
        { name: "Cozy Holiday Sweater", link: "holiday/clothes", tags: ["all","cozy","holiday","sweater","clothes"] },
        { name: "Woolen Scarf", link: "holiday/clothes", tags: ["all","woolen","scarf","clothes"] },
        { name: "Winter Gloves", link: "holiday/clothes", tags: ["all","winter","gloves","clothes"] },
        { name: "Holiday Cookies", link: "holiday/food", tags: ["all","holiday","cookies","food"] },
        { name: "Chocolate Gift Box", link: "holiday/food", tags: ["all","chocolate","gift","box","food"] },
        { name: "Gourmet Cheese Set", link: "holiday/food", tags: ["all","gourmet","cheese","set", "food"]},
        { name: "Scented Candle", link: "holiday/scented", tags: ["all", "candle","scented"] },
        { name: "Aromatic Diffuser", link: "holiday/scented", tags: ["all","aromatic","diffuser","scented"] },
        { name: "Perfume Gift Set", link: "holiday/scented", tags: ["all","perfume","gift","set","scented"] }
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
                    resultDiv.onclick = () => {
                        window.location.href = item.link;
                    };
                    resultsDiv.appendChild(resultDiv);
                }
            });
        }
    }
</script>