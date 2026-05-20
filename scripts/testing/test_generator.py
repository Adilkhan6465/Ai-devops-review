import os
from scripts.common.ai_client import ask_ai

SYSTEM_PROMPT = """
    Generate unit tests for this Python code.
    Include: happy path, edge cases, error handling.
    Return only runnable test code.
    """
def generate_tests(source_code: str):
    
    return ask_ai(SYSTEM_PROMPT, source_code)

if __name__ == "__main__":

    with open("diff.txt", "r") as f:
        source_code = f.read()

    tests = generate_tests(source_code)
    os.makedirs("generated", exist_ok=True)
    with open("generated/generated_tests.py", "w") as f:
        f.write(str(tests))

    print("Tests generated.")


