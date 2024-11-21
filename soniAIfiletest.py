import google.generativeai as genai
import json
import os

# Use the environment variable "API_KEY" to configure the API key
genai.configure(api_key=os.environ["API_KEY"])

# Load dataset
dataset_path = "dataset2.json"
try:
    with open(dataset_path, "r") as open_file:
        dataset = json.load(open_file)["database"]
except FileNotFoundError:
    dataset = []

new_user = ""

# AI Assistant Instructions
instructions = """
You are an application with special expertise in recommending good book suggestions based on the 
information given in the dataset. Depending on the 3 preferred genres of the person, you are required 
to provide 5 suggested books, their authors, genres, a short synopsis, and age rating.
"""

# Get user input
prompt = input("Enter a prompt: ")

# Prepare the prompt by combining the dataset and instructions
context = f"Dataset: {dataset}\n\nInstructions: {instructions}\n\nPrompt: {prompt}"

try:
    # Generate text using the Gemini API (correct method usage)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        input_text = context,  # Correct argument for the input content
        max_output_tokens = 500,  # Optional: Adjust as needed
        temperature=0.7,  # Optional: Adjust creativity level
    )

    # Display the AI response
    print("\n############################################")
    print("Response: ")
    print(response.text)  # Should now correctly print the generated text
    print("############################################\n")

    # Check if the user wants to add new data
    if "book recommendation" in response.text.lower():
        print("You are not in our database. Would you like to be added? Type yes/no.")
        yesNo = input()
        if yesNo.lower() == "yes":
            newName = input("Enter your name: ")
            bookGenre1 = input("Enter your preferred genre 1: ")
            bookGenre2 = input("Enter your preferred genre 2: ")
            bookGenre3 = input("Enter your preferred genre 3: ")
            new_user = {
                "name": newName,
                "bookGenre1": bookGenre1,
                "bookGenre2": bookGenre2,
                "bookGenre3": bookGenre3
            }

            dataset.append(new_user)
            with open(dataset_path, "w") as outfile:
                json.dump({"database": dataset}, outfile)
                print("New user information added.")
                print("Please re-run the program and ask again.")

except Exception as e:
    print("An error occurred while generating text:", str(e))
git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only 