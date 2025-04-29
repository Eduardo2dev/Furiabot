from telegram import Update
from telegram.ext import ContextTypes

#comando /loja
async def loja_furia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loja_url = "https://www.furia.gg/"  # URL da loja oficial da FURIA
    mensagem = f"🛒 **Se liga na Loja Oficial da FURIA:**\n\nEncontre camisetas, acessórios e os produtos mais irados para se tornar um verdadeiro Furioso(a):\n{loja_url}"
    await update.message.reply_text(mensagem, parse_mode="Markdown", disable_web_page_preview=True)