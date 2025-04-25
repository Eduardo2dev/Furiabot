from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🔥 BEM-VINDO AO FURIA FAN BOT! 🔥\n'
        '👊 Aqui, quem não é furioso, não é FURIA!\n'
        '💥 Fique ligado para atualizações, estatísticas e tudo o que envolve a organização mais insana do cenário!\n'
        '⚡ Entre na pele da nossa pantera e sinta a energia que vai te deixar FURIOSO!\n'
        '💬 Quer se tornar um verdadeiro furioso? Digite /comandos e descubra os atalhos para estar sempre ligado na nossa pantera!\n'
    )
# Comando /comandos
async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        '📋 *Lista de Comandos Disponíveis:*\n\n'
        '/cs - Lineup atual de Counter-Strike 2\n'
        '/valorant - Lineup atual de Valorant\n'
        '/lol - Lineup atual de League of Legends\n'
        '/r6 - Lineup atual de Rainbow Six\n'
        '/pubg - Lineup atual de PUBG\n'
        '/socialfuria - Redes sociais da FURIA\n'
        '/loja - Acessar a loja oficial da FURIA\n'
        '/titulos - Ver títulos conquistados\n'
    )

    await update.message.reply_text(texto, parse_mode='Markdown')


def main():
    app = ApplicationBuilder().token("7693528871:AAHzgO0id6wpgvtf8RxVRnog80vsz-pxP3Q").build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('texto', comandos))

    print('Bot FURIA está rodando!')
    app.run_polling()

if __name__ == '__main__':
    main()