from mistralai import Mistral
import os
from config import api_ai

async def generate(content):
    s = Mistral(
        api_key = api_ai,
    )
    res = await s.chat.complete_async(model='mistral-small-latest',messages=[
        {
            'content':content,
            'role':'user',
        },
    ])
    if res is not None:
        return res.choices[0].message.content