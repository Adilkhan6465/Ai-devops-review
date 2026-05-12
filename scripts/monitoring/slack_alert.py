import os
import requests
from scripts.common.ai_client import ask_ai

SYSTEM_PROMPT = """
You are a DevOps incident response expert.
Generate concise Slack alerts.
"""
def create_incident_alert(error_data: dict):

    return ask_ai(SYSTEM_PROMPT, str(error_data))

def post_to_slack(message: str):

    webhook = os.getenv("SLACK_WEBHOOK")

    requests.post(
        webhook,
        json={"text": str(message)}
    )

if __name__ == "__main__":

    alert = create_incident_alert({
        "cpu": 95,
        "service": "backend-api"
    })

    print(alert)


