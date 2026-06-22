from openai import OpenAI
from dotenv import load_dotenv

from src.ai_interfaces.ai_hub_connection import AiHubConnection
from src.ai_interfaces.ollama_connection import OllamaConnection
from src.x_agent import XAgent

load_dotenv()

def main():
    # user input => AI (LLM) to generate X posts => output post
    usr_input = input("What should the post be about? ")
    x_agent = XAgent(OllamaConnection())
    
    
    x_post = x_agent.generate_x_post(usr_input)
    print("Generated X post")
    print (x_post)


if __name__ == "__main__":
    main()
