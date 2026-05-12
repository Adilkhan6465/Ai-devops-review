import os, json

import anthropic

#from scripts.review.providers.prompts import SYSTEM_PROMPT

def review_with_claude(system_prompt: str, user_prompt: str) -> str:
    client = anthropic.Anthropic(
        api_key=os.getenv('ANTHROPIC_API_KEY')
    )
    response = client.messages.create(

        model='claude-sonnet-4-20250514',

        max_tokens=2048,

        messages=[
            {
                'role': 'user',
                'content': f'''
{system_prompt}


{user_prompt}
'''
            }
        ]
    )

    

    return response.content[0].text.strip()