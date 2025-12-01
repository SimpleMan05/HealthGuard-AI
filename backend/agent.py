from utils.memory_utils import MemoryManager
from utils.symptom_utils import analyze_basic_symptoms
from utils.mcp_tools import (
    load_symptom_rules,
    get_emergency_guideline,
    get_home_remedy
)
from utils.response_validator import validate_response

class HealthAgent:
    def __init__(self):
        self.memory = MemoryManager()
        self.symptom_db = load_symptom_rules()

    async def run(self, user_input):
        symptom = user_input.get("symptom", "")
        self.memory.add(symptom)

        # Basic rule-based analysis
        basic = analyze_basic_symptoms(symptom)

        # Emergency guideline tool
        guideline = get_emergency_guideline(symptom)

        # Home remedy tool
        remedy = get_home_remedy(symptom)

        result = {
            "symptom": symptom,
            "analysis": basic,
            "home_remedy": remedy,
            "emergency_guideline": guideline,
            "memory": self.memory.get_history()
        }

        # run quality checks
        final = validate_response(result)
        return final

health_agent = HealthAgent()
