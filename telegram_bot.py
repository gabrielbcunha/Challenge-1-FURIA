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
    botao_time = types.InlineKeyboardButton("Nosso Time", callback_data="botao_time")
    botao_redes = types.InlineKeyboardButton("Nossas Redes", callback_data="botao_redes")
    botao_estilo = types.InlineKeyboardButton("Estilo da Furia", callback_data="botao_estilo")

    teclado.add(botao_sobre, botao_historia)
    teclado.add(botao_time, botao_redes)
    teclado.add(botao_estilo)

    teclado.add(types.InlineKeyboardButton("Voltar", callback_data="botao_voltar"))
    return teclado

def enviar_tela_inicial(chat_id):

    boas_vindas=""

    with open("FURIA_FULL.png", "rb") as foto:
        bot.send_photo(
            chat_id,
            foto,
            caption=boas_vindas,
            reply_markup=teclado_inicial()
        )

def menu_time():
    
    teclado = types.InlineKeyboardMarkup()
    
    botao_fallen = types.InlineKeyboardButton("FalleN Capitão", callback_data="botao_fallen")
    botao_molodoy = types.InlineKeyboardButton("molodoy", callback_data="botao_molodoy")
    botao_yuurih = types.InlineKeyboardButton("Yuurih", callback_data="botao_yuurih")
    botao_yekindar = types.InlineKeyboardButton("YEKINDAR", callback_data="yekindar")
    botao_kscerato = types.InlineKeyboardButton("KSCERATO", callback_data="botao_kscerato")
    botao_hepa = types.InlineKeyboardButton("Hepa", callback_data="botao_hepa")
    botao_sidde = types.InlineKeyboardButton("Sidde", callback_data="botao_sidde")
    
    teclado.add(botao_fallen)
    teclado.add(botao_kscerato, botao_yuurih)
    teclado.add(botao_yekindar, botao_molodoy)
    teclado.add(botao_hepa, botao_sidde)
    teclado.add(types.InlineKeyboardButton("Voltar", callback_data="botao_voltar"))
    return teclado


@bot.message_handler(commands=["start","help"])
def start(mensagem):
    
    boas_vindas="""Fala Furioso
        Seja bem Vindo ao Bot oficial da FURIA no Telegram
    
    """
    
    with open("FURIA_FULL.png", "rb") as foto:
        bot.send_photo(
            mensagem.chat.id,
            foto,
            caption=boas_vindas,
            reply_markup=teclado_inicial()
        )
        
@bot.callback_query_handler(func=lambda call:True)
def acionamento_botao(call:types.CallbackQuery):

    match call.data:
        case "botao_portugues":
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=sobre)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())

        #Menu principal em Português
        case "botao_sobre":
            sobre = """📜Acompanhe a nossa trajetoria até aqui📜 
            """
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=sobre)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_historia":
            historia="""Nossa Historia
            """
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=historia)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_time":
            time="""Nossa Historia
            """
            
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=time)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())
        case "botao_redes":
            redes="""Nossa Historia
            """
            
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=redes)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_estilo":
            estilo="""Nossa Historia
            """
            
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=estilo)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_voltar":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            enviar_tela_inicial(call.message.chat.id)

        #Menu do Time
        case "botao_fallen":
            fallen="""Nossa Historia
            """
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=fallen)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())  
        case "botao_molodoy":
            moloy="""Nossa Historia
            """
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=moloy)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())
        case "botao_yuurih":
            yuurih="""Nossa Historia
            """
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=yuurih)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())  
        case "botao_yekindar":
            yekindar="""Nossa Historia
            """
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=yekindar)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time()) 
        case "botao_kscerato":
            kscerato="""Nossa Historia
            """  
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=kscerato)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())
        case "botao_hepa":
            hepa="""Nossa Historia
            """
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=hepa)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())     
        case "botao_sidde":
            sidde="""Nossa Historia
            """  
            media = types.InputMediaPhoto(open("FURIA_FULL.png", "rb"), caption=sidde)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())
                        
bot.infinity_polling()







