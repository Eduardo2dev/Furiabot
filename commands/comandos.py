from telegram import Update
from telegram.ext import ContextTypes

# Comando /comandos
async def comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        '📋 *Lista de Comandos Disponíveis:*\n\n'
        '/cs - Lineup atual de Counter-Strike 2\n'
        '/valorant - Lineup atual de Valorant\n'
        '/lol - Lineup atual de League of Legends\n'
        '/r6 - Lineup atual de Rainbow Six\n'
        '/pubg - Lineup atual de PUBG\n'
        '/rocketleague - Lineup atual de rocket League\n'
        '/socialfuria - Redes sociais da FURIA\n'
        '/loja - Acessar a loja oficial da FURIA\n'
        '/titulos - Ver títulos conquistados\n'
        '/kingsleague - Tudo sobre a Furia na kings league'
    )

    await update.message.reply_text(texto, parse_mode='Markdown')