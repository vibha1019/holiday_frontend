import os
import google.auth
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# Path to your OAuth 2.0 credentials JSON file
credentials_file = r"C:\Users\kdhen\Downloads\client_secret_307600395344-7t14i5bd0nn7hn7apjskirkh35qvcrvc.apps.googleusercontent.com.json"# Replace with the path to your downloaded file

# Set up the OAuth flow
flow = InstalledAppFlow.from_client_secrets_file(
    credentials_file,
    scopes=['https://www.googleapis.com/auth/cloud-platform']  # You can change the scope based on the API you're using
)

creds = flow.run_local_server(port=0)  # This will open a browser for you to sign in and grant access

# If the credentials are expired and have a refresh token, refresh them
if creds and creds.expired and creds.refresh_token:
    creds.refresh(Request())

# Get the access token
access_token = creds.token
print("Access Token:", access_token)
