---
layout: post
title: Survey
permalink: /holiday/survey/
author: Soni Dhenuva
comments: true
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Review Survey</title>
    <style>
        .popup {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            z-index: 1000;
        }
        .survey-box {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ddd;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
            position: relative;
        }
        .edit-button, .delete-button {
            position: absolute;
            top: 5px;
            cursor: pointer;
            font-size: 14px;
            border: none;
            border-radius: 5px;
            padding: 5px;
        }
        .edit-button { right: 40px; background: blue; color: white; }
        .delete-button { right: 10px; background: red; color: white; }
    </style>
</head>
<body>
    <div id="survey-list"></div>
    <div id="edit-popup" class="popup">
        <h2>Edit Review</h2>
        <textarea id="edit-text"></textarea>
        <button id="save-edit">Save</button>
    </div>
    <script type="module">
        import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
        let currentEditId = null;
        async function fetchSurveys() {
            const response = await fetch(`${pythonURI}/api/surveys`, { ...fetchOptions, method: 'GET' });
            if (!response.ok) return alert("Failed to fetch surveys.");
            const surveys = await response.json();
            const surveyList = document.getElementById("survey-list");
            surveyList.innerHTML = '';
            surveys.forEach(survey => {
                const surveyBox = document.createElement('div');
                surveyBox.classList.add('survey-box');
                surveyBox.setAttribute('data-id', survey.id);
                const editButton = document.createElement('button');
                editButton.textContent = "Edit";
                editButton.classList.add('edit-button');
                editButton.addEventListener("click", () => openEditPopup(survey.id, survey.message));
                const deleteButton = document.createElement('button');
                deleteButton.textContent = "X";
                deleteButton.classList.add('delete-button');
                deleteButton.addEventListener("click", () => deleteSurvey(survey.id));
                const reviewContent = document.createElement('div');
                reviewContent.textContent = survey.message;
                surveyBox.appendChild(editButton);
                surveyBox.appendChild(deleteButton);
                surveyBox.appendChild(reviewContent);
                surveyList.appendChild(surveyBox);
            });
        }
        async function deleteSurvey(surveyId) {
            const response = await fetch(`${pythonURI}/api/survey?id=${surveyId}`, { ...fetchOptions, method: 'DELETE' });
            if (response.ok) {
                alert("Survey deleted successfully!");
                fetchSurveys();
            } else {
                alert("Failed to delete survey.");
            }
        }
        function openEditPopup(id, message) {
            currentEditId = id;
            document.getElementById("edit-text").value = message;
            document.getElementById("edit-popup").style.display = "block";
        }
        document.getElementById("save-edit").addEventListener("click", async function () {
            const newMessage = document.getElementById("edit-text").value;
            if (!currentEditId || newMessage.trim() === "") return alert("Invalid input");
            const response = await fetch(`${pythonURI}/api/survey?id=${currentEditId}`, {
                ...fetchOptions,
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: newMessage })
            });
            if (response.ok) {
                alert("Survey updated successfully!");
                document.getElementById("edit-popup").style.display = "none";
                fetchSurveys();
            } else {
                alert("Failed to update survey.");
            }
        })
        window.onload = fetchSurveys;
    </script>
</body>
</html>
