# There are two ways:
#                     1. Json Mode
#                     2. Structured output

# Here we are seeing Json Mode:

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()


# Json Mode:

input_messages = [
    {
        "role": "user",
        "content": """
        Alice and Bob are going to a science fair on 26 August, 2026.
        
        Respond with JSON object with the following keys:
        {
            "name": "Name of event",
            "date": "Date of event",
            "location": "Location of event",
            "attendees": ["Name of aattendees]
        }
        """
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="You are a helpful assistant.",
    input=input_messages,
    text = {
        "format": {
            "type": "json_object"
        }
    }
)

print(response.output_text)