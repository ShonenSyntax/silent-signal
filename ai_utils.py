import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() #reads .env

# Read API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-flash-latest")

def analyze_report(report_text):
    prompt = f"""
    You are analyzing anonymous campus issue reports.

    Task:
    1. Summarize the issue in one sentence.
    2. Classify it into one category:
        - Harassement
        - Safety
        - Infrastructure
        - Academic
        - Other
    3. Assign a severity level from 1(low) to 5(critical).

    Report:
    {report_text}

    Respond strictly in this format:
    Summary:
    Category:
    Severity:
    """

    response = model.generate_content(prompt)
    return response.text