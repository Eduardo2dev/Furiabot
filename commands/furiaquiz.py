from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler, ApplicationBuilder

# Dicionário para armazenar o estado do quiz dos usuários
quiz_state = {}

# Definir as perguntas do quiz como uma lista de tuplas.
quiz_perguntas = [
    ("Qual animal é o mascote e representa a identidade visual da FURIA?", ["Tigre", "Leão", "Pantera", "Onça"], 2),
    ("Em que ano a FURIA foi fundada?", ["2016", "2017", "2018", "2019"], 1),
    ("Em que cidade a FURIA foi fundada?", ["Uberlandia", "São Paulo", "Rio de Janeiro", "Brasilia"], 0),
    ("Qual o jogo principal onde a FURIA se destacou inicialmente?", ["CS:GO", "LoL", "Valorant", "PUBG"], 0),
    ("Além de jogador profissional de CS:GO, qual outra atividade online 'FalleN' é bastante conhecido e engajado com a comunidade?", ["Desenvolvimento de jogos", "Streamer", "Músico", "Pintor"], 1),
    ("Qual dos seguintes jogadores atualmente desempenha a função de capitão em jogo (IGL) na equipe de Counter-Strike 2 (CS2) da FURIA?", ["Fallen", "Molodoy", "Yekindar", "yuurih"], 0),
    ("Quem é o presidente do time da FURIA na Kings League Brasil?", ["Guerri", "Neymar", "Fallen", "Cris Guedes"], 3),
    ("Em qual grande Major a FURIA alcançou a semifinal pela primeira vez?", ["PGL Major Stockholm 2021", "IEM Rio Major 2022", "ESL One Cologne 2020", "BLAST Paris Major 2023"], 1),
    ("Em qual campeonato a FURIA representou o Brasil no VALORANT Champions pela primeira vez?", ["VCT Champions 2021", "VCT LOCK//IN 2023", "Masters Berlin 2021", "VCT Champions 2022"], 3),
     ("Com qual marca esportiva a FURIA firmou parceria em 2025 para produzir seus uniformes?", ["Nike", "Adidas", "Puma", "New Balance"], 1),
]

async def quizfuria(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    quiz_state[user_id] = {"pergunta_atual": 0, "pontuacao": 0}
    print(f"QUIZ INICIADO - User ID: {user_id}")
    await enviar_pergunta(update, context)

async def enviar_pergunta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    print(f"ENVIAR PERGUNTA - User ID: {user_id}, Pergunta Index: {quiz_state.get(user_id, {}).get('pergunta_atual')}")
    if user_id not in quiz_state:
        print("ENVIAR PERGUNTA - Quiz não iniciado para este usuário.")
        return

    estado = quiz_state[user_id]
    pergunta_index = estado["pergunta_atual"]

    if pergunta_index < len(quiz_perguntas):
        pergunta, opcoes, _ = quiz_perguntas[pergunta_index]
        keyboard = [[InlineKeyboardButton(opcao, callback_data=f"resposta_{pergunta_index}_{i}")] for i, opcao in enumerate(opcoes)]
        reply_markup = InlineKeyboardMarkup(keyboard)

        chat_id = update.effective_chat.id
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"Pergunta {pergunta_index + 1}: {pergunta}",
            reply_markup=reply_markup
        )
    else:
        await finalizar_quiz(update, context)

async def responder_pergunta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    print(f"RESPONDER PERGUNTA - User ID: {query.from_user.id}, Callback Data: {query.data}")
    await query.answer()
    user_id = query.from_user.id

    if user_id not in quiz_state:
        print("RESPONDER PERGUNTA - Quiz não encontrado para este usuário.")
        return

    estado = quiz_state[user_id]
    pergunta_index = estado["pergunta_atual"]
    print(f"RESPONDER PERGUNTA - Pergunta Index Atual: {pergunta_index}")
    _, _, resposta_correta_index = quiz_perguntas[pergunta_index]
    resposta_usuario_index = int(query.data.split("_")[-1])

    if resposta_usuario_index == resposta_correta_index:
        estado["pontuacao"] += 1
        await context.bot.send_message(chat_id=query.message.chat_id, text=f"✅ Correto! Sua pontuação: {estado['pontuacao']}")
    else:
        await context.bot.send_message(chat_id=query.message.chat_id, text=f"❌ Incorreto! A resposta certa era: {quiz_perguntas[pergunta_index][1][resposta_correta_index]}. Sua pontuação: {estado['pontuacao']}")

    estado["pergunta_atual"] += 1
    print(f"RESPONDER PERGUNTA - Novo Pergunta Index: {estado['pergunta_atual']}")
    await enviar_pergunta(update, context)

async def finalizar_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in quiz_state:
        pontuacao = quiz_state[user_id]["pontuacao"]
        total_perguntas = len(quiz_perguntas)
        del quiz_state[user_id]
        print(f"QUIZ FINALIZADO - User ID: {user_id}, Pontuação Final: {pontuacao}/{total_perguntas}")
        mensagem_final = f"🏁 Quiz finalizado! Sua pontuação final: {pontuacao}/{total_perguntas}"
        if pontuacao == total_perguntas:
            mensagem_final += "\n\n🏆 Você é um verdadeiro FURIOSO! Parabéns por acertar todas as perguntas!"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mensagem_final)
