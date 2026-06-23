from openai import OpenAI

from src.ai_model import AiModel
from src.ai_prompt.ai_prompt import AiPrompt
from src.ai_connection.ai_connection import AiConnection


class LocalAiConnection(AiConnection):
    def __init__(self):
        self.client = OpenAI(
            base_url="https://localhost:8080/v1"
        )

    def execute_ai_call(self, prompt: AiPrompt, model: AiModel = AiModel.GEMMA_3_1B_IT) -> str:
        print("Querying AI Hub...")
        responses = self.client.responses.create(
            model=model.value,
            input=prompt.get_prompt()
        )
        return responses.output_text