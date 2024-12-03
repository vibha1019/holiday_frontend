---
layout: post
title: Clothes
permalink: /holiday/clothes/
author: Soni Dhenuva, Vibha Mandayam, Kushi Gade, Nora Ahadian, Spencer Lyons
comments: true
---

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

