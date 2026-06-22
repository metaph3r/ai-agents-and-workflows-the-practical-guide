from abc import ABC, abstractmethod

class AiConnection(ABC):
    @abstractmethod    
    def execute_ai_call(self, instruction: str, prompt: str) -> str:
        """execute an ai call and return the output text"""
        pass