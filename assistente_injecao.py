import os
import sys
import time

# ==============================================================================
# --- TRAVA DE SEGURANÇA: CORREÇÃO DE DIRETÓRIO DE TRABALHO (CWD) ---
# ==============================================================================
diretorio_script = os.path.dirname(os.path.abspath(__file__))
# Aguarda até 30 segundos caso a rede do WSL esteja instável no boot do PC
for _ in range(30):
    if os.path.exists(diretorio_script):
        break
    time.sleep(1)

os.chdir(diretorio_script)
# ==============================================================================

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog  
import keyboard
import pyperclip  
import pyautogui   
from config_manager import load_config, save_config  

# Variáveis globais de estado interno
ARQUIVOS_COMPLETOS = []
ARQUIVOS_VISUAIS = []
ORDEM_SELECAO = []

# Componentes da interface gráfica
root = None
entry_pesquisa = None
listbox_arquivos = None

def listar_arquivos_reais(diretorio_custom=None):
    """Varre a pasta mapeando os caminhos (aceita caminho direto ou lê do config.json)."""
    if diretorio_custom is not None:
        diretorio = diretorio_custom
    else:
        config = load_config()
        diretorio = config.get("default_directory", "")
        
    if not diretorio or not os.path.exists(diretorio):
        return []
    
    lista_arquivos = []
    for raiz, pastas, arquivos in os.walk(diretorio):
        if "__pycache__" in raiz or ".git" in raiz:
            continue
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            caminho_relativo = os.path.relpath(caminho_completo, diretorio)
            lista_arquivos.append(caminho_relativo)
    return lista_arquivos

def atualizar_lista_visual():
    """Filtra e renderiza os itens na tela com os números de prioridade."""
    global ARQUIVOS_VISUAIS
    texto_busca = entry_pesquisa.get().lower()
    listbox_arquivos.delete(0, tk.END)
    ARQUIVOS_VISUAIS = []
    
    for item in ARQUIVOS_COMPLETOS:
        if texto_busca in item.lower():
            ARQUIVOS_VISUAIS.append(item)
            if item in ORDEM_SELECAO:
                num_prioridade = ORDEM_SELECAO.index(item) + 1
                listbox_arquivos.insert(tk.END, f"[{num_prioridade}] {item}")
            else:
                listbox_arquivos.insert(tk.END, item)

def filtrar_arquivos(event):
    atualizar_lista_visual()

def descer_para_lista(event):
    if listbox_arquivos.size() > 0:
        listbox_arquivos.focus_set()
        listbox_arquivos.select_set(0)
        listbox_arquivos.activate(0)

def alternar_selecao_customizada(event):
    global ORDEM_SELECAO
    selecao_atual = listbox_arquivos.curselection()
    if not selecao_atual:
        return "break"
        
    index_visual = selecao_atual[0]
    arquivo_alvo = ARQUIVOS_VISUAIS[index_visual]
    
    if arquivo_alvo in ORDEM_SELECAO:
        ORDEM_SELECAO.remove(arquivo_alvo)
    else:
        ORDEM_SELECAO.append(arquivo_alvo)
        
    atualizar_lista_visual()
    listbox_arquivos.select_set(index_visual)
    listbox_arquivos.activate(index_visual)
    return "break"

def alterar_diretorio_interface():
    """Abre dentro do volume do Linux de forma portátil, permitindo duplo clique funcional."""
    global ARQUIVOS_COMPLETOS, ORDEM_SELECAO
    config = load_config()
    diretorio_atual = config.get("default_directory", "")
    
    if diretorio_atual and os.path.exists(diretorio_atual):
        ponto_partida = os.path.dirname(diretorio_atual)
    else:
        if os.path.exists("\\\\wsl.localhost\\Ubuntu"):
            ponto_partida = "\\\\wsl.localhost\\Ubuntu"
        elif os.path.exists("\\\\wsl.localhost\\"):
            ponto_partida = "\\\\wsl.localhost\\"
        else:
            ponto_partida = "C:\\"  

    nova_pasta = filedialog.askdirectory(title="Selecione a Nova Pasta do Projeto", initialdir=ponto_partida)
    if nova_pasta:
        nova_pasta = os.path.normpath(nova_pasta)
        save_config(nova_pasta)
        
        ORDEM_SELECAO = []
        entry_pesquisa.delete(0, tk.END)
        
        ARQUIVOS_COMPLETOS = listar_arquivos_reais(nova_pasta)
        atualizar_lista_visual()
        
        root.update()
        entry_pesquisa.focus_force()

def confirmar_e_copiar(event=None):
    """Processa os arquivos, oculta a interface e executa o Ctrl+V automático."""
    config = load_config()
    diretorio_raiz = config.get("default_directory", "")
    if not ORDEM_SELECAO:
        root.withdraw()
        return

    texto_final_contexto = ""
    for arquivo_relativo in ORDEM_SELECAO:
        caminho_absolute = os.path.join(diretorio_raiz, arquivo_relativo)
        try:
            with open(caminho_absolute, "r", encoding="utf-8") as f:
                conteudo_codigo = f.read()
            texto_final_contexto += f"{arquivo_relativo}\n{conteudo_codigo}\n\n"
        except Exception as e:
            print(f"[ERRO] Falha ao ler '{arquivo_relativo}': {e}")

    pyperclip.copy(texto_final_contexto)
    root.withdraw()
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'v')

def acionar_hotkey():
    root.after(0, acordar_janela)

def acordar_janela():
    global ORDEM_SELECAO, ARQUIVOS_COMPLETOS
    ORDEM_SELECAO = [] 
    entry_pesquisa.delete(0, tk.END) 
    ARQUIVOS_COMPLETOS = listar_arquivos_reais()
    atualizar_lista_visual()
    
    largura, altura = 600, 400
    pos_x = (root.winfo_screenwidth() // 2) - (largura // 2)
    pos_y = (root.winfo_screenheight() // 2) - (altura // 2)
    root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
    
    root.deiconify()
    root.update()                        
    root.lift()                          
    root.attributes("-topmost", True)     
    root.after(100, lambda: root.attributes("-topmost", False)) 
    root.focus_force()                   
    entry_pesquisa.focus_force()         

def executar_warmup():
    root.deiconify()
    root.update()
    root.focus_force()
    entry_pesquisa.focus_force()
    root.withdraw()
    print("[SISTEMA] Ciclo fantasma concluído com sucesso!")

def configurar_interface():
    global root, entry_pesquisa, listbox_arquivos, ARQUIVOS_COMPLETOS
    root = tk.Tk()
    root.title("Assistente de Injeção de Código")
    root.geometry("600x400-2000-2000")
    root.configure(bg="#2d2d2d")

    top_frame = tk.Frame(root, bg="#2d2d2d", padx=10, pady=10)
    top_frame.pack(fill=tk.X)
    lbl_pesquisa = tk.Label(top_frame, text="🔍 Buscar arquivo:", bg="#2d2d2d", fg="#ffffff", font=("Arial", 10, "bold"))
    lbl_pesquisa.pack(side=tk.LEFT, padx=5)
    entry_pesquisa = tk.Entry(top_frame, font=("Arial", 11), bg="#3d3d3d", fg="#ffffff", insertbackground="white", bd=1)
    entry_pesquisa.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

    middle_frame = tk.Frame(root, bg="#2d2d2d", padx=10, pady=5)
    middle_frame.pack(fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(middle_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox_arquivos = tk.Listbox(
        middle_frame, font=("Consolas", 10), bg="#1e1e1e", fg="#d4d4d4",
        selectbackground="#007acc", selectmode=tk.BROWSE, yscrollcommand=scrollbar.set, bd=0
    )
    listbox_arquivos.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox_arquivos.yview)

    bottom_frame = tk.Frame(root, bg="#2d2d2d", padx=10, pady=10)
    bottom_frame.pack(fill=tk.X)
    
    btn_mudar_pasta = tk.Button(bottom_frame, text="🔄 Mudar Pasta", bg="#4d4d4d", fg="#ffffff", font=("Arial", 10), bd=0, command=alterar_diretorio_interface)
    btn_mudar_pasta.pack(side=tk.LEFT, padx=5)

    btn_confirmar = tk.Button(bottom_frame, text="Injetar Direto (Enter)", bg="#0e639c", fg="#ffffff", font=("Arial", 10, "bold"), bd=0, command=confirmar_e_copiar)
    btn_confirmar.pack(side=tk.RIGHT, padx=5)

    entry_pesquisa.bind("<KeyRelease>", lambda event: filtrar_arquivos(event))
    entry_pesquisa.bind("<Down>", lambda event: descer_para_lista(event))
    listbox_arquivos.bind("<space>", lambda event: alternar_selecao_customizada(event))
    root.bind("<Return>", lambda event: confirmar_e_copiar(event))

    # AQUI ESTÁ A LINHA CORRIGIDA SEM NENHUM CARACTERE VAZADO:
    root.protocol("WM_DELETE_WINDOW", lambda: root.withdraw())

    ARQUIVOS_COMPLETOS = listar_arquivos_reais()
    atualizar_lista_visual()
    root.withdraw() 
    root.after(100, executar_warmup)
    root.mainloop()

if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+shift+alt+i', acionar_hotkey)
    configurar_interface()
