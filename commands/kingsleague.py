from telegram import Update
from telegram.ext import ContextTypes

async def kings_league(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link_geral = "https://kingsleague.pro/pt/times/50-furia-fc"
    link_regras = "https://cms-br.kingsleague.pro/wp-content/uploads/2025/03/KLQL-reglamento-20250416.pdf"
    link_social_furia_kl = "https://www.instagram.com/furia.football/"
    
    texto = (
        "*Kings League Brasil - Informações da Nossa Pantera:*  👑⚽\n\n"
        f"Acompanhe a classificação, resultados e próximos jogos da FURIA:\n"
        f"➡️ [Clique aqui para acessar]({link_geral})\n\n"
        f"Consulte o regulamento completo da Kings League:\n"
        f"📜 [Clique aqui para ver as regras]({link_regras})\n\n"
        f"*Siga a FURIA FC no Instagram* para ficar por dentro de tudo:\n"
        f"📸 [Clique aqui para acessar]({link_social_furia_kl})\n\n"
        "Mantenha-se atualizado sobre a Kings League!"
    )
    await update.message.reply_text(texto, parse_mode='Markdown')