import os
from dotenv import load_dotenv
from pathlib import Path

def get_key(name, default=None):
    return os.getenv(name, default)

def load_env():
    env_path = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(env_path)