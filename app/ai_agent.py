from agents import Agent, Runner, SQLiteSession
from .schemas import InvoiceCategoryOutput
from openai import OpenAI
from .schemas import ChatResponse

agent = Agent(
    name="",
    model="gpt-4o-mini",
    instructions="Your are a general agent which have to orcherstrate which agent to call for the best response or if you know you can response yourself.",
    #output_type=InvoiceCategoryOutput,
)





