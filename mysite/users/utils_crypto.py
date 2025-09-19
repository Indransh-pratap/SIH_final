from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet
from pathlib import Path

# Load .env from parent folder of 'users' (where manage.py is)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)  # load .env

KEY = os.environ.get("ENCRYPTION_KEY")
if not KEY:
    raise Exception("Set ENCRYPTION_KEY environment variable")

fernet = Fernet(KEY.encode())

def encrypt_text(plain_text: str) -> bytes:
    return fernet.encrypt(plain_text.encode())

def decrypt_text(token: bytes) -> str:
    return fernet.decrypt(token).decode()
