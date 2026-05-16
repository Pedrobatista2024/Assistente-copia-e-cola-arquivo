# Constituição do Projeto: Assistente de Injeção de Código

## Princípios Gerais
1. Simplicidade e leveza: O assistente deve abrir instantaneamente ao comando do atalho.
2. Segurança: O aplicativo só lê os arquivos locais da pasta explicitamente autorizada pelo usuário.

## Restrições de Arquitetura e Tecnologia
1. Multiplataforma / Suporte Windows: Como o ambiente final é Windows, o app deve ser construído usando uma tecnologia que permita registrar atalhos globais de teclado no sistema operacional e simular digitação (ex: Electron, Tauri com Rust/Frontend, ou Python com bibliotecas nativas de automação de UI).
2. Persistência de Estado: O caminho da pasta selecionada pelo usuário deve ser salvo em um arquivo de configuração local (ex: JSON ou SQLite leve) para que o usuário precise mapear o diretório apenas uma vez.
3. Injeção Direta: O envio de código deve simular a digitação ou usar APIs de automação do sistema operacional para inserir o bloco de texto diretamente no campo de input que estiver com o foco ativo no momento da confirmação.

## Padrões de Código
1. Clean Code e funções de responsabilidade única.
2. Tratamento estrito de erros para arquivos grandes ou não textuais (binários/imagens).
