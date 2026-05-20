import os
from scripts.common.ai_client import ask_ai

SYSTEM_PROMPT = f"""
You are a DevOps SRE expert.
Analyze logs.
Find root cause.
Suggest fixes.
"""
def analyze_logs(logs: str):

    return ask_ai(SYSTEM_PROMPT, logs)

if __name__ == "__main__":

    with open("logs/app.log", "r") as f:
        logs = f.read()

    report = analyze_logs(logs)
    os.makedirs("generated", exist_ok=True)
    with open("generated/log_report.txt", "w") as f:
        f.write(str(report))

    print("Log report generated.")




