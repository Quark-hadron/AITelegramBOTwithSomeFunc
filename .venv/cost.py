import asyncio
import os

from mistralai import Mistral


async def main():
    api_key = os.environ["oR23xggffrpIVX6klVhvxmIIz3pMdwQJ"]
    model = "mistral-tiny"

    client = Mistral(api_key=api_key)

    response = await client.chat.stream_async(
        model=model,
        messages=[
             {
                  "role": "user",
                  "content": "Who is the best French painter? Answer in JSON.",
              },
        ],
    )
    async for chunk in response:
        if chunk.data.choices[0].delta.content is not None:
            print(chunk.data.choices[0].delta.content, end="")


if __name__ == "__main__":
    asyncio.run(main())