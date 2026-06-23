from abc import ABC, abstractmethod

class AiPrompt(ABC):
    @abstractmethod
    def get_prompt(self) -> str:
        """return prompt"""        
        pass