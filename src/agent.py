import os
# from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_KEY")

llm = ChatOllama(model="llama3")

class WaterIntakeAgent():
    def __init__(self):
        self.history = []
    def analyze_intake(self, intake_ml):
        prompt= f"""You are a health assistant specialized in tracking water intake. A user has consumed {intake_ml} ml of water today. Provide hydration status and recommendations based on this intake."""

        response = llm.invoke([HumanMessage(content=prompt)])    
        return response.content
    
if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake = 1500
    feedback = agent.analyze_intake(intake)
    print(f"Hydration Analysis: {feedback}")    