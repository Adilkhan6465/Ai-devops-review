from scripts.review.providers.openai_provider import review_with_openai
from scripts.review.providers.claude_provider import review_with_claude
from scripts.review.providers.gemini_provider import review_with_gemini

def review_with_fallback(system_prompt: str, user_prompt: str) -> str:
    models = [
        ('OpenAI GPT-4o',  review_with_openai),
        ('Claude Sonnet',  review_with_claude),
        ('Gemini Flash',   review_with_gemini),
    ]
    for name, fn in models:
        try:
           print(f'Trying {name}...')
           result = fn(system_prompt, user_prompt)
           print(f'Success with {name}')
           return result
        except Exception as e:
           print(f'{name} unavailable: {e}. Trying next provider...')
    raise RuntimeError('All AI models failed')