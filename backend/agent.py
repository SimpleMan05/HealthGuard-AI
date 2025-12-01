from utils.memory_utils import MemoryManager
from utils.symptom_utils import analyze_basic_symptoms

class HealthAgent:
    def __init__(self):
        self.memory = MemoryManager()

    async def run(self, user_input):
        symptom = user_input.get("symptom", "")
        self.memory.add(symptom)

        analysis = analyze_basic_symptoms(symptom)

        return {
            "input": symptom,
            "analysis": analysis,
            "memory": self.memory.get_history()
        }

health_agent = HealthAgent()
