from abc import ABC, abstractmethod

from src.ai_prompt.ai_prompt import AiPrompt

class AiConnection(ABC):
    @abstractmethod    
    def execute_ai_call(self, prompt: AiPrompt) -> str:
        """execute an ai call and return the output text"""
        pass