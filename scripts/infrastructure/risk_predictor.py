import json
from scripts.common.ai_client import ask_ai

SYSTEM_PROMPT = """
You are a DevOps risk analysis expert.
Return ONLY valid JSON.
"""
def predict_deployment_risk(diff: str,deployment_time: str) -> dict:

    user_prompt = f'''
        Predict deployment risk for this change.
        Deployment time: {deployment_time}
        Code diff: {diff}

        Return json:
        {{
            "risk_score": 1-10,
            "risk_level": "low|medium|high|critical",
            "rollback_plan": "steps to rollback",
            "recommended_deploy_time": "when to deploy safely"
        }}
        '''
    raw = ask_ai(SYSTEM_PROMPT, user_prompt)
    raw = raw.strip()
    
    if raw.startswith("```json"):
        raw = raw.replace("```json", "")
        raw = raw.replace("```", "")
        raw = raw.strip()
    
    return json.loads(raw)

if __name__ == "__main__":

    with open("diff.txt", "r") as f:
        diff = f.read()

    result = predict_deployment_risk(
        diff,
        "Friday 10 PM"
    )

    with open("generated/risk_report.json", "w") as f:
        json.dump(result, f, indent=2)

    print("Risk report generated.")