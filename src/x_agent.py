from src.ai_interfaces.ai_interface import AiConnection


class XAgent:
    def __init__(self, ai_connection: AiConnection):
        self.connection = ai_connection
    
    def generate_x_post(self, topic: str) -> str:
        instructions = """
You are an expert social media manager, and you excel at crafting viral, highly engaging posts for X (formerly Twitter).

Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
Avoid using hashtags or too many emojis (a few are okay, but not too many).

Keep the post short and focused. Structure it in a clean, readable way, using line breaks and blank lines to enhance readability.
"""
        
        return self.connection.execute_ai_call(instructions=instructions, prompt=topic)