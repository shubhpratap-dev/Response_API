# API-Response

Practice lessons for the OpenAI Responses API.

## Project structure

```
API-Response/
├── assets/
│   └── menu.jpg                  # image used in lesson 02
├── lessons/
│   ├── 01_basic_response.py      # general structure of a Responses API call
│   ├── 02_image_input.py         # sending an image, extracting menu items
│   ├── 03_json_mode.py           # JSON Mode
│   ├── 04_structured_output.py   # Structured Output with a JSON schema
│   ├── 05_pydantic_schema.py     # generating the schema with Pydantic
│   ├── 06_file_search.py         # File Search tool (vector store)
│   ├── 07_function_calling.py    # function calling / tool loop
│   └── 08_computer_use.py        # Computer Use with Playwright
├── .env                          # OPENAI_API_KEY (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium   # only needed for lesson 08
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-key-here
```

## Running a lesson

From the project root:

```powershell
python lessons/01_basic_response.py
```
