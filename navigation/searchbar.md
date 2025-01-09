---
layout: post
title: searchbar
permalink: /searchbar
---
<div style="font-family: Arial, sans-serif; margin: 0; padding: 0;">
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
    async function getCredentials() {
    try {
        const response = await fetch('http://127.0.0.1:8887/api/id', {
            method: 'GET',
            credentials: 'include', // Include credentials like cookies
        });
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Fetched credentials:', data);
    } catch (error) {
        console.error('Fetch error: ', error);
    }
}
// Example usage when an item is clicked
document.addEventListener('click', () => {
    getCredentials();
});
    async function searchItems() {
        const input = document.getElementById('searchInput').value.trim().toLowerCase();
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = ''; // Clear previous results
        if (input) {
            try {
                const response = await fetch(`http://127.0.0.1:8887/search?q=${encodeURIComponent(input)}`, { method: 'GET' });
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const items = await response.json();
                if (items.length > 0) {
                    items.forEach(item => {
                        const resultDiv = document.createElement('div');
                        resultDiv.className = 'result';
                        resultDiv.textContent = item.name;
                        resultDiv.onclick = () => {
                            window.location.href = item.link; // Redirect to item's link
                        };
                        resultsDiv.appendChild(resultDiv);
                    });
                } else {
                    resultsDiv.textContent = 'No results found.';
                }
            } catch (error) {
                console.error('Error fetching search results:', error);
                resultsDiv.textContent = 'An error occurred while searching. Please try again.';
            }
        }
    }
    // Attach function to global scope
    window.searchItems = searchItems;
</script>
