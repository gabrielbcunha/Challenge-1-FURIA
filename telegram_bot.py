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

    with open("imagens/start_image.png", "rb") as foto:
        bot.send_photo(
            chat_id,
            foto,
            caption=boas_vindas,
            reply_markup=teclado_inicial()
        )

def menu_time_portugues():
    
    teclado = types.InlineKeyboardMarkup()
    
    botao_fallen = types.InlineKeyboardButton("FalleN Capitão", callback_data="botao_fallen")
    botao_molodoy = types.InlineKeyboardButton("molodoy", callback_data="botao_molodoy")
    botao_yuurih = types.InlineKeyboardButton("Yuurih", callback_data="botao_yuurih")
    botao_yekindar = types.InlineKeyboardButton("YEKINDAR", callback_data="botao_yekindar")
    botao_kscerato = types.InlineKeyboardButton("KSCERATO", callback_data="botao_kscerato")
 
    
    teclado.add(botao_fallen)
    teclado.add(botao_kscerato, botao_yuurih)
    teclado.add(botao_yekindar, botao_molodoy)
    teclado.add(types.InlineKeyboardButton("Voltar", callback_data="botao_voltar"))
    return teclado


@bot.message_handler(commands=["start","help"])
def start(mensagem):
    
    boas_vindas="""Fala Furioso
        Seja bem Vindo ao Bot oficial da FURIA no Telegram
    
    """
    
    with open("imagens/start_image.png", "rb") as foto:
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
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption="Olá")
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())

        #Menu principal em Português
        case "botao_sobre":
            sobre = """📜Acompanhe a nossa trajetoria até aqui📜 
            """
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=sobre)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_historia":
            historia="""Nossa Historia
            """
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=historia)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_time":
            time="""Nossa Historia
            """
            
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=time)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time_portugues())
        case "botao_redes":
            redes="""Nossa Historia
            """
            
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=redes)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_estilo":
            estilo="""Nossa Historia
            """
            
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=estilo)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_portugues())
        case "botao_voltar":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            enviar_tela_inicial(call.message.chat.id)

        #Menu do Time - Portugues
        case "botao_fallen":
            fallen="""🇧🇷 FalleN "O Professor"

Gabriel "FalleN" Toledo (nascido em 30 de maio de 1991) é considerado um dos maiores jogadores de Counter-Strike da história do Brasil e do mundo, tendo sido eleito o segundo melhor jogador do mundo em 2016 e o quinto em 2017. Além dos seus dois títulos de major, FalleN também conquistou vários outros prêmios e reconhecimentos ao longo da sua carreira, incluindo uma vaga no hall da fama do CS:GO. Desde 03 de julho de 2023 atua como capitan-in-game no time de CS2 da FURIA

Siga FaleN em suas redes sociais:
Instagram: https://www.instagram.com/fallen/
X (Antigo Twiter): https://x.com/FalleNCS
            """
            media = types.InputMediaPhoto(open("imagens/time/fallen_image.jpg", "rb"), caption=fallen)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time_portugues())  
        
        case "botao_molodoy":
            molodoy="""🇰🇿 molodoy 

Danil "molodoy" Golubenko (nascido em 10 de janeiro de 2005) 

Siga molodoy em suas redes sociais:
Instagram:  
X (Antigo Twiter):  
"""
            media = types.InputMediaPhoto(open("imagens/time/molodoy_image.jpeg", "rb"), caption=molodoy)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time_portugues())
        
        case "botao_yuurih":
            yuurih="""🇧🇷 YUURIH 

Yuri "YUURIH" Boian (nascido em 22 de dezembro de 1999) 

Siga YUURIH em suas redes sociais:
Instagram:  
X (Antigo Twiter): 
"""
            media = types.InputMediaPhoto(open("imagens/time/yuurih_image.jpeg", "rb"), caption=yuurih)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time_portugues())  
        
        case "botao_yekindar":
            yekindar="""🇱🇻 YEKINDAR 

Mareks "YEKINDAR" Gaļinskis (nascido em 04 de outubro de 1999) 

Siga YEKINDAR em suas redes sociais:
Instagram:  
X (Antigo Twiter):  
"""
            media = types.InputMediaPhoto(open("imagens/time/yekindar_image.jpeg", "rb"), caption=yekindar)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time_portugues()) 
        
        case "botao_kscerato":
            kscerato="""🇧🇷 KSCERATO 

Kaike "KSCERATO" Cerato (nascido em 12 de dezembro de 1999) 

Siga KSCERATO em suas redes sociais:
Instagram:  
X (Antigo Twiter):  
"""
            media = types.InputMediaPhoto(open("imagens/time/kscerato_image.jpg", "rb"), caption=kscerato)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time_portugues())
                    
bot.infinity_polling()







