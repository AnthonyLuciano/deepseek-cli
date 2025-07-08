# DeepSeek CLI Assistant

A command-line assistant to interact with the DeepSeek API, using your project files as context to answer questions intelligently.

## Installation

### Arch Linux (AUR)

You can install directly from the AUR using an AUR helper like `yay`:

```bash
yay -S deepseek-cli
```

Or manually:

```bash
git clone https://aur.archlinux.org/deepseek-cli.git
cd deepseek-cli
makepkg -si
```

After installation, run the command:

```bash
deepseekcli
```

---

### Installation via pip (for development)

```bash
git clone https://github.com/yourusername/deepseek-cli-assistant.git
cd deepseek-cli-assistant
pip install .
```

Or, if you prefer, create a symbolic link:

```bash
sudo ln -s /path/to/main.py /usr/local/bin/deepseek
```

---

## Configuration

Create a `.env` file in the root of the project with:

```
API_KEY=your-deepseek-api-key
MODEL=deepseek-chat
BASE_URL=https://api.deepseek.com
```

---

## Usage

Run the command:

```bash
deepseekcli
```

Follow the terminal instructions:

* Enter the path to the project (file or folder)
* Ask questions or use special commands:

  * `:file` — Change project/context
  * `:ask` — Explicitly ask a question
  * `:exit` — Exit the assistant

Example:

```
📁 Project path (folder or file): ./my-project
Context loaded!
Type a question or command (:file, :ask, :exit): How does main.py work?
Assistant: The main.py file is responsible for...
```

---

## Features

* ✅ Uses your DeepSeek API key
* 📁 Reads project files (single or multiple)
* 🧠 Accepts user questions
* 🗨️ Answers in the terminal using file context
* 🔁 Works in a loop (chat-style)
* 🧹 Clean and simple interface (uses [rich](https://github.com/Textualize/rich))
* ⌨️ Supports commands like `:file`, `:ask`, `:exit`
* 🔒 Loads settings from `.env` (API\_KEY, MODEL, BASE\_URL)

---

## Dependencies

* Python 3.7+
* requests
* rich
* tqdm
* python-dotenv

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## Packaging for Arch Linux

To manually package, use the provided PKGBUILD in this repository.

---

## License

MIT

---

Made with ❤️ by [Anthony](https://github.com/AnthonyLuciano) aka "mrmedicmain"

---
