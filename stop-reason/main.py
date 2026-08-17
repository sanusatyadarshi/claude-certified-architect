import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from anthropic import AsyncAnthropic, DefaultAioHttpClient

load_dotenv(Path(__file__).parent.parent / ".env")



# https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python
# To run:
# cd stop-reason
# source .venv/bin/activate
# python3 main.py


async def main() -> None:
    async with AsyncAnthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        http_client=DefaultAioHttpClient(),
    ) as client:
        message = await client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "Hello, Claude",
                }
            ],
            model="claude-haiku-4-5-20251001", # changed to cheaper model
        )
        print(message.content)


asyncio.run(main())