# 🚀 Assistente de Injeção de Código (Universal Context Injector)

Fala, dev! Se você já passou horas programando com Inteligência Artificial e ficou cansado de sofrer com o famoso *Vibe Coding* — abrindo pasta por pasta, copiando o código de três ou quatro arquivos na mão para tentar dar contexto pro ChatGPT, Claude ou Gemini —, essa ferramenta é o seu xeque-mate definitivo.

O **Assistente de Injeção de Código** é um utilitário de produtividade fantasma que roda em segundo plano no Windows. Com um único atalho global de teclado, ele abre uma lupa de pesquisa instantânea centralizada na sua tela. Você navega pelas pastas do seu projeto (seja no disco local *C:* ou dentro do seu ecossistema Linux no **WSL**), seleciona os arquivos que quer enviar em lote usando a barra de espaço, e o assistente envelopa tudo, joga na área de transferência e faz o `Ctrl + V` automático direto no campo de texto onde você estava digitando!

Tudo isso sem deixar nenhuma janela preta de terminal poluindo o seu monitor. É ligar o PC e focar no código.

---

## ⚡ Funcionalidades Insanas

* **Gatilho Global Limpo (`Ctrl + Shift + Alt + I`):** Atalho customizado e blindado contra conflitos com o Google Chrome ou outros navegadores. Funciona com o assistente oculto na bandeja do sistema.
* **Navegação Portátil de Cliques (WSL + Windows):** Suporte nativo completo para ler o caminho de rede `\\\\wsl.localhost\\Ubuntu`. O seletor gráfico de pastas abre no coração do Linux permitindo duplo clique funcional nas subpastas sem quebrar.
* **Seleção Múltipla Ordenada por Prioridade:** Pressione `Espaço` na tabela de arquivos para selecionar mais de um arquivo ao mesmo tempo. A interface insere tags numéricas automáticas como `[1] arquivo.py`, `[2] config.json`, definindo exatamente a ordem em que os códigos serão injetados para a IA.
* **Filtro Avançado com Lupa de Busca:** Pesquisa textual instantânea em tempo real que ajuda a diferenciar arquivos homônimos (como múltiplos `index.js` ou `styles.css`) mostrando seus caminhos relativos de pastas.
* **Persistência Dinâmica de Estado:** Suas configurações e caminhos de projetos são salvos de forma assíncrona em um arquivo local `config.json`. O utilitário lembra a última pasta aberta a cada boot do sistema operacional, removendo o atrito de reconfiguração manual.
* **Comportamento de Serviço Nativo (Trava do X Vermelho):** Clicar no botão fechar (X) da janela gráfica não mata o monitor de teclado em background. O script intercepta o protocolo e apenas oculta a tela, mantendo o assistente pronto na memória RAM para o próximo atalho.

---

## 🧠 Como a Mágica Acontece: Arquitetura Híbrida

Para o assistente ter controle total de automação de UI (simular digitação rápida, focar janelas de navegadores e escutar o teclado em nível de kernel), o interpretador principal do Python roda diretamente no ecossistema do **Windows**.

No entanto, o script foi projetado para ser totalmente **agnóstico a caminhos**. Ele se conecta à ponte de rede virtual do WSL, realizando varreduras rápidas (`os.walk`) e indexações de arquivos textuais dentro do Ubuntu. 

Durante a inicialização do computador, criamos uma **blindagem contra quedas de rede**. O inicializador silencioso em VBScript possui um ciclo de teste com tolerância a falhas que espera pacientemente por até 90 segundos o carregamento completo dos serviços de rede do Linux para disparar o assistente sem travar ou gerar erros invisíveis de boot.

---

