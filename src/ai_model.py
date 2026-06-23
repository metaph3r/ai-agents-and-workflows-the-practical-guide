from enum import Enum

class AiModel(Enum):
    QWEN_3_6_35B = "qwen-3.6-35b-sovereign" # AI Hub
    GEMMA_3_1B_IT = "gemma-3-1b-it" # local AI
    GEMMA_3_1B = "gemma3:1b" # ollama