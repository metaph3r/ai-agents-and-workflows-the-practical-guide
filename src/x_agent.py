from src.ai_prompt.x_post_prompt import XPostPrompt
from src.ai_connection.ai_connection import AiConnection


class XAgent:
    def __init__(self, ai_connection: AiConnection):
        self.connection = ai_connection
    
    def generate_x_post(self, topic: str) -> str:
        prompt = XPostPrompt(topic)        
        return self.connection.execute_ai_call(prompt)