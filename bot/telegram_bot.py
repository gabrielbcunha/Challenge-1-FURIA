import telebot
from telebot import types


from utils.keep_alive import keep_alive
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("CHAVE_API")

keep_alive()

bot = telebot.TeleBot(TOKEN)

def teclado_inicial():
    teclado = types.InlineKeyboardMarkup()
    
    botao_historia = types.InlineKeyboardButton("📜Nossa História", callback_data="botao_historia") 
    botao_time = types.InlineKeyboardButton("🏆Nosso Time", callback_data="botao_time")
    botao_whatsapp = types.InlineKeyboardButton("📱Bot Whatsapp", callback_data="botao_whatsapp")   
    botao_redes = types.InlineKeyboardButton("🎥Redes Sociais", callback_data="botao_redes")
    botao_loja = types.InlineKeyboardButton("🛒Lojinha da Pantera", callback_data="botao_loja")
    botao_contato = types.InlineKeyboardButton("✉️Contate-nos", callback_data="botao_contato")

    teclado.add(botao_time, botao_historia)
    teclado.add(botao_whatsapp, botao_redes)
    teclado.add(botao_loja)
    teclado.add(botao_contato)
   
    teclado.add(types.InlineKeyboardButton("⬅️Voltar", callback_data="botao_voltar"))
    return teclado

@bot.message_handler(commands=["start","help"])
def start(mensagem):
        
    with open("static/imagens/menu/furia_start_image.png", "rb") as foto:
        bot.send_photo(
            mensagem.chat.id,
            foto,
            caption=boas_vindas,
            reply_markup=teclado_inicial()
        )

def enviar_menu(chat_id):
        with open("static/imagens/menu/furia_start_image.png", "rb") as foto:
            bot.send_photo(
            chat_id,
            foto,
            caption=boas_vindas,
            reply_markup=teclado_inicial()
        )

def criar_botoes_time(lista_botoes):
    teclado = types.InlineKeyboardMarkup()
    for linha in lista_botoes:
        botoes = [types.InlineKeyboardButton(texto, callback_data=callback) for texto, callback in linha]
        teclado.add(*botoes)
    teclado.add(types.InlineKeyboardButton("Voltar", callback_data="botao_voltar"))                      
    return teclado

def menu_time():
    lista_botoes = [
        [("🇧🇷FalleN","botao_fallen")],
        [("🇰🇿molodoy", "botao_molodoy"), ("🇧🇷Yuurih", "botao_yuurih")],
        [("🇱🇻YEKINDAR", "botao_yekindar"), ("🇧🇷KSCERATO", "botao_kscerato")],
    ]
    return criar_botoes_time(lista_botoes)

def criar_botoes_loja(lista_botoes):
    teclado = types.InlineKeyboardMarkup()
    for linha in lista_botoes:
        botoes = [types.InlineKeyboardButton(texto, callback_data=callback) for texto, callback in linha]
        teclado.add(*botoes)
    teclado.add(types.InlineKeyboardButton("Voltar", callback_data="botao_voltar"))
    return teclado
    
def menu_loja():        
    lista_botoes = [
        [("Adidas X Furia", "botao_adidas")], 
        [("Batman", "botao_batman"), ("Champion", "botao_champion")],
        [("Future is Black", "botao_future"), ("My Hero Academia", "botao_hero")],
        [("Zor", "botao_zor"), ("Classic", "botao_classic")],
        [("Furia X New Era", "botao_new_era"), ("Magic Panthera", "botao_panthera")],
        [("Hard to Love X Harder to Kill", "botao_love")],
        ]
    return criar_botoes_loja(lista_botoes)  
    
acoes = {
    "botao_historia": ("historia", teclado_inicial),
    "botao_time": ("time", menu_time),
    "botao_whatsapp": ("whatsapp", teclado_inicial),
    "botao_redes": ("redes", teclado_inicial),
    "botao_loja": ("loja", menu_loja),
    "botao_contato": ("contato", teclado_inicial),
    "botao_voltar": ("boas_vindas", teclado_inicial),
    
    "botao_fallen": ("fallen",menu_time),
    "botao_molodoy": ("molodoy", menu_time),
    "botao_yuurih": ("yuurih", menu_time),
    "botao_yekindar": ("yekindar", menu_time),
    "botao_kscerato": ("kscerato", menu_time),
    
    "botao_adidas": ("adidas", menu_loja),
    "botao_batman": ("batman", menu_loja),
    "botao_champion": ("champion", menu_loja),
    "botao_future": ("future", menu_loja),
    "botao_hero": ("hero", menu_loja),
    "botao_zor": ("zor", menu_loja),
    "botao_love": ("love", menu_loja),
    "botao_classic": ("classic", menu_loja),
    "botao_new_era": ("new_era", menu_loja),
    "botao_panthera": ("panthera", menu_loja),
}

@bot.callback_query_handler(func=lambda call: True)        
def acionamento_botao(call:types.CallbackQuery):    
    conteudo, teclado_func = acoes.get(call.data, (None, None))
    if conteudo:
        with open(imagens[call.data], "rb") as foto:
            media = types.InputMediaPhoto(foto, caption=globals()[conteudo])
            bot.edit_message_media(
                media,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=teclado_func()
            )
    elif call.data == "botao_voltar":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        enviar_menu(call.message.chat.id)  
                 
bot.infinity_polling()