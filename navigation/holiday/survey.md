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
        .popup-content h2 {
            color: black;
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
        .close-popup {
            position: absolute;
            top: 10px;
            right: 15px;
            font-size: 20px;
            cursor: pointer;
        }
        #survey-list {
            margin-top: 20px;
            padding: 0;
            display: flex;
            flex-direction: column;
            gap: 10px;
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
            width: 250px;
        }
        .survey-box p {
            margin: 5px 0;
            color: black;
        }
    </style>
</head>
<body>
    <button id="review-button">Give Us a Review</button>
    <div id="review-popup" class="popup">
        <div class="popup-content">
            <span class="close-popup">&times;</span>
            <h2>Enter a Review for the Website</h2>
            <textarea id="review-text" placeholder="Write your review here..."></textarea>
            <button id="submit-review">Send</button>
        </div>
    </div>
    <div id="survey-list"></div>
    <script type="module">
        // Ensure the correct import
        import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
        async function fetchSurveys() {
            try {
                // Using the dynamic pythonURI for fetching surveys
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
                        const reviewTitle = document.createElement('div');
                        reviewTitle.classList.add('review-title');
                        reviewTitle.textContent = "Review";
                        const reviewContent = document.createElement('div');
                        reviewContent.classList.add('review-content');
                        reviewContent.textContent = survey.message;
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
        // The review button to open the popup
        document.getElementById("review-button").addEventListener("click", function () {
            document.getElementById("review-popup").style.display = "block";
        });
        // Close popup on close icon click
        document.querySelector(".close-popup").addEventListener("click", function () {
            document.getElementById("review-popup").style.display = "none";
        });
        // Submit the review to the API
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
                    fetchSurveys(); // Refresh the survey list
                } else {
                    alert("Failed to submit review.");
                }
            } catch (error) {
                console.error("Error submitting review:", error);
                alert("An error occurred while submitting the review.");
            }
        });
        // Fetch surveys on page load
        window.onload = fetchSurveys;
    </script>
</body>
</html>
