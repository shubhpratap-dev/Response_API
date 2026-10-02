# There are two ways:
#                     1. Json Mode
#                     2. Structured output

# Here we are seeing Structured Output Mode:

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()



# Structured Mode:

input_messages = [
    {
        "role": "user",
        "content": "Alice and Bob are going to a science fair in New York on 26 August, 2026."
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Extract the event information.",
    input=input_messages,
    text = {
        "format": {
            "type": "json_schema",
            "name": "calendar_event",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "date": {
                        "type": "string"
                    },
                    "location": {
                        "type": "string"
                    },
                    "participants": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": ["name", "date", "location", "participants"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
)

print(response.output_text)