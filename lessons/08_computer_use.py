from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
from playwright.sync_api import sync_playwright
import base64
import time
from PIL import Image
from io import BytesIO

# Input Message:
input_message = [
    {
        "role": "user",
        "content": "Open chrome and search for images of Virat Kohli. Then click on the first image that you found"
    }
]

# Tools:
tools = [{
    "type": "computer_use_preview",
    "display_width": 1024,
    "display_height": 768,
    "environment": "browser",
}]

# OpenAI Client
client = OpenAI()

def show_image(base_64_image):
    image_data = base64.b64decode(base_64_image)
    image = Image.open(BytesIO(image_data))
    image.show()

# To take the screenshot of browser window and pass it back to our agent
def get_screenshot(page):
    """
    Take a full page screenshot using Playwright and return the image bytes.
    """
    return page.screenshots()

def handel_model_action(browser, page, action):
    action_type = action.type
    
    try:
        # Check if we have a new page/tab and switch to it
        all_pages = browser.contexts[0].pages
        if len(all_pages) > 1 and all_pages[-1] != page:
            page = all_pages[-1]
            print("Switch to a new tab/page")
            
        match action_type:
            case 'click':
                x, y= action.x, action.y
                button = action.button
                print(f"Clicking at ({x},{y}) with button {button}")
                page.mouse.click(x,y,button=button)
                
        return page
    
    except Exception as e:
        print(f"Error handling action {action}: {e}")
        return page # Return the original page

def computer_use_loop(browser, page, response):
    while True:
        computer_calls = [item for item in response.output if item.type == "computer_call"]
        if not computer_calls:
            print("No more computer calls. Output from model: ")
            for item in response.output:
                print(item)
            break   # Exit when no computer calls are issued.
        
        # We expect at most one computer call per response.
        computer_call = computer_calls[0]
        last_call_id = computer_call.call_id
        action = computer_call.action
        
        page = handel_model_action(browser, page, action)
        time.sleep(1)
        
        screenshot_bytes = get_screenshot(page)
        screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")
        show_image(screenshot_base64)
        
        response = client.responses.create(
            model = "computer_use_preview",
            previous_response_id = response.id,
            tools = tools,
            input = [
                {
                    "call_id": last_call_id,
                    "type":"computer_Call_output",
                    "output": {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{screenshot_base64}"
                    }
                }
            ],
            truncation="auto"                                    
        )
        print("Response: ", response.output)
        break
    return response

        

        

def main():

    # It is for an instance of a Browser
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            chromium_sandbox=True,
            env={},
            args=[
                "--disable-extensions",
                "--disable-file-system"
            ]
        )
        
        # To open a new tab in browser
        page = browser.new_page()
        
        # To set view posrt size of browser same as given in tools
        page.set_viewport_size({"width": 1024, "height": 768})
        
        # Navigate to initial URL
        page.goto("https://www.google.com", wait_until="domcontentloaded")
    
    
        # Create initial Response (Adding Response API)
        response = client.responses.create(
            #model="gpt-5",
            model="computer_use_preview",
            input=input_message,
            tools = tools,
            reasoning = {
                "generate_summary": "concise",
            },
            truncation = "auto",
            
        )

        print(response.output)
        
        final_response = computer_use_loop(browser,page,response)
        print("Final response: ", final_response.output_text)
        
        browser.close()
        
        
if __name__ == "__main__":
    main()