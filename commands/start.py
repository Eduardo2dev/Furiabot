from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🔥 *BEM-VINDO AO FURIA FAN BOT!* 🔥\n'
        '👊 Aqui, quem não é furioso, não é FURIA!\n'
        '💥 Fique ligado para atualizações, estatísticas e tudo o que envolve a organização mais insana do cenário!\n'
        '⚡ Entre na pele da nossa pantera e sinta a energia que vai te deixar FURIOSO!\n'
        '💬 Quer se tornar um verdadeiro furioso? Digite /comandos e descubra os atalhos para estar sempre ligado na nossa pantera!\n',
        parse_mode='Markdown'
    )
