import json
import os

CONFIG_FILE = "config.json"

def load_config():
    """Lê o arquivo JSON de configuração se ele existir."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao ler configuração: {e}")
            return {}
    return {}

def save_config(directory_path):
    """Salva ou atualiza o caminho do diretório no arquivo JSON."""
    config = load_config()
    config["default_directory"] = directory_path
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        print(f"[SUCESSO] Configuração gravada! Diretório salvo: {directory_path}")
    except Exception as e:
        print(f"[ERRO] Falha ao salvar configuração: {e}")

if __name__ == "__main__":
    print("--- Testando Mecanismo de Persistência (Tarefa 1.2) ---")
    
    
    caminho_teste = r"\\wsl.localhost\Ubuntu\home\pedro\projetos\meu_projeto_estruturado"
    
    # Executando a escrita
    save_config(caminho_teste)
    
    
    configuracao_carregada = load_config()
    print(f"[VALIDAÇÃO] Lido do JSON: {configuracao_carregada.get('default_directory')}")