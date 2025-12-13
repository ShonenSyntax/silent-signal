import google.generativeai as genai

#Will set this key later
genai.configure(api_key="API_KEY_HERE")

model = genai.GenerativeModel("gemini-1.5-flash")

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