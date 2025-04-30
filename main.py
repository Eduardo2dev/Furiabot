from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

# Importe as funções dos outros comandos
from commands.start import start
from commands.comandos import comandos
from commands.socialfuria import social_furia
from commands.loja import loja_furia
from commands.titulos import titulos_furia
from commands.kingsleague import kings_league
from commands.furiaquiz import quizfuria, responder_pergunta

# Importe a funções lineup do arquivo commands
from commands.cs import lineup_cs
from commands.valorant import lineup_valorant
from commands.lol import lineup_lol
from commands.r6 import lineup_r6
from commands.pubg import lineup_pubg
from commands.rocketleague import lineup_rocket

#Exibe mensagem para comandos desconhecidos
async def desconhecido_comando(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Desculpe, esse comando não existe. Use /comandos para ver a lista de comandos disponíveis.")

async def desconhecido_texto(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Desculpe, não entendi essa mensagem. Use /comandos para ver a lista de comandos disponíveis.")

def main():
    app = ApplicationBuilder().token("7907523943:AAEDHcRA76iTraAWLgQfkVJ3WGXdIF4OyhI").build()

     # Adiciona um handler para os comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("comandos", comandos))
    app.add_handler(CommandHandler("cs", lineup_cs))
    app.add_handler(CommandHandler("valorant", lineup_valorant))
    app.add_handler(CommandHandler("lol", lineup_lol))
    app.add_handler(CommandHandler("r6", lineup_r6))
    app.add_handler(CommandHandler("pubg", lineup_pubg))
    app.add_handler(CommandHandler("socialfuria", social_furia))
    app.add_handler(CommandHandler("loja", loja_furia))
    app.add_handler(CommandHandler("titulos", titulos_furia))
    app.add_handler(CommandHandler("rocketleague", lineup_rocket))
    app.add_handler(CommandHandler("kingsleague", kings_league))

    #adiciona um handler para o comando quiz
    app.add_handler(CommandHandler("quizfuria", quizfuria))
    app.add_handler(CallbackQueryHandler(responder_pergunta, pattern="^resposta_"))

    # Este handler captura comandos desconhecidos (começam com '/')
    app.add_handler(MessageHandler(filters.COMMAND, desconhecido_comando))

    # Este handler captura texto que não é comando
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, desconhecido_texto))


    print("Bot da FURIA está rodando... (Pressione Ctrl+C para parar)")
    app.run_polling()

if __name__ == '__main__':
    main()