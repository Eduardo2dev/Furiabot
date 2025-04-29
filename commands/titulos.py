from telegram import Update
from telegram.ext import ContextTypes

# Comando /titulos
async def titulos_furia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    titulos = {
        "🟠 Counter-Strike: Global Offensive (CS:GO)": [
            "ESL Pro League Season 12: North America (2020)",
            "ESL Pro League Season 13: North America (2021)",
            "ECS Season 7 Finals (2019)",
            "DreamHack Masters Spring 2020: North America (2020)",
            "IEM New York 2020: North America (2020)",
            "Arctic Invitational 2019 (2019)",
            "StarLadder Major 2019 (2019)",
            "PGL Major Stockholm 2021 (3º lugar)",
            "PGL Major Antwerp 2022: American RMR (2022)",
            "IEM Rio Major 2022 (3º lugar)"
        ],
        "🟡 Rocket League": [
            "Gamers8 2022 (2022)",
            "RLCS 2022–23 North American Spring Invitational (2023)",
            "RLCS Season X South American Championship (2021)",
            "Esports World Cup 2024 (2024)"
        ],
        "🔴 Valorant": [
            "Tixinha Invitational (2024)"
        ],
        "🟢 League of Legends": [
            "Campeonato Brasileiro de League of Legends (CBLOL) (2015–2024)"
        ],
        "🔵 Rainbow Six Siege": [
            "Esports World Cup 2024 (2024)"
        ]
    }

    response = "**🏆 Títulos da FURIA:**\n\n"
    for modalidade, lista_de_titulos in titulos.items():
        if lista_de_titulos:
            response += f"**{modalidade}:**\n"
            for titulo in lista_de_titulos:
                response += f"- {titulo}\n"
            response += "\n"
        else:
            response += f"**{modalidade}:** Nenhum título registrado.\n\n"

    await update.message.reply_text(response, parse_mode="Markdown")