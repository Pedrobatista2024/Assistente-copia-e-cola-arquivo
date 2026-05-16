# Plano Técnico (plan.md) - Assistente de Injeção de Código

## 1. Stack de Tecnologia Proposta
* **Linguagem Principal:** Python 3.12 (Executado no lado do Windows para ter acesso total às APIs de interface gráfica e simulação de teclado).
* **Interface Gráfica (GUI):** `Tkinter` (nativo, leve e abre instantaneamente) ou `PyQt`/`CustomTkinter` para uma estética moderna estilo "lupa de pesquisa".
* **Captura de Atalhos Globais:** Biblioteca `keyboard` ou `pynput` para escutar o comando `Ctrl + Shift + I` em segundo plano no Windows.
* **Automação de Injeção de Texto:** Biblioteca `pyautogui` ou `keyboard` para simular a digitação rápida, ou manipulação da Área de Transferência combinada com um comando de colagem automático (`Ctrl + V`).
* **Persistência de Dados:** Arquivo de configuração simples em formato JSON (`config.json`) para salvar o caminho do diretório padrão do usuário.

## 2. Arquitetura do Fluxo de Dados
1. O script inicia em segundo plano (background) no Windows e lê o arquivo `config.json`.
2. Quando o atalho `Ctrl + Shift + I` é acionado, o script identifica qual janela/campo de texto estava ativo e abre a interface gráfica.
3. A interface lê a árvore de diretórios do projeto (seja um caminho local do Windows ou o caminho de rede do WSL `\\wsl.localhost\Ubuntu\...`).
4. O usuário digita o filtro na barra de pesquisa, seleciona os arquivos desejados na árvore estruturada e clica em "Confirmar".
5. O programa lê o conteúdo textual dos arquivos selecionados, fecha a interface gráfica, devolve o foco para a janela anterior e injeta o texto formatado em blocos Markdown.
