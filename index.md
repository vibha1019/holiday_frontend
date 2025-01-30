---
layout: post
title: Home 
search_exclude: true
hide: true
menu: nav/home.html
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Review Survey</title>
    <style>
        #review-button {
            position: fixed;
            bottom: 20px;
            left: 20px;
            padding: 10px 15px;
            background-color: #008080;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        #review-button:hover {
            background-color: #005f5f;
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
    <script>
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
            const token = localStorage.getItem("authToken"); // Ensure authentication
            if (!token) {
                alert("You must be logged in to submit a review.");
                return;
            }
            const response = await fetch("/api/survey", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({ message: reviewText })
            });
            if (response.ok) {
                alert("Thank you for your review!");
                document.getElementById("review-popup").style.display = "none";
                document.getElementById("review-text").value = "";
            } else {
                alert("Failed to submit review. Please try again.");
            }
        });
    </script>
</body>
</html>


<table style="background-color: #da95f5;">
    <tr>
        <td><a href="{{site.baseurl}}/aws">AWS Deployment Blog</a></td>
    </tr>
</table>
