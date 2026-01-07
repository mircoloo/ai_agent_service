import os
from app.ai_agent import agent
from dotenv import load_dotenv
import asyncio
from app.utils import InvoiceCategoryOutput, ChatRequest, sample_invoice_text
from fastapi import FastAPI
from config import load_config


load_config()
app = FastAPI()

@app.get("/test")
async def test():
    return {"message": "AI Agent Service is running."}

@app.post("/chat")
async def classify_invoice(req: ChatRequest):
    result = await agent.run(agent, req.text)

    # Se result è un oggetto, lo trasformiamo in dict
    if hasattr(result, "dict"):
        return result.dict()
    return result
    


