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
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            text-align: center;
        }
        #review-button {
            padding: 10px 15px;
            background-color: rgb(15, 99, 128);
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        #review-button:hover {
            background-color: #008080;
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
        }
        #submit-review {
            margin-top: 10px;
            padding: 10px 15px;
            background-color: #008080;
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
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-top: 20px;
            padding: 0;
        }
        .survey-box {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ddd;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
            text-align: left;
            height: 180px;
            width: 250px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        .review-title {
            font-weight: bold;
            margin-bottom: 5px;
        }
        .review-content {
            flex-grow: 1;
            overflow-y: auto;
            max-height: 120px;
            padding-right: 5px;
        }
        .review-content::-webkit-scrollbar {
            width: 5px;
        }
        .review-content::-webkit-scrollbar-thumb {
            background-color: #ccc;
            border-radius: 5px;
        }
        @media (max-width: 1024px) {
            #survey-list {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (max-width: 600px) {
            #survey-list {
                grid-template-columns: repeat(1, 1fr);
            }
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
    <script>
        async function fetchSurveys() {
            try {
                const response = await fetch('/api/surveys'); 
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
                const response = await fetch('/api/survey', {
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
</body>
</html>
