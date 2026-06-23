from openai import OpenAI

from src. ai_model import AiModel
from src.ai_prompt.ai_prompt import AiPrompt
from src.ai_connection.ai_connection import AiConnection


class AiHubConnection(AiConnection):
    def __init__(self):
        self.client = OpenAI(
            base_url="https://adesso-ai-hub.3asabc.de/v1"
        )

    def execute_ai_call(self, prompt: AiPrompt, model: AiModel = AiModel.QWEN_3_6_35B) -> str:
        print("Querying AI Hub...")
        responses = self.client.responses.create(
            model=model.value,
            input=prompt.get_prompt()
        )
        return responses.output_text