from telegram import Update
from telegram.ext import ContextTypes

# Comando /rocketleague
async def lineup_rocket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_lineup = [
        ("🇧🇷", "yANXNZ"),
        ("🇧🇷", "Lostt"),
        ("🇧🇷", "DRUFINHO"),
        ("🇧🇷", "STL"),
    ]
    lineup_str = "⚔️ **Lineup atual da FURIA ROCKET LEAGUE:**\n"
    for flag, player in current_lineup:
        lineup_str += f"{flag} {player}\n"

    next_game_info = "🗓️ Você pode acompanhar a agenda dos próximos jogos e o histórico de partidas da FURIA aqui: [egamersworld - Próximos Jogos](https://egamersworld.com/rocketleague/team/furia-esports-V1dH3ESEc)"

    response = f"{lineup_str}\n{next_game_info}"
    await update.message.reply_text(response, parse_mode="Markdown", disable_web_page_preview=True)