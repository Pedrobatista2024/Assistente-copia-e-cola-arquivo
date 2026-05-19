# Especificação do Projeto (spec.md) - Assistente de Injeção de Código

## 1. Objetivo do Sistema
Facilitar o envio de contexto de código para Inteligências Artificiais, permitindo que o desenvolvedor busque, filtre e selecione múltiplos arquivos de um projeto local diretamente no campo de texto ativo do navegador ou chat, por meio de um atalho global de teclado, eliminando o processo manual de copiar e colar.

## 2. Requisitos Funcionais (RF)
* **RF01 - Atalho de Teclado Global Blindado:** O sistema deve escutar o atalho global `Ctrl + Shift + Alt + I` em segundo plano para evitar conflitos com ferramentas nativas do Google Chrome e outras IDEs.
* **RF02 - Seletor Portátil de Diretórios:** O sistema deve permitir a escolha visual da pasta do projeto. O seletor gráfico de pastas deve abrir de forma inteligente no volume do Ubuntu (`\\wsl.localhost\Ubuntu`) caso ele esteja disponível, garantindo o duplo clique funcional em subpastas, ou cair em `C:\` como fallback.
* **RF03 - Filtro Instantâneo de Busca:** Deve haver uma barra de pesquisa textual (lupa) que filtra os arquivos listados em tempo real à medida que o usuário digita.
* **RF04 - Seleção Múltipla Ordenada por Prioridade:** O usuário deve conseguir marcar vários arquivos usando a tecla `Espaço`. A interface deve exibir de forma visível uma tag numérica de prioridade (ex: `[1] arquivo.py`, `[2] spec.md`), definindo a ordem de junção.
* **RF05 - Atualização Dinâmica e Redesenho de Tela:** Ao alterar a pasta de trabalho, a interface gráfica deve ignorar os atrasos de escrita física do HD e recarregar os arquivos diretamente na visualização gráfica de forma instantânea.
* **RF06 - Injeção Automatizada Ativa:** Ao confirmar com `Enter`, o sistema deve fechar a interface, concatenar o conteúdo dos arquivos selecionados em blocos Markdown estruturados com seus caminhos relativos, jogar os dados na Área de Transferência e simular um comando de colagem rápida (`Ctrl + V`) no elemento que estava focado.

## 3. Regras de Negócio (RN)
* **RN01 - Persistência Assíncrona de Diretório:** O usuário só mapeia o projeto uma única vez. O arquivo `config.json` deve registrar o caminho para alimentar automaticamente os próximos boots do sistema.
* **RN02 - Interceptação do Botão Fechar (X):** O clique no botão (X) vermelho da janela é interceptado pelo protocolo de sistema para apenas ocultar a interface via memória RAM (`withdraw`), mantendo o monitor de teclado ativo em background.