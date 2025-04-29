from telegram import Update
from telegram.ext import ContextTypes

# Comando /pubg
async def lineup_pubg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_lineup = [
        ("🇧🇷", "guizeraa"),
        ("🇧🇷", "Haven"),
        ("🇧🇷", "possa"),
        ("🇧🇷", "zkrakeN"),
    ]
    lineup_str = "⚔️ **Lineup atual da FURIA PUBG:**\n"
    for flag, player in current_lineup:
        lineup_str += f"{flag} {player}\n"

    next_game_info = "🗓️ Você pode acompanhar a agenda dos próximos jogos e o histórico de partidas da FURIA aqui: [ggscore - Próximos Jogos](https://ggscore.com/en/pubg/team/furia-esports)"

    response = f"{lineup_str}\n{next_game_info}"
    await update.message.reply_text(response, parse_mode="Markdown", disable_web_page_preview=True)