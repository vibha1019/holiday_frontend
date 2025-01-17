---
layout: post
title: Profile Page
permalink: /profile
comments: true
---

<div id="data">
    <!-- This is where the JSON data will be inserted -->
</div>
<div id="output"></div>

<script>
    let Database;
    fetch('/socialmedia_backend_fork/Database.json')
        .then(response => response.json())
        .then(data => {
            Database = data;
            console.log('Stored Data:', Database);
        })
        .catch(error => console.error('Error fetching JSON:', error));
    const text = `Game Name: ${Database[0].username}, Genre: ${Database[0].password}`;
    document.getElementById('output').textContent = text;
</script>
