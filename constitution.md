# Constituição do Projeto: Assistente de Injeção de Código

## Princípios Gerais
1. Simplicidade e leveza: O assistente deve abrir instantaneamente ao comando do atalho de teclado global.
2. Segurança e Privacidade: O aplicativo só lê os arquivos locais da pasta explicitamente autorizada pelo usuário através da interface de seleção.
3. Persistência de Serviço: O programa deve rodar de forma invisível em segundo plano sem poluir o ambiente visual do usuário com terminais abertos.

## Restrições de Arquitetura e Tecnologia
1. Sistema Operacional Alvo: Windows Nativo. O app utiliza bibliotecas capazes de interagir com o kernel de eventos do Windows para escutar o teclado e injetar comandos de UI.
2. Portabilidade Híbrida (Windows + WSL): O aplicativo precisa rodar nativamente no Windows, mas deve ser capaz de ler e navegar de forma fluida tanto em diretórios locais (`C:\`) quanto em volumes de rede virtual do Linux Linux (`\\wsl.localhost\Ubuntu`).
3. Inicialização e Resiliência: O sistema deve se registrar no boot do Windows através de um script de inicialização fantasma em VBScript dotado de tolerância a falhas críticas, aguardando o carregamento da rede do WSL por até 90 segundos se necessário.
4. Persistência de Estado: O caminho mapeado pelo usuário deve ser salvo assincronamente em um arquivo leve `config.json` no diretório do script.

## Padrões de Código
1. Modularidade: Separação clara entre a lógica de I/O do arquivo de configuração (`config_manager.py`) e a interface/automação gráfica (`assistente_injecao.py`).
2. Gerenciamento de Janelas: Implementação estrita do protocolo de destruição gráfica. O clique no botão fechar (X) não pode encerrar a execução do programa; deve apenas ocultar a janela principal.
3. Robustez de Leitura: Tratamento estrito de exceções para arquivos protegidos, corrompidos ou excessivamente grandes.