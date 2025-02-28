<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Review Survey</title>
    <style>
        body {
            background-image: url('{{site.baseurl}}/images/present.png');
            background-position: center;
            max-height: 250vh;
            background-size: 800px auto; /* Adjust width */
            }
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
        .edit-button {
            position: absolute;
            top: 5px;
            left: 10px;
            background: blue;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 14px;
            border-radius: 5px;
            padding: 5px;
        }
        .edit-button:hover {
            background: darkblue;
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
            <h2 class="textERW">Enter a Review for the Website</h2>
            <textarea id="review-text" placeholder="Write your review here..."></textarea>
            <button id="submit-review">Send</button>
        </div>
    </div>
    <div id="survey-list"></div>
    <script type="module">
        import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
        async function getCurrentUserId() {
            try {
                const response = await fetch(`${pythonURI}/api/current_user`, {
                    ...fetchOptions,
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json' }
                });
                if (response.ok) {
                    const data = await response.json();
                    return data.userId; // Assuming backend returns { userId: "123" }
                } else {
                    console.error("Failed to get current user ID.");
                    return null;
                }
            } catch (error) {
                console.error("Error fetching user ID:", error);
                return null;
            }
        }
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
                    const currentUserId = await getCurrentUserId();
                    console.log(`Current User ID: ${currentUserId}`);
                    surveys.forEach(survey => {
                        console.log(`Survey ID: ${survey.id}, Created by User ID: ${survey.userId}`);
                        const surveyBox = document.createElement('div');
                        surveyBox.classList.add('survey-box');
                        surveyBox.setAttribute('data-id', survey.id);
                        if (survey.userId === currentUserId) {
                            const deleteButton = document.createElement('button');
                            deleteButton.textContent = "X";
                            deleteButton.classList.add('delete-button');
                            deleteButton.addEventListener("click", () => deleteSurvey(survey.id));
                            surveyBox.appendChild(deleteButton);
                        }
                        surveyList.appendChild(surveyBox);
                    });
                } else {
                    alert("Failed to fetch surveys.");
                }
            } catch (error) {
                console.error("Error fetching surveys:", error);
            }
        }
        async function deleteSurvey(surveyId) {
            try {
                const currentUserId = await getCurrentUserId();
                if (!currentUserId) {
                    alert("Unable to verify user. Please log in.");
                    return;
                }
                console.log(`Current User ID: ${currentUserId}`);
                console.log(`Attempting to delete survey ID: ${surveyId}`);
                const response = await fetch(`${pythonURI}/api/survey?id=${surveyId}`, {
                    ...fetchOptions,
                    method: 'DELETE',
                    headers: { 'Content-Type': 'application/json' }
                });
                if (response.ok) {
                    alert("Survey deleted successfully!");
                    fetchSurveys();
                } else {
                    const errorData = await response.json();
                    console.error("Deletion failed:", errorData);
                    alert(`Failed to delete survey: ${errorData.message}`);
                }
            } catch (error) {
                console.error("Error deleting survey:", error);
                alert("An error occurred while deleting the survey.");
            }
        }
        function editSurvey(survey) {
            document.getElementById("review-popup").style.display = "block";
            const reviewTextArea = document.getElementById("review-text");
            reviewTextArea.value = survey.message;
            document.getElementById("submit-review").onclick = () => updateSurvey(survey.id);
        }
        async function updateSurvey(surveyId) {
            const reviewText = document.getElementById("review-text").value;
            if (reviewText.trim() === "") {
                alert("Please enter a review before submitting.");
                return;
            }
            try {
                const response = await fetch(`${pythonURI}/api/survey?id=${surveyId}`, {
                    ...fetchOptions,
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: reviewText })
                });
                if (response.ok) {
                    alert("Survey updated successfully!");
                    document.getElementById("review-popup").style.display = "none";
                    document.getElementById("review-text").value = "";
                    fetchSurveys();
                } else {
                    alert("Failed to update survey.");
                }
            } catch (error) {
                console.error("Error updating survey:", error);
                alert("An error occurred while updating the survey.");
            }
        }
        document.getElementById("review-button").addEventListener("click", () => {
            document.getElementById("review-popup").style.display = "block";
        });
        document.querySelector(".close-popup").addEventListener("click", () => {
            document.getElementById("review-popup").style.display = "none";
        });
        window.onload = fetchSurveys;
    </script>
</body>
</html>
