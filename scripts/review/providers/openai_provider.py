import os, sys, json
from openai import OpenAI      	# openai >= 1.0.0
#from scripts.review.providers.prompts import SYSTEM_PROMPT



def review_with_openai(system_prompt: str, user_prompt: str) -> str:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()


   