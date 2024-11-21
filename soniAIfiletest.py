import os
import requests

# Define API endpoint and headers
API_URL = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText"
API_KEY = os.environ.get("API_KEY")  # Ensure API_KEY is set in your environment variables
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# AI Assistant Instructions
instructions = """
You are an application with special expertise in recommending good book suggestions based on the user's input. 
Please provide 5 book suggestions along with their authors, genres, short synopsis, and age ratings based on the prompt given.
"""

# Get user input
prompt = input("Enter a prompt for book recommendations: ")

# Prepare the context to send
context = f"Instructions: {instructions}\n\nPrompt: {prompt}"

# Prepare the request body
request_data = {
    "prompt": context,
    "max_output_tokens": 500,  # Limit the response size
    "temperature": 0.7,  # Control creativity level (higher = more creative)
}

# Make the POST request to the API
try:
    response = requests.post(API_URL, json=request_data, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses (4xx/5xx)
    
    # Get the response from the API and print the result
    response_data = response.json()
    print("\n############################################")
    print("Response: ")
    print(response_data.get("result", "No result found"))
    print("############################################\n")
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred while sending the request: {e}")
