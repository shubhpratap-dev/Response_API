# This the General Structure for the response API code:

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role": "user",
        "content": "Who is Virat Kohli?"
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
)

print(response.output_text)