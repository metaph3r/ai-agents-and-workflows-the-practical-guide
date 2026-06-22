from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_x_post(topic: str) -> str:
    # automatically uses OPENAI_API_KEY environment variable
    client = OpenAI(
        base_url="https://adesso-ai-hub.3asabc.de/v1"
    )
    instructions = """
You are an expert social media manager, and you excel at crafting viral, highly engaging posts for X (formerly Twitter).

Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
Avoid using hashtags or too many emojis (a few are okay, but not too many).

Keep the post short and focused. Structure it in a clean, readable way, using line breaks and blank lines to enhance readability.
"""
    
    # call AI / LLM
    responses = client.responses.create(
        model="gpt-4o",
        instructions=instructions, 
        input=topic
    )
    return responses.output_text

def main():
    # user input => AI (LLM) to generate X posts => output post
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post")
    print (x_post)


if __name__ == "__main__":
    main()
