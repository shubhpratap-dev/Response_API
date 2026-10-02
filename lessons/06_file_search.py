from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role": "user",
        "content": "What are the current specials?"
    }
]

tools = [
    {
        "type": "file_search",
        "vector_search_ids": ["vs_6abb93b089708191b0beb1635a20a6df"],
        "max_num_results": 2
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="You are a helpful assistant.",
    input=input_messages,
    tools = tools
)

print(response.output_text)