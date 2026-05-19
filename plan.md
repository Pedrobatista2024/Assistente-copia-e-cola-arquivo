# Plano Técnico (plan.md) - Assistente de Injeção de Código

## 1. Stack de Tecnologia Consolidada
* **Ambiente de Execução:** Python 3.12+ executado diretamente no interpretador do Windows.
* **Interface Gráfica (GUI):** Biblioteca nativa `Tkinter` customizada com paleta de cores escura (estilo VS Code / Dark Mode).
* **Componentes Gráficos Usados:** `Entry` para a lupa de pesquisa, `Listbox` com `Scrollbar` acoplada para renderização textual rápida dos caminhos relativos e `Button` para ações em mouse.
* **Monitoramento Global de Teclado:** Biblioteca `keyboard` acoplada diretamente ao nível de eventos do kernel do Windows para escutar a hotkey `Ctrl + Shift + Alt + I`.
* **Mecanismo de Injeção de UI:** Combinação híbrida entre as bibliotecas `pyperclip` (para transferência segura do bloco Markdown de texto para a memória coletiva da Área de Transferência) e `pyautogui` (para disparar o comando assíncrono de hardware `ctrl + v` com delay de segurança de 0.2s).
* **Persistência I/O:** Módulo nativo `json` gerenciando o estado no arquivo `config.json`.

## 2. Arquitetura do Fluxo de Dados e Inicialização
1. No boot do Windows, a pasta Inicializar dispara o arquivo `iniciar_assistente.vbs`.
2. O script VBScript executa uma rotina protegida por `On Error Resume Next`. Ele roda um loop de até 90 repetições com intervalo de 1000ms testando a existência do arquivo Python através do comando puro `.ProviderPath` do PowerShell (garantindo que o caminho comece limpo em `\\wsl.localhost\`).
3. Assim que a rede do WSL monta o volume, o Python é chamado em modo oculto (`0, False`).
4. O programa executa um ciclo rápido de aquecimento visual (`executar_warmup`) para renderizar e ocultar a janela, deixando a interface pré-carregada na memória RAM.
5. Quando o atalho é acionado, a janela acorda via `deiconify`, traz o foco para si (`focus_force`), limpa os filtros anteriores e renderiza a Listbox puxando os arquivos usando o método de varredura `os.walk`.