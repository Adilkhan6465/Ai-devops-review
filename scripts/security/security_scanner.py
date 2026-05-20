import json, os
from scripts.common.ai_client import ask_ai

SECURITY_PROMPT = '''
You are a security expert. Scan for:
- Hardcoded passwords, API keys, tokens
- SQL injection vulnerabilities
- XSS vulnerabilities
- Insecure dependencies
- OWASP Top 10 issues

Return ONLY valid JSON: {issues: [{type, severity, line, description, fix}]}
'''
 
def security_scan(code: str) -> dict:
    raw = ask_ai(SECURITY_PROMPT, code)
    
    raw = raw.strip()
 
    if raw.startswith("```json"):
        raw = raw.replace("```json", "")
        raw = raw.replace("```", "")
        raw = raw.strip()

    return json.loads(raw)

if __name__ == "__main__":

    with open("diff.txt", "r") as f:
        code = f.read()

    result = security_scan(code)
    os.makedirs("generated", exist_ok=True)
    with open("generated/security_report.txt", "w") as f:
        f.write(json.dumps(result, indent=2))

    print("Security report generated.")