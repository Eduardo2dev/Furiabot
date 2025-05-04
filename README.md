# README do Projeto FURIA Fan Bot

Este README fornece uma visão geral do projeto FURIA Fan Bot, um bot para Telegram desenvolvido como parte do Desafio #1 da FURIA no processo seletivo de estágio em Engenharia de Software. O objetivo principal do bot é facilitar o acesso rápido, simples e divertido às informações relevantes da organização FURIA para seus fãs diretamente no Telegram.

## Visão Geral do Projeto

O FURIA Fan Bot é uma experiência conversacional criada para engajar a comunidade de fãs da FURIA, fornecendo acesso fácil a:

- Informações dos Times: Resultados de partidas, próximos jogos, elencos.
- Redes Sociais: Links diretos para as páginas oficiais da FURIA.
- Loja Oficial: Acesso à loja para adquirir produtos da organização.
- Títulos Conquistados: Histórico de conquistas da FURIA.
- Quiz Interativo: Um quiz para testar o conhecimento dos fãs sobre a FURIA.
- Informações sobre a participação da FURIA na Kings League.

Para complementar a experiência, foi desenvolvida uma landing page simples que redireciona os usuários diretamente para o bot no Telegram, servindo como um ponto de entrada intuitivo para o projeto.

## Tecnologias Utilizadas

- Linguagem de Programação: Python
- Biblioteca Telegram Bot: `python-telegram-bot`

## Como Utilizar o FURIA Fan Bot

1. **Acesso via Telegram:** Abra o aplicativo Telegram e procure por `FURIA fan bot` (ou clique no link da landing page, se disponível).
2. **Iniciar o Bot:** Envie o comando `/start` ou toque no botão "Iniciar" (se fornecido pelo Telegram).
3. **Explorar os Comandos:** Após iniciar, o bot exibirá uma mensagem de boas-vindas e sugerirá o uso do comando `/comandos` para visualizar todas as funcionalidades disponíveis.
4. **Interagir:** Utilize os comandos listados abaixo diretamente na janela de chat com o bot para obter as informações desejadas. Siga as instruções do bot para navegar e interagir com o quiz.

## Comandos Disponíveis

* `/cs` - Exibe a lineup atual da equipe de Counter-Strike 2.
* `/valorant` - Mostra a lineup atual da equipe de Valorant.
* `/lol` - Apresenta a lineup atual da equipe de League of Legends.
* `/r6` - Informa a lineup atual da equipe de Rainbow Six.
* `/pubg` - Exibe a lineup atual da equipe de PUBG.
* `/rocketleague` - Mostra a lineup atual da equipe de Rocket League.
* `/kingsleague` - Fornece informações sobre a participação da FURIA na Kings League.
* `/socialfuria` - Lista os links para as redes sociais oficiais da FURIA.
* `/loja` - Oferece um link direto para acessar a loja oficial da FURIA.
* `/titulos` - Exibe os títulos conquistados pela organização FURIA.
* `/quizfuria` - Inicia um quiz para testar seus conhecimentos sobre a FURIA.

## Landing Page

Uma landing page simples foi criada para facilitar o acesso ao FURIA Fan Bot. A página contém uma breve descrição do bot e um link direto para iniciá-lo no Telegram.

- Link da Landing Page: `https://furiabothtml.vercel.app/`

## Estrutura do Código

O projeto é estruturado da seguinte forma:

furia_fan_bot/
├── assets/         # Organizar código em pastas para melhor modularidade
├── commands/       # feat: adicionado o comando /quiz
├── templates/      # Organizar código em pastas para melhor modularidade
├── .gitignore      # Feat escondendo token bot
├── main.py         # Feat escondendo token bot
└── requirements.txt # feat: Adiciona dependência python-dotenv ao requirements....

## Próximos Passos e Melhorias Futuras

Aqui você pode listar possíveis melhorias ou funcionalidades que você planeja adicionar no futuro, como:

- Notificações de jogos em tempo real.
- Integração com outras plataformas.
- Personalização das informações para o usuário.
- Expansão do quiz com mais perguntas e categorias.

## Contato

- **Nome:** Eduardo Nazario
- **Email:** eduardonazario74@gmail.com
- **LinkedIn (Opcional):** https://www.linkedin.com/in/eduardo-nazario-898973282/
