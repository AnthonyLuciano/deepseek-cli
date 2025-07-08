import os

def carregar_contexto(caminho):
    conteudo = ""
    arquivos_lidos = 0

    if os.path.isfile(caminho):
        arquivos = [caminho]
    elif os.path.isdir(caminho):
        arquivos = []
        for root, dirs, files in os.walk(caminho):
            for file in files:
                arquivos.append(os.path.join(root, file))
    else:
        print(f"[Erro] Caminho não encontrado: {caminho}")
        return ""

    for caminho_completo in arquivos:
        try:
            with open(caminho_completo, 'r', encoding='utf-8') as f:
                texto = f.read()
        except UnicodeDecodeError:
            try:
                with open(caminho_completo, 'r', encoding='latin1') as f:
                    texto = f.read()
            except Exception as e:
                print(f"[Aviso] Ignorado (erro de leitura): {caminho_completo} ({e})")
                continue
        except Exception as e:
            print(f"[Erro] Ignorado: {caminho_completo} ({e})")
            continue

        conteudo += f"\n### Arquivo: {os.path.basename(caminho_completo)}\n{texto}\n"
        arquivos_lidos += 1

    print(f"[Info] Total de arquivos lidos e incluídos no contexto: {arquivos_lidos}")
    return conteudo
