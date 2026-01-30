from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake
from src.logger import log_message

app = FastAPI()

agent = WaterIntakeAgent()

class IntakeRequest(BaseModel):
    user_id: str
    intake_ml: int


@app.post("/log-intake")    
