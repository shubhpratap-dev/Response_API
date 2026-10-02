#  from openai import OpenAI
#  from dotenv import load_dotenv
#  load_dotenv()

#  from pydantic import BaseModel, ConfigDict   # (Importing ConfigDict bcz to add additional properties)
#  from typing import List

#  # Creating the Pydantic class
#  class Event(BaseModel):
#      model_config = ConfigDict(extra="forbid")
#      name: str
#      date: str
#      location: str
#      attendees: List[str]
    
#  schema = Event.model_json_schema()

#  print(schema)

#  # Initial messages
#  input_messages = [
#      {
#          "role": "user",
#          "content": [
#              {
#                  "type": "input_text",
#                  "tetx": "Alice and Bob are going to a science fair in New York on Friday."
#              },
#          ]
#      }
#  ]


#  We are using pydantic to generate schema
#  client = OpenAI()

#  response = client.responses.create(
#      model = "gpt-4o-mini",
#      instructions="Extract the event information",
#      input=input_messages,
#      text={
#          "format": {
#              "type": "json_schema",
#              "name": "event_info",
#              "schema":{
#                  "type": "object",
#                  "properties": {
#                      "name": {
#                          "type": "string"
#                      },
#                      "data": {
#                          "type": "string"
#                      },
#                      "location": {
#                          "type": "sting"
#                      },
#                      "participants": {
#                          "type": "array",
#                          "items": {
#                              "type": "string"
#                          }
#                      },
#                  },
#                  "required": ["name", "date", "participants"],
#                  "additionalProperties": False
#              },
#              "strict": True
#          }
#      }
#  )