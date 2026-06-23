from openai import OpenAI

from src.ai_connection.ai_connection import AiConnection


class AiHubConnection(AiConnection):
    def __init__(self):
        self.client = OpenAI(
            base_url="https://adesso-ai-hub.3asabc.de/v1"
        )

    def execute_ai_call(self, instructions: str, prompt: str) -> str:
        print("Querying AI Hub...")
        responses = self.client.responses.create(
            model="gpt-4o",
            instructions=instructions,
            input=prompt
        )
        return responses.output_text