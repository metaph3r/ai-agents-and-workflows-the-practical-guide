import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_x_post(topic: str) -> str:
    prompt = f"""
You are an expert social media manager, and you excel at crafting viral, highly engaging posts for X (formerly Twitter).

Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
Avoid using hashtags or too many emojis (a few are okay, but not too many).

Keep the post short and focused. Structure it in a clean, readable way, using line breaks and blank lines to enhance readability.

Here is the topic provided by the user for which you need to generate a post:

<topic>
{topic}
</topic>
    """
    
    # call AI / LLM
    response = requests.post(
        url="http://localhost:12434/engines/v1",
        json={
            "model": "ai/smollm2",
            "prompt": prompt
        },
        headers={
            "Content-Type": "application/json"
        })
    response_text = response.json().get("output", [{}])[0].get("content", [{}])[0].get("text", "")
    return response_text

def main():
    # user input => AI (LLM) to generate X posts => output post
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post")
    print (x_post)


if __name__ == "__main__":
    main()
