# DeepSeek CLI Assistant

Um assistente de linha de comando para interagir com a API do DeepSeek, usando o contexto dos arquivos do seu projeto para responder perguntas de forma inteligente.

## Instalação

### Arch Linux (AUR)

Você pode instalar diretamente do AUR usando um AUR helper, como o `yay`:

```bash
yay -S deepseek-cli
```

Ou manualmente:

```bash
git clone https://aur.archlinux.org/deepseek-cli.git
cd deepseek-cli
makepkg -si
```

Após a instalação, use o comando:

```bash
deepseekcli
```

---

### Instalação via pip (para desenvolvimento)

```bash
git clone https://github.com/seuusuario/deepseek-cli-assistant.git
cd deepseek-cli-assistant
pip install .
```

Ou, se preferir, crie um link simbólico:

```bash
sudo ln -s /caminho/para/main.py /usr/local/bin/deepseek
```

---

## Configuração

Crie um arquivo `.env` na raiz do projeto com:

```
API_KEY=sua-chave-deepseek
MODEL=deepseek-chat
BASE_URL=https://api.deepseek.com
```

---

## Uso

Execute o comando:

```bash
deepseekcli
```

Siga as instruções no terminal:

- Digite o caminho do projeto (arquivo ou pasta)
- Faça perguntas ou use comandos especiais:
    - `:file` — Trocar o projeto/contexto
    - `:ask` — Fazer uma pergunta explicitamente
    - `:exit` — Sair do assistente

Exemplo:

```
📁 Caminho do projeto (pasta ou arquivo): ./meu-projeto
Contexto carregado!
Digite uma pergunta ou comando (:file, :ask, :exit): Como funciona o arquivo main.py?
Assistente: O arquivo main.py é responsável por...
```

---

## Funcionalidades

- ✅ Usa sua API do DeepSeek
- 📁 Lê arquivos do projeto (um ou vários)
- 🧠 Recebe perguntas do usuário
- 🗨️ Responde no terminal com contexto dos arquivos
- 🔁 Funciona em loop (tipo chat)
- 🧹 Interface limpa e simples (usa [rich](https://github.com/Textualize/rich))
- ⌨️ Aceita comandos como `:file`, `:ask`, `:exit`
- 🔒 Carrega configurações do `.env` (API_KEY, MODEL, BASE_URL)

---

## Dependências

- Python 3.7+
- requests
- rich
- tqdm
- python-dotenv

Instale todas com:

```bash
pip install -r requirements.txt
```

---

## Empacotamento para Arch Linux

Para empacotar manualmente, use o PKGBUILD fornecido neste repositório.

---

## Licença

MIT

---

Feito com ❤️ por [Anthony](https://github.com/AnthonyLuciano)