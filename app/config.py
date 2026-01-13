from dotenv import load_dotenv
import os


def load_config():
    load_dotenv()

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PORT = int(os.getenv("PORT", 8000))

    if OPENAI_API_KEY is None:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")
