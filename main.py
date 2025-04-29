from telegram.ext import ApplicationBuilder, CommandHandler

# Importe as funções dos outros comandos
from commands.start import start
from commands.comandos import comandos
from commands.socialfuria import social_furia
from commands.loja import loja_furia
from commands.titulos import titulos_furia

# Importe a funções lineup do arquivo commands
from commands.cs import lineup_cs
from commands.valorant import lineup_valorant
from commands.lol import lineup_lol
from commands.r6 import lineup_r6
from commands.pubg import lineup_pubg
from commands.rocketleague import lineup_rocket

def main():
    app = ApplicationBuilder().token("7693528871:AAHzgO0id6wpgvtf8RxVRnog80vsz-pxP3Q").build()

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


    print("Bot da FURIA está rodando... (Pressione Ctrl+C para parar)")
    app.run_polling()

if __name__ == '__main__':
    main()