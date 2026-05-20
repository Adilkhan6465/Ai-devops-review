import os
from scripts.common.ai_client import ask_ai

SYSTEM_PROMPT = """
You are a Terraform expert.
Generate production-ready Terraform code.
Follow best practices: variables, outputs, tags.
"""

def generate_terraform(requirement: str):
 
    return ask_ai(SYSTEM_PROMPT, requirement)

if __name__ == "__main__":

    terraform_code = generate_terraform(
        "AWS EC2 t3.micro with port 443"
    )
    os.makedirs("generated", exist_ok=True)
    with open("generated/main.tf", "w") as f:
        f.write(str(terraform_code))

    print("Terraform generated.")




