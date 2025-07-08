# chat_engine.py

import requests
from config import API_KEY, MODEL, BASE_URL

def enviar_para_deepseek(mensagem_usuario, contexto="", streaming=False):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Você é um assistente inteligente. Use o contexto a seguir se for útil:\n" + contexto},
            {"role": "user", "content": mensagem_usuario}
        ],
        "stream": streaming
    }

    if streaming:
        resp = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=body, stream=True)
        resposta = ""
        for line in resp.iter_lines():
            if line:
                try:
                    import json
                    data = json.loads(line.decode("utf-8"))
                    content = data.get("choices", [{}])[0].get("delta", {}).get("content", "")
                    print(content, end="", flush=True)
                    resposta += content
                except Exception:
                    continue
        print()  # Nova linha ao final do streaming
        return resposta
    else:
        resp = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=body)
        if resp.status_code == 200:
            return resp.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Erro {resp.status_code}: {resp.text}")

def testar_conexao():
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        body = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ],
            "stream": False
        }
        resp = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=body, timeout=30)
        return resp.status_code == 200
    except Exception as e:
        print(f"[Erro] Falha ao conectar: {e}")
        return False
