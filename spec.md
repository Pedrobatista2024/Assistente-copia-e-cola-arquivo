# Especificação do Projeto (spec.md) - Assistente de Injeção de Código

## 1. Objetivo do Sistema
Facilitar o envio de contexto de código para Inteligências Artificiais, permitindo que o desenvolvedor busque, selecione e injete múltiplos arquivos de um projeto local diretamente no campo de texto ativo do navegador ou chat, por meio de um atalho global de teclado, eliminando o processo manual de copiar e colar.

## 2. Requisitos Funcionais (RF)
* **RF01 - Atalho de Teclado Global:** O sistema deve escutar um atalho configurável (ex: `Ctrl + Shift + I`) que funciona mesmo se o aplicativo estiver rodando em segundo plano.
* **RF02 - Seleção de Pasta de Trabalho:** Na primeira execução, o usuário deve selecionar a pasta raiz do projeto. O sistema deve memorizar esse caminho de forma persistente.
* **RF03 - Navegação em Árvore de Arquivos:** A interface deve exibir uma estrutura visual de arquivos em árvore (estilo barra lateral do VS Code) para permitir a abertura de subpastas específicas.
* **RF04 - Busca de Arquivos por Nome:** Deve haver uma barra de pesquisa (lupa) para filtrar arquivos rapidamente pelo nome, ajudando a diferenciar arquivos homônimos (ex: múltiplos `index.js`) através da exibição do caminho relativo da pasta.
* **RF05 - Seleção Múltipla:** O usuário deve ser capaz de selecionar um ou mais arquivos simultaneamente antes de confirmar a operação.
* **RF06 - Injeção Direta de Texto:** Ao confirmar a seleção, o sistema deve fechar a interface de busca, ler o conteúdo dos arquivos e digitá-los/injetá-los automaticamente no campo de entrada de texto que estava focado antes do acionamento.

## 3. Regras de Negócio (RN)
* **RN01 - Persistência do Diretório:** O usuário só precisa selecionar a pasta do projeto uma única vez. Nas próximas ativações do atalho, a interface já deve abrir diretamente exibindo a árvore daquela pasta salva, a menos que ele solicite explicitamente a alteração do diretório.
* **RN02 - Formatação da Injeção:** Os arquivos selecionados devem ser injetados contendo uma marcação clara de identificação para a IA externa (ex: nome do arquivo e caminho, seguido pelo código envelopado em blocos de Markdown).
