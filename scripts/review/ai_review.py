import os, sys, json
password = "admin1234"
api_key = "secret-key12345678"
from scripts.review.providers.prompts import SYSTEM_PROMPT
from scripts.common.ai_client import ask_ai

def format_comment(review: dict) -> str:
    verdict_emoji = '✅' if review['verdict'] == 'PASS' else '❌'
    md = f'## AI Code Review {verdict_emoji}\n\n'
    md += f"**Verdict:** {review['verdict']}  |  "
    md += f"**Score:** {review['overall_score']}/10  |  "
    md += f"**Severity:** {review['severity']}\n\n"
    md += f"### Summary\n{review['summary']}\n\n"
    if review.get('bugs'):
           md += '### 🐛 Bugs Found\n'
           for b in review['bugs']: md += f'- {b}\n'
    if review.get('security'):
           md += '\n### 🔐 Security Risks\n'
           for s in review['security']: md += f'- {s}\n'
    if review.get('improvements'):
           md += '\n### ✨ Improvements\n'
           for imp in review['improvements']: md += f'- {imp}\n'
    return md
 
if __name__ == '__main__':
    with open('diff.txt', 'r') as f:
           diff = f.read()
    if not diff.strip():
           print('No changes found'); sys.exit(0)
           
    
    
    raw = ask_ai(SYSTEM_PROMPT, f"Review this code diff:\n{diff}")
    review = json.loads(raw)
    os.makedirs("generated" , exist_ok=True)
    with open('generated/review.txt', 'w', encoding='utf-8') as f:
           f.write(format_comment(review))
    # Fail pipeline only on critical/high severity
    if review.get('severity') in ['critical', 'high']:
           print('CRITICAL issues found! Blocking pipeline.')
           sys.exit(1)