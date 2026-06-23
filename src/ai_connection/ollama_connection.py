from ollama import generate, GenerateResponse

from src.ai_connection.ai_connection import AiConnection


class OllamaConnection(AiConnection):
    def execute_ai_call(self, instructions: str, prompt: str) -> str:
        print("Querying Ollama...")        
        prompt = f"""
{instructions}

Here's the topic provided by the user for which you need to generate a post:

<topic>
{prompt}
</topic>
"""
        response:GenerateResponse  = generate(model="qwen3.5:0.8b", prompt=prompt)
        return response.response