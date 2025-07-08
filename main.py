# main.py

from rich.console import Console
from rich.prompt import Prompt
from context_loader import carregar_contexto
from chat_engine import enviar_para_deepseek, testar_conexao

console = Console()

def escolher_projeto():
    projeto = Prompt.ask("📁 Caminho do projeto (pasta ou arquivo)")
    contexto = carregar_contexto(projeto)
    console.print("[green]Contexto carregado![/green]")
    return projeto, contexto

def main():
    console.print("[bold cyan]Assistente DeepSeek CLI[/bold cyan]")

    # Teste de conexão antes de tudo
    if not testar_conexao():
        console.print("[red]Não foi possível conectar à API. Verifique suas configurações.[/red]")
        return

    projeto, contexto = escolher_projeto()

    while True:
        entrada = Prompt.ask("[bold yellow]Digite uma pergunta ou comando (:file, :ask, :exit)[/bold yellow]")

        if entrada.strip().lower() in [":exit", "sair", "exit", "q"]:
            console.print("[red]Saindo...[/red]")
            break

        elif entrada.strip().lower().startswith(":file"):
            projeto, contexto = escolher_projeto()

        elif entrada.strip().lower().startswith(":ask"):
            pergunta = entrada[4:].strip() or Prompt.ask("Pergunta")
            try:
                resposta = enviar_para_deepseek(pergunta, contexto)
                console.print(f"[bold green]Assistente:[/bold green] {resposta}")
            except Exception as e:
                console.print(f"[red]Erro:[/red] {e}")

        elif entrada.strip().startswith(":"):
            console.print("[yellow]Comando não reconhecido.[/yellow]")

        else:
            pergunta = entrada
            try:
                resposta = enviar_para_deepseek(pergunta, contexto)
                console.print(f"[bold green]Assistente:[/bold green] {resposta}")
            except Exception as e:
                console.print(f"[red]Erro:[/red] {e}")

if __name__ == "__main__":
    main()
