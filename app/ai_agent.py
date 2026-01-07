from agents import Agent, Runner, trace, function_tool
from app.utils import InvoiceCategoryOutput
from openai import OpenAI

client = OpenAI()  # picks the key from the environment

agent = Agent(
    name="MyTestAgent",
    model="gpt-4o-mini",
    instructions="Un agente che deve riconoscere le categoria di una fattura con il testo estratto tramite OCR da un pdf.",
    output_type=InvoiceCategoryOutput,
    client=client,
)