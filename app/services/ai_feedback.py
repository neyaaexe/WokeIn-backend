import requests

PUTER_API_URL = "https://api.puter.com/v2/ai/chat"

def get_ai_feedback(score, matched, missing_skills):
    prompt = f"""
You are an AI hiring assistant representing a company.

Context:
- Candidate Score: {score}
- Strong Evidence:
{matched}
- Missing Skills:
{missing_skills}

Instructions:
1. Provide a professional evaluation from the company's perspective.
2. Do NOT criticize the candidate personally.
3. Frame gaps as "expectations from the role" rather than weaknesses.
4. Maintain a formal and constructive tone.

Output Format:
- Summary
- Key Strengths
- Areas Aligned with Company Expectations
- Areas Where Company Expectations Differ
- Final Recommendation (Strong Hire / Consider / Not Aligned)

Example tone:
"The candidate demonstrates solid experience in X. The role, however, places additional emphasis on Y..."
"""

    payload = {
        "model": "x-ai/grok-4.20-beta",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(PUTER_API_URL, json=payload, headers=headers)
        data = response.json()

        return data.get("message", {}).get("content", "No response")

    except Exception as e:
        return f"AI Error: {str(e)}"
        