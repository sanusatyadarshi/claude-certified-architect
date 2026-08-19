# https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#tool-use
# To run:
# cd 002-tool-use
# (first time only) python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
# source .venv/bin/activate
# python3 main.py


# For advanced tool-using agent: https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent

import json
import os
from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic, beta_tool

load_dotenv(Path(__file__).parent.parent / ".env")

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


@beta_tool
def get_weather(location: str) -> str:
    """Get the weather for a given location.

    Args:
        location: The city and state, for example, San Francisco, CA
    Returns:
        A JSON-encoded string with the location, temperature, and weather condition.
    """
    return json.dumps(
        {
            "location": location,
            "temperature": "68°F",
            "condition": "Sunny",
        }
    )


# Use the tool_runner to automatically handle tool calls
runner = client.beta.messages.tool_runner(
    max_tokens=1024,
    model="claude-opus-5",
    tools=[get_weather],
    messages=[
        {"role": "user", "content": "What is the weather in Bengaluru?"},
    ],
)
for message in runner:
    print(message)