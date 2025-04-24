import telebot
from telebot import types

CHAVE_API = "7590710509:AAFJr53U0eGHHkiLWuf0yA1uWnkshZzj-yo"

bot = telebot.TeleBot(CHAVE_API)

def teclado_inicial():
    teclado = types.InlineKeyboardMarkup()
    
    botao_portugues = types.InlineKeyboardButton("🇧🇷 Versão em Portugês", callback_data="botao_portugues")
    botao_ingles = types.InlineKeyboardButton("🇺🇸 English Version", callback_data="botao_ingles")

    teclado.add(botao_portugues, botao_ingles)
    return teclado   

def teclado_portugues():
    teclado = types.InlineKeyboardMarkup()
    
    botao_sobre = types.InlineKeyboardButton("Sobre nós", callback_data="botao_sobre")
    botao_historia = types.InlineKeyboardButton("Nossa História", callback_data="botao_historia") 
    botao_times = types.InlineKeyboardButton("Nossos Times", callback_data="botao_times")
    botao_redes = types.InlineKeyboardButton("Nossas Redes", callback_data="botao_redes")
    botao_estilo = types.InlineKeyboardButton("Estilo da Furia", callback_data="botao_estilo")

    teclado.add(botao_sobre, botao_historia)
    teclado.add(botao_times, botao_redes)
    teclado.add(botao_estilo)

    teclado.add(types.InlineKeyboardButton("Voltar", callback_data="botao_voltar"))
    return teclado

def enviar_tela_inicial(chat_id):
    with open("FURIA_FULL.png", "rb") as foto:
        bot.send_photo(
            chat_id,
            foto,
            caption="Bem vindo",
            reply_markup=teclado_inicial()
        )

@bot.message_handler(commands=["start","help"])
def start(mensagem):
    with open("FURIA_FULL.png", "rb") as foto:
        bot.send_photo(
            mensagem.chat.id,
            foto,
            caption="Bem vindo",
            reply_markup=teclado_inicial()
        )
        
@bot.callback_query_handler(func=lambda call:True)
def acionamento_botao(call:types.CallbackQuery):
    
    teclado=teclado_portugues()

    sobre = """Furia 
Fundada em agosto de 2017, a FURIA Esports é uma organização brasileira de esportes eletrônicos que rapidamente se destacou no cenário competitivo global. Com sede em São Paulo, a FURIA é reconhecida por sua abordagem inovadora, paixão pelo jogo e dedicação ao desenvolvimento de talentos. A equipe compete em diversos títulos, incluindo Counter-Strike 2, League of Legends, Valorant, Rocket League e Rainbow Six Siege. Além das conquistas dentro dos jogos, a FURIA também se destaca por sua forte presença cultural e engajamento com a comunidade, tornando-se uma das marcas mais influentes dos esports no Brasil e no mundo.​
"""
    
    historia = """Nossa Historia"""
    
    times = """Nossos times"""
    
    redes = """Nossas Redes sociais"""
    
    estilo = """Vista-se no estilo da Furia"""
    
    match call.data:
        case "botao_portugues":
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=teclado_portugues())
        case "botao_sobre":
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=sobre)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_historia":
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=historia)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_times":
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=times)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_redes":
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=redes)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_estilo":
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=estilo)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_voltar":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            enviar_tela_inicial(call.message.chat.id)
            
bot.infinity_polling()







