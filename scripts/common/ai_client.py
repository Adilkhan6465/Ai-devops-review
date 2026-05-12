from scripts.review.providers.fallback_provider import review_with_fallback

def ask_ai(system_prompt: str, user_prompt) -> str:
    
    return review_with_fallback(system_prompt, user_prompt)