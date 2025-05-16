from telegram import Update
from telegram.ext import ContextTypes

# Comando /cs
async def lineup_cs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_lineup = [
        ("🇧🇷", "yuurih"),
        ("🇧🇷", "FalleN"),
        ("🇧🇷", "KSCERATO"),
        ("🇱🇻", "YEKINDAR"),
        ("🇰🇿", "molodoy")
    ]
    lineup_str = "⚔️ **Lineup atual da FURIA CS:**\n"
    for flag, player in current_lineup:
        lineup_str += f"{flag} {player}\n"

    next_game_info = "🗓️ Você pode acompanhar a agenda dos próximos jogos e o histórico de partidas da FURIA aqui: [HLTV - Próximos Jogos](https://www.hltv.org/team/8297/furia#tab-matchesBox)"

    response = f"{lineup_str}\n{next_game_info}"
    await update.message.reply_text(response, parse_mode="Markdown", disable_web_page_preview=True)