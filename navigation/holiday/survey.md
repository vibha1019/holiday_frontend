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
        #review-button {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 10px 15px;
            background-color: rgb(15, 99, 128) !important;
            color: black;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        #review-button:hover {
            background-color: #008080 !important;
        }
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
        .popup-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        textarea {
            width: 100%;
            height: 80px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            resize: none;
            color: black;
        }
        #submit-review {
            margin-top: 10px;
            padding: 10px 15px;
            background-color: #008080 !important;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        #submit-review:hover {
            background-color: #005f5f;
        }
        .survey-box {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ddd;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
            color: black;
            font-size: 16px;
            height: 150px;
            width: 30%;
            position: relative;
        }
        .delete-button {
            position: absolute;
            top: 5px;
            right: 10px;
            background: red;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 14px;
            border-radius: 5px;
            padding: 5px;
        }
        .delete-button:hover {
            background: darkred;
        }
        .textERW{
            color: black !important;
        }
    </style>
</head>
<body>
    <button id="review-button">Give Us a Review</button>
    <div id="review-popup" class="popup">
        <div class="popup-content">
            <span class="close-popup">&times;</span>
            <h2 class = "textERW">Enter a Review for the Website</h2>
            <textarea id="review-text" placeholder="Write your review here..."></textarea>
            <button id="submit-review">Send</button>
        </div>
    </div>
    <div id="survey-list"></div>
<script type="module">
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
    async function fetchSurveys() {
        try {
            const response = await fetch(`${pythonURI}/api/surveys`, {
                ...fetchOptions,
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            });
            if (response.ok) {
                const surveys = await response.json();
                const surveyList = document.getElementById("survey-list");
                surveyList.innerHTML = '';
                surveys.forEach(survey => {
                    const surveyBox = document.createElement('div');
                    surveyBox.classList.add('survey-box');
                    surveyBox.setAttribute('data-id', survey.id);
                    const deleteButton = document.createElement('button');
                    deleteButton.textContent = "X";
                    deleteButton.classList.add('delete-button');
                    deleteButton.addEventListener("click", () => deleteSurvey(survey.id));
                    const editButton = document.createElement('button');
                    editButton.textContent = "Edit";
                    editButton.classList.add('edit-button');
                    editButton.addEventListener("click", () => openEditPopup(survey));
                    const reviewTitle = document.createElement('div');
                    reviewTitle.textContent = "REVIEW";
                    const reviewContent = document.createElement('div');
                    reviewContent.textContent = survey.message;
                    surveyBox.appendChild(deleteButton);
                    surveyBox.appendChild(editButton);
                    surveyBox.appendChild(reviewTitle);
                    surveyBox.appendChild(reviewContent);
                    surveyList.appendChild(surveyBox);
                });
            } else {
                alert("Failed to fetch surveys.");
            }
        } catch (error) {
            console.error("Error fetching surveys:", error);
            alert("An error occurred while fetching surveys.");
        }
    }
    async function deleteSurvey(surveyId) {
        try {
            const response = await fetch(`${pythonURI}/api/survey?id=${surveyId}`, {
                ...fetchOptions,
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' }
            });
            if (response.ok) {
                alert("Survey deleted successfully!");
                fetchSurveys(); // Refresh the list after deletion
            } else {
                const errorData = await response.json();
                alert(`Failed to delete survey: ${errorData.message}`);
            }
        } catch (error) {
            console.error("Error deleting survey:", error);
            alert("An error occurred while deleting the survey.");
        }
    }
    function openEditPopup(survey) {
        const editPopup = document.getElementById("edit-popup");
        document.getElementById("edit-text").value = survey.message;
        document.getElementById("submit-edit").onclick = () => submitEdit(survey.id);
        editPopup.style.display = "block";
    }
    async function submitEdit(surveyId) {
        const updatedMessage = document.getElementById("edit-text").value;
        if (updatedMessage.trim() === "") {
            alert("Please enter a message before submitting.");
            return;
        }
        try {
            const response = await fetch(`${pythonURI}/api/survey?id=${surveyId}`, {
                ...fetchOptions,
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: updatedMessage })
            });
            if (response.ok) {
                alert("Survey updated successfully!");
                document.getElementById("edit-popup").style.display = "none";
                fetchSurveys(); // Refresh surveys after update
            } else {
                alert("Failed to update survey.");
            }
        } catch (error) {
            console.error("Error updating survey:", error);
            alert("An error occurred while updating the survey.");
        }
    }
    document.getElementById("review-button").addEventListener("click", function () {
        document.getElementById("review-popup").style.display = "block";
    });
    document.querySelector(".close-popup").addEventListener("click", function () {
        document.getElementById("review-popup").style.display = "none";
    });
    document.getElementById("submit-review").addEventListener("click", async function () {
        let reviewText = document.getElementById("review-text").value;
        if (reviewText.trim() === "") {
            alert("Please enter a review before submitting.");
            return;
        }
        try {
            const response = await fetch(`${pythonURI}/api/survey`, {
                ...fetchOptions,
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: reviewText })
            });
            if (response.ok) {
                alert("Thank you for your review!");
                document.getElementById("review-popup").style.display = "none";
                document.getElementById("review-text").value = "";
                fetchSurveys();
            } else {
                alert("Failed to submit review.");
            }
        } catch (error) {
            console.error("Error submitting review:", error);
            alert("An error occurred while submitting the review.");
        }
    });
    window.onload = fetchSurveys;
</script>

<!-- Edit Popup Modal -->
<div id="edit-popup" class="popup">
    <div class="popup-content">
        <span class="close-popup">&times;</span>
        <h2>Edit Review</h2>
        <textarea id="edit-text" placeholder="Edit your review here..."></textarea>
        <button id="submit-edit">Submit Edit</button>
    </div>
</div>

</body>
</html>