import telebot
from telebot import types

CHAVE_API = "7590710509:AAFJr53U0eGHHkiLWuf0yA1uWnkshZzj-yo"

bot = telebot.TeleBot(CHAVE_API)

def teclado_inicial():
    teclado = types.InlineKeyboardMarkup()
    
    botao_sobre = types.InlineKeyboardButton("Sobre nós", callback_data="botao_sobre")
    botao_historia = types.InlineKeyboardButton("Nossa História", callback_data="botao_historia") 
    botao_time = types.InlineKeyboardButton("🏆 Nosso Time", callback_data="botao_time")
    botao_redes = types.InlineKeyboardButton("🎥 Nossas Redes Sociais", callback_data="botao_redes")
    botao_loja = types.InlineKeyboardButton("🛒 Lojinha da Pantera", callback_data="botao_loja")

    teclado.add(botao_sobre, botao_historia)
    teclado.add(botao_time, botao_redes)
    teclado.add(botao_loja)

    teclado.add(types.InlineKeyboardButton("Voltar", callback_data="botao_voltar"))
    return teclado

boas_vindas="""🐾 Fala, guerreiro(a)!
Seja bem Vindo ao Bot oficial da FURIA no Telegram!

Você quer acessar facilmente tudo relacionado ao seu time do coração❤? 

Agora tudo a um clique de distancia🔥

Aqui em baixo você consegue ver o menu interativo do bot, basta clicar para navegar entre as funcionalidades. 

Vem ganhar junto com a FURIA! 👊
    """

@bot.message_handler(commands=["start","help"])
def start(mensagem):
        
    with open("imagens/start_image.png", "rb") as foto:
        bot.send_photo(
            mensagem.chat.id,
            foto,
            caption=boas_vindas,
            reply_markup=teclado_inicial()
        )

def enviar_menu(chat_id):
        with open("imagens/start_image.png", "rb") as foto:
            bot.send_photo(
            chat_id,
            foto,
            caption=boas_vindas,
            reply_markup=teclado_inicial()
        )
            
def menu_time():
    
    teclado = types.InlineKeyboardMarkup()
    
    botao_fallen = types.InlineKeyboardButton("FalleN", callback_data="botao_fallen")
    botao_molodoy = types.InlineKeyboardButton("molodoy", callback_data="botao_molodoy")
    botao_yuurih = types.InlineKeyboardButton("Yuurih", callback_data="botao_yuurih")
    botao_yekindar = types.InlineKeyboardButton("YEKINDAR", callback_data="botao_yekindar")
    botao_kscerato = types.InlineKeyboardButton("KSCERATO", callback_data="botao_kscerato")
 
    
    teclado.add(botao_fallen)
    teclado.add(botao_kscerato, botao_yuurih)
    teclado.add(botao_yekindar, botao_molodoy)
    teclado.add(types.InlineKeyboardButton("Voltar", callback_data="botao_voltar"))
    return teclado
        
def menu_loja():        
    
    teclado = types.InlineKeyboardMarkup()
    
    botao_adidas = types.InlineKeyboardButton("Adidas + Furia", callback_data="botao_adidas")        
    botao_batman = types.InlineKeyboardButton("Batman", callback_data="botao_batman")        
    botao_champion = types.InlineKeyboardButton("Champion", callback_data="botao_champion")        
    botao_future = types.InlineKeyboardButton("Future is Black", callback_data="botao_future")        
    botao_hero = types.InlineKeyboardButton("My Hero Academia", callback_data="botao_hero")        
    botao_zor = types.InlineKeyboardButton("Zor", callback_data="botao_zor")  
       
    
    teclado.add(botao_adidas, botao_batman)
    teclado.add(botao_champion, botao_future)
    teclado.add(botao_hero, botao_zor)
    teclado.add(types.InlineKeyboardButton("Voltar", callback_data="botao_voltar"))        
    return teclado
    
@bot.callback_query_handler(func=lambda call:True)
def acionamento_botao(call:types.CallbackQuery):

    match call.data:
        #Menu principal 
        case "botao_sobre":
            sobre = """📜Acompanhe a nossa trajetoria até aqui📜 
            
            """
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=sobre)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_inicial())
        case "botao_historia":
            historia="""📜Fala 
            
            
            
            """
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=historia)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_inicial())
        case "botao_time":
            time="""Nossa Historia
            
            """
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=time)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())
        case "botao_redes":
            redes="""Não perca nenhuma atualização sobre a Furia🔥

Nos siga em nossas redes socias, basta clicar nos links abaixo
    
Instagram: http://instagram.com/furiagg
Twiter: https://x.com/FURIA
Youtube: https://www.youtube.com/@FURIAgg 
Facebook: www.facebook.com/furiagg 

            """
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=redes)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_inicial())
        case "botao_loja":
            loja="""loja
            
            
            """
            media = types.InputMediaPhoto(open("imagens/start_image.png", "rb"), caption=loja)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
        case "botao_voltar":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            enviar_menu(call.message.chat.id)

        #Menu do Time
        case "botao_fallen":
            fallen="""🇧🇷 FalleN "O Professor"

Gabriel "FalleN" Toledo (nascido em 30 de maio de 1991) é considerado um dos maiores jogadores de Counter-Strike da história do Brasil e do mundo, tendo sido eleito o segundo melhor jogador do mundo em 2016 e o quinto em 2017. Além dos seus dois títulos de major, FalleN também conquistou vários outros prêmios e reconhecimentos ao longo da sua carreira, incluindo uma vaga no hall da fama do CS:GO. Desde 03 de julho de 2023 atua como capitan-in-game no time de CS2 da FURIA

Siga FaleN em suas redes sociais:
Instagram: https://www.instagram.com/fallen/
X (Antigo Twiter): https://x.com/FalleNCS
            """
            media = types.InputMediaPhoto(open("imagens/time/fallen_image.jpg", "rb"), caption=fallen)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())  
        
        case "botao_molodoy":
            molodoy="""🇰🇿 molodoy 

Danil "molodoy" Golubenko (nascido em 10 de janeiro de 2005) é o promissor jovem que se destacou como AWPer nos campeonatos do Cazaquistão, tendo ingressado na organização FURIA Esports em 11 de abril de 2025, sua partida de estreia será justamente no Cazaquistão, onde a Furia disputará a PGL Astana 2025 entre os dias 10 e 18 de maio.
    
Siga molodoy em suas redes sociais: 
X (Antigo Twiter): https://x.com/tvoy_molodoy  
"""
            media = types.InputMediaPhoto(open("imagens/time/molodoy_image.jpeg", "rb"), caption=molodoy)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())
        
        case "botao_yuurih":
            yuurih="""🇧🇷 YUURIH 

Yuri "YUURIH" Boian (nascido em 22 de dezembro de 1999) é conhecido por suas atuações em grande nível e por sua história de dedicação ao esporte. YUURIH faz parte da organização FURIA Esports desde 08 de novembro de 2017 e já alcançou a marca de 1000 mapas disputados com a FURIA, sendo atualmente o jogador ativo mais antigo na equipe. 

Siga YUURIH em suas redes sociais:
Instagram: https://www.instagram.com/yuurihfps/  
X (Antigo Twiter): https://x.com/yuurih 
"""
            media = types.InputMediaPhoto(open("imagens/time/yuurih_image.jpeg", "rb"), caption=yuurih)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())  
        
        case "botao_yekindar":
            yekindar="""🇱🇻 YEKINDAR 

Mareks "YEKINDAR" Gaļinskis (nascido em 04 de outubro de 1999) é amplamente reconhecido por seu estilo de jogo agressivo como entry fragger. YEKINDAR é conhecido por sua capacidade de abrir espaços para sua equipe, sua mira precisa e sua habilidade em situações de clutch. Em 22 de abril de 2025 ingressou na organização Furia Esports como Stand-in. 

Siga YEKINDAR em suas redes sociais:
Instagram: https://www.instagram.com/yek1ndar/  
X (Antigo Twiter): https://x.com/yek1ndar  
"""
            media = types.InputMediaPhoto(open("imagens/time/yekindar_image.jpeg", "rb"), caption=yekindar)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time()) 
        
        case "botao_kscerato":
            kscerato="""🇧🇷 KSCERATO 

Kaike "KSCERATO" Cerato (nascido em 12 de dezembro de 1999) é conhecido por ser um jogador consistente e crucial para a equipe. Sua forte sinergia com companheiros de equipe como YUURIH tem sido um fator chave no sucesso da FURIA ao longo dos anos. KSCERATO faz parte da organização Furia Esports desde 06 de fevereiro de 2018, sendo o segundo jogador ativo mais antigo da Furia, atrás somente de YUURIH.

Siga KSCERATO em suas redes sociais:
Instagram: https://www.instagram.com/kscerato  
X (Antigo Twiter): https://x.com/kscerato  
"""
            media = types.InputMediaPhoto(open("imagens/time/kscerato_image.jpg", "rb"), caption="")
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
        
        case "botao_adidas":
            adidas = """ 
            
            """
            media = types.InputMediaPhoto(open("imagens/loja/furia_adidas_image.jpg", "rb"), caption=adidas)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
                  
        case "botao_batman":
            batman="""
            
            """
            media = types.InputMediaPhoto(open("imagens/loja/furia_batman_image.jpg", "rb"), caption=batman)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
            
        case "botao_champion":
            champion="""
            
            """
            media = types.InputMediaPhoto(open("imagens/loja/furia_champion_image.jpg", "rb"), caption=champion)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
            
        case "botao_future":                                        
            future="""
            
            """
            media = types.InputMediaPhoto(open("imagens/loja/furia_future_is_black_image.jpg", "rb"), caption=future)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
                            
        case "botao_hero":  
            hero="""
            
            """
            media = types.InputMediaPhoto(open("imagens/loja/furia_my_hero_academia_image.jpg", "rb"), caption=hero)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
            
        case "botao_zor":
            zor="""
A collab FURIA x ZOR une o estilo western ao lifestyle de Brino, influenciador conhecido por sua autenticidade. Inspirada no clipe "Todo Mundo Tá Tão Bem", a coleção traz peças que celebram a liberdade e as raízes do oeste americano, com toque urbano e moderno.

Com cores como cinza chumbo, preto, verde, bege e marrom, a linha mistura o casual com o funcional. Cada peça foi criada para contar uma história e refletir o estilo único de Brino, com modelagens marcantes e estampas exclusivas.

A coleção já está disponível em edição limitada no nosso site. Garanta a sua e mostre seu estilo com atitude!

Clique neste link para acessar a coleção: www.furia.gg/produtos/collabs/zor

            """                      
            media = types.InputMediaPhoto(open("imagens/loja/furia_zor_image.jpg", "rb"), caption=zor)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())            

bot.infinity_polling()