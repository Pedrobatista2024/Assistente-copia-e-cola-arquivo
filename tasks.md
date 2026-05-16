# Lista de Tarefas (tasks.md) - Assistente de Injeção de Código

## [ ] Fase 1: Configuração e Infraestrutura Inicial
* **Tarefa 1.1:** Inicializar o ambiente Python no lado do Windows e instalar as dependências de automação (`keyboard`, `pynput`, `pyautogui`).
* **Tarefa 1.2:** Criar o mecanismo de leitura e escrita do arquivo `config.json` para persistir o caminho do diretório selecionado pelo usuário.

## [ ] Fase 2: Captura de Eventos e Interface Gráfica (GUI)
* **Tarefa 2.1:** Construir o listener em segundo plano para capturar o atalho global de teclado `Ctrl + Shift + I`.
* **Tarefa 2.2:** Desenvolver a interface visual da "lupa de pesquisa" usando a biblioteca gráfica escolhida.
* **Tarefa 2.3:** Implementar o componente de árvore de arquivos (estilo VS Code) capaz de mapear o diretório salvo (incluindo o suporte para ler caminhos do WSL `\\wsl.localhost\Ubuntu\...`).

## [ ] Fase 3: Regras de Negócio e Filtragem
* **Tarefa 3.1:** Implementar o mecanismo de busca textual para filtrar os arquivos da árvore em tempo real pelo nome.
* **Tarefa 3.2:** Desenvolver o sistema de seleção múltipla (caixas de seleção) para permitir marcar mais de um arquivo sequencialmente.

## [ ] Fase 4: Leitura e Injeção de Contexto
* **Tarefa 4.1:** Criar a função de leitura de arquivos textuais com tratamento de erro básico para arquivos binários ou excessivamente grandes.
* **Tarefa 4.2:** Implementar a formatação de saída que envelopa o conteúdo de cada arquivo selecionado em blocos Markdown contendo a identificação do caminho relativo.
* **Tarefa 4.3:** Construir a rotina de automação para ocultar a interface, devolver o foco para a janela anterior do sistema e injetar/digitar o texto formatado diretamente no campo ativo.
