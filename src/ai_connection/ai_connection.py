from abc import ABC, abstractmethod

from src.ai_model import AiModel
from src.ai_prompt.ai_prompt import AiPrompt

class AiConnection(ABC):
    @abstractmethod    
    def execute_ai_call(self, prompt: AiPrompt, model: AiModel) -> str:
        """execute an ai call and return the output text"""
        pass