from telegram import Update
from telegram.ext import ContextTypes

# Comando /lol
async def lineup_lol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_lineup = [
        ("🇧🇷", "Guigo"),
        ("🇧🇷", "Tatu"),
        ("🇧🇷", "Tutsz"),
        ("🇧🇷", "Ayu"),
        ("🇧🇷", "Jojo")
    ]
    lineup_str = "⚔️ **Lineup atual da FURIA LOL:**\n"
    for flag, player in current_lineup:
        lineup_str += f"{flag} {player}\n"

    next_game_info = "🗓️ Você pode acompanhar a agenda dos próximos jogos e o histórico de partidas da FURIA aqui: [Flashcore - Próximos Jogos](https://www.flashscore.com.br/equipe/furia-esports-league-of-legends/Msu28Ozt/)"

    response = f"{lineup_str}\n{next_game_info}"
    await update.message.reply_text(response, parse_mode="Markdown", disable_web_page_preview=True)