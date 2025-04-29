from telegram import Update
from telegram.ext import ContextTypes

# Comando /r6
async def lineup_r6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_lineup = [
        ("🇧🇷", "FelipoX"),
        ("🇧🇷", "HerdsZ"),
        ("🇧🇷", "Jv92"),
        ("🇧🇷", "Kheyze"),
        ("🇧🇷", "nade")
    ]
    lineup_str = "⚔️ **Lineup atual da FURIA R6:**\n"
    for flag, player in current_lineup:
        lineup_str += f"{flag} {player}\n"

    next_game_info = "🗓️ Você pode acompanhar a agenda dos próximos jogos e o histórico de partidas da FURIA aqui: [Ubisoft - Próximos Jogos](https://www.ubisoft.com/pt-br/esports/rainbow-six/siege/team/9/schedule)"

    response = f"{lineup_str}\n{next_game_info}"
    await update.message.reply_text(response, parse_mode="Markdown", disable_web_page_preview=True)