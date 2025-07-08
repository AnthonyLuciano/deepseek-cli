# config.py

import os
from dotenv import load_dotenv

# 1. Verifica se o .env existe, se não, cria um vazio
if not os.path.exists(".env"):
    with open(".env", "w") as f:
        f.write("# Variáveis de ambiente para DeepSeek CLI\n")

load_dotenv()

def pedir_env_var(nome, mensagem):
    valor = input(f"{mensagem}: ").strip()
    with open(".env", "a") as f:
        f.write(f"{nome}={valor}\n")
    return valor

API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")
BASE_URL = os.getenv("BASE_URL")

if not API_KEY:
    API_KEY = pedir_env_var("API_KEY", "Digite sua API KEY do DeepSeek")
if not MODEL:
    MODEL = pedir_env_var("MODEL", "Digite o modelo (ex: deepseek-reasoner)")
if not BASE_URL:
    BASE_URL = pedir_env_var("BASE_URL", "Digite a BASE_URL (ex: https://api.deepseek.com/v1)")
