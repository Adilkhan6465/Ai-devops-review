import os, json

from google import genai

#from scripts.review.providers.prompts import SYSTEM_PROMPT


def review_with_gemini(system_prompt: str, user_prompt: str) -> str:

    client = genai.Client(
        api_key=os.getenv('GEMINI_API_KEY')
    )

    response = client.models.generate_content(

        model='gemini-3.5-flash',

        contents=f'''
{system_prompt}


{user_prompt}
'''
    )

   

    return response.text.strip()