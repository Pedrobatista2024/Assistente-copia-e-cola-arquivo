# Lista de Tarefas (tasks.md) - Assistente de Injeção de Código

## [X] Fase 1: Configuração e Infraestrutura Inicial
* **Tarefa 1.1:** Inicializar o ambiente Python no lado do Windows e instalar as dependências de automação (`keyboard`, `pyautogui`, `pyperclip`).
* **Tarefa 1.2:** Desenvolver o módulo isolado de persistência de dados `config_manager.py` com funções de leitura e escrita síncronas do arquivo `config.json`.

## [X] Fase 2: Captura de Eventos e Interface Gráfica (GUI)
* **Tarefa 2.1:** Construir o listener global em segundo plano monitorando a combinação estável `Ctrl + Shift + Alt + I`.
* **Tarefa 2.2:** Desenvolver a interface visual da "lupa de pesquisa" com design Dark Mode usando frames estruturados no Tkinter.
* **Tarefa 2.3:** Criar a função híbrida de mapeamento portátil de diretórios capaz de realizar fallbacks automáticos entre o Ubuntu (`\\wsl.localhost\Ubuntu`) e o disco local do Windows (`C:\`).

## [X] Fase 3: Regras de Negócio e Filtragem
* **Tarefa 3.1:** Desenvolver o algoritmo de busca em tempo real com gatilhos de evento `<KeyRelease>` atrelados à caixa de entrada da lupa.
* **Tarefa 3.2:** Implementar o sistema de seleção customizada via tecla `Espaço`, gerenciando a matriz global `ORDEM_SELECAO` e renderizando os índices dinâmicos de prioridade na tela.
* **Tarefa 3.3:** Adicionar a interceptação de fechamento da janela gráfica no protocolo `WM_DELETE_WINDOW` para redirecionar o clique do X vermelho para a função oculta `withdraw`.

## [X] Fase 4: Leitura, Injeção e Inicialização Oculta no Boot
* **Tarefa 4.1:** Desenvolver o extrator textual de arquivos com proteção contra falhas e envelopamento customizado em blocos Markdown.
* **Tarefa 4.2:** Integrar a rotina de injeção automática combinando a limpeza de tela, cópia de clipboard e disparo de hotkey de hardware (`Ctrl + V`).
* **Tarefa 4.3:** Escrever o script inicializador silencioso em VBScript blindado com travas de loop de 90 segundos e ignoranciamento de erros de montagem de rede no boot do Windows.