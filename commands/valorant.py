from telegram import Update
from telegram.ext import ContextTypes

# Comando /valorant
async def lineup_valorant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_lineup = [
        ("🇧🇷", "khalil"),
        ("🇧🇷", "heat"),
        ("🇧🇷", "havoc"),
        ("🇧🇷", "raafa "),
        ("🇧🇷", "pryze")
    ]
    lineup_str = "⚔️ **Lineup atual da FURIA VALORANT:**\n"
    for flag, player in current_lineup:
        lineup_str += f"{flag} {player}\n"

    next_game_info = "🗓️ Você pode acompanhar a agenda dos próximos jogos e o histórico de partidas da FURIA aqui: [valorantzone.gg - Próximos Jogos](https://valorantzone.gg/equipe/furia-esports/)"
    link_instagram_valorant = "📸 Siga nosso time de Valorant no Instagram: [Clique aqui](https://www.instagram.com/furia.valorant/?hl=pt-br)"
    link_youtube_valorant = "▶️ Siga nosso time de Valorant no Youtube [Clique aqui](https://www.youtube.com/@FURIAggVAL/videos)"

    response = f"{lineup_str}\n{next_game_info}\n\n{link_instagram_valorant}\n{link_youtube_valorant}"
    await update.message.reply_text(response, parse_mode="Markdown", disable_web_page_preview=True)