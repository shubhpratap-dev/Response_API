from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, ConfigDict
import json

# Tool Functions
def get_todo_list():
    return [
        {
            "id": 1,
            "title": "Buy Bread"
        },
        {
            "id": 2,
            "title": "Buy Milk"
        }
    ]
    
# Pydantic Schema:
class GetTodoListParams(BaseModel):
    model_config = ConfigDict(extra="forbid")
    pass

# Generate schemas
todo_list_schema = GetTodoListParams.model_json_schema()
    
tools = [
    {
        "type": "function",
        "name": "get_todo_list",
        "description": "Get the list of tools",
        "parameters": todo_list_schema,
        "strict": True
    }
]

client = OpenAI()

input_messages = [
    {
        "role": "user",
        "content": "What are my todos?"
    }
]

while True:
    response = client.responses.create(
        model="gpt-4o-mini",
        input=input_messages,
        tools=tools
    )
    
    response_output = response.output[0]
    response_type = response_output.type
    
    if response_type == "message":
        print(response.output_text)
        break
        
    if response_type == "function_call":
        function_name = response_output.name
        arguments = response_output.arguments
        args = json.loads(arguments)
        
        print(f"Function: {function_name} with args: {args}")
        
        tool_result = ""
        if function_name == "get_todo_list":
            tool_result = get_todo_list()

        input_messages.append(response_output)
        input_messages.append({
            "type": "function_call_output",
            "call_id": response_output.call_id,
            "output": str(tool_result)
        })
        
    print(response.output)