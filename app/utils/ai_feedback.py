import requests

GROK_API_KEY = "YOUR_GROK_API_KEY"  # replace with your free API key
GROK_URL = "https://api.puter.ai/v2/chat"

def generate_ai_feedback(matched_skills, missing_skills, job_title, company_name):
    """
    Generates company-style feedback using Grok AI
    """
    prompt = (
        f"As a recruiter from {company_name}, evaluate the candidate for the {job_title} role. "
        f"The candidate has the following skills: {', '.join(matched_skills)}. "
        f"Missing skills for this role: {', '.join(missing_skills)}. "
        f"Provide formal, company-focused feedback on how suitable the candidate is, "
        f"without sounding like advice to the candidate directly."
    )

    headers = {"Authorization": f"Bearer {GROK_API_KEY}"}
    payload = {
        "model": "x-ai/grok-4.20-beta",
        "input": prompt
    }

    response = requests.post(GROK_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data.get("message", {}).get("content", "No feedback generated")
    else:
        return "Failed to generate AI feedback"