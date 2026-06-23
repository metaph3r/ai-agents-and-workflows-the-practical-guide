from ollama import generate, GenerateResponse

from src.ai_prompt.ai_prompt import AiPrompt
from src.ai_connection.ai_connection import AiConnection


class OllamaConnection(AiConnection):
    def execute_ai_call(self, prompt: AiPrompt) -> str:
        print("Querying Ollama...")
        response: GenerateResponse = generate(model="gemma3:1b", prompt=prompt.get_prompt())
        return response.response