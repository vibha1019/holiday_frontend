---
layout: post
title: recommended
permalink: /recommended
comments: true
---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Recommendations</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 1rem;
      background-color: #f5f5f5;
      line-height: 1.6;
    }
    .recommendations-content {
      padding: 1rem;
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .recommendations-content h1 {
      color: #333;
    }
    .recommendations-content a {
      color: #007bff;
      text-decoration: none;
    }
    .recommendations-content a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <h1>Recommendations</h1>
  <div class="recommendations-content" id="recommendations"></div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      fetch('/tri2/socialmedia_backend_fork/api/recommend.js')
        .then(response => response.text())
        .then(markdown => {
          // Parse and render Markdown
          const markdownParser = (markdown) => {
            return markdown
              .replace(/^# (.+)/gm, '<h1>$1</h1>')
              .replace(/- \*\*(.+?)\*\*\((.+?)\): (.+)/g, '<p>- <a href="$2"><strong>$1</strong></a>: $3</p>')
              .replace(/_(.+?)_/g, '<em>$1</em>');
          };
          document.getElementById('recommendations').innerHTML = markdownParser(markdown);
        })
        .catch(error => {
          console.error('Error fetching recommendations:', error);
          document.getElementById('recommendations').textContent = 'Failed to load recommendations.';
        });
    });
  </script>
</body>
</html>