import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega o .env da raiz de agente-estudos para os testes
env_path = Path(__file__).resolve().parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
