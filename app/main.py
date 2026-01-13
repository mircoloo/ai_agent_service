import logging
import asyncio
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .schemas import InvoiceCategoryOutput, ChatRequest, ChatResponse
from .config import load_dotenv
from .ai_agent import agent
from agents import Runner

# ---- logging ----
logger = logging.getLogger("api")

# ---- config ----
load_dotenv()

app = FastAPI()

@app.get("/test")
async def test():
    logger.info("Health check endpoint called")
    return {"message": "AI Agent Service is running."}


@app.post("/v1/chat")
async def chat(req: ChatRequest = Body(..., description="Chat request payload")):
    logger.info("Received chat request")
    result = await Runner.run(agent, req.req_text)
    return ChatResponse(res_text=result.final_output)
