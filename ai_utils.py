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
        - Harassment
        - Safety
        - Infrastructure
        - Academic
        - Management
        - Other
    3. Assign a severity level from 1(low) to 5(critical).
       Severity scale (campus context):
        - 1 Minor inconvenience, no harm, no urgency  
        - 2 Repeated inconvenience or discomfort  
        - 3 Emotional distress, harassment, or moderate disruption  
        - 4 Serious harassment, discrimination, or safety risk  
        - 5 Immediate danger, abuse, or severe safety threat
        Severity should be based on human impact, urgency for administration,
        and potential long-term effects, not just physical dange.


    Report:
    {report_text}

    Respond strictly in this format:
    Summary:
    Category:
    Severity:
    """

    response = model.generate_content(prompt)
    return response.text
    
def parse_analysis(response):
    lines = response.split("\n")

    result = {
        "summary": "",
        "category": "",
        "severity": 0
    }

    for line in lines:
        if line.startswith("Summary:"):
            result["summary"] = line.replace("Summary: ", "").strip()
        elif line.startswith("Category: "):
            result["category"] = line.replace("Category: ", "").strip()
        elif line.startswith("Severity:"):
            try:
                result["severity"] = int(line.replace("Severity: ", "").strip())
            except:
                result["severity"] = 0
    
    return result