from telegram import Update
from telegram.ext import ContextTypes

# Comando /socialfuria
async def social_furia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    social_links = {
        "🐦 Twitter": "https://twitter.com/FURIA",
        "📸 Instagram": "https://www.instagram.com/furiagg/",
        "🎮 Twitch": "https://www.twitch.tv/furiatv",
        "📺 YouTube": "https://www.youtube.com/@FURIAgg/featured",
        "📘 Facebook": "https://www.facebook.com/furiagg",
        "🎵 TikTok": "https://www.tiktok.com/@furiagg"
    }

    response = "🔗 **Confira as Redes Sociais da FURIA:**\n\n"
    for platform, link in social_links.items():
        response += f"➡️ {platform}: [{platform} link]({link})\n"

    await update.message.reply_text(response, parse_mode="MarkdownV2", disable_web_page_preview=True)