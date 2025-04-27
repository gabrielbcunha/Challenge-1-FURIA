import telebot
from telebot import types

CHAVE_API = "7590710509:AAFJr53U0eGHHkiLWuf0yA1uWnkshZzj-yo"

bot = telebot.TeleBot(CHAVE_API)

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

boas_vindas="""🐾 Fala, guerreiro(a)!
Seja bem Vindo ao Bot oficial da FURIA no Telegram!

Você quer acessar facilmente tudo relacionado ao seu time do coração❤? 

Agora tudo a um clique de distancia🔥

Aqui em baixo você consegue ver o menu interativo do bot, basta clicar para navegar entre as funcionalidades. 

Vem ganhar junto com a FURIA! 👊
    """

@bot.message_handler(commands=["start","help"])
def start(mensagem):
        
    with open("imagens/menu/furia_start_image.png", "rb") as foto:
        bot.send_photo(
            mensagem.chat.id,
            foto,
            caption=boas_vindas,
            reply_markup=teclado_inicial()
        )

def enviar_menu(chat_id):
        with open("imagens/menu/furia_start_image.png", "rb") as foto:
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
    teclado.add(types.InlineKeyboardButton("⬅️Voltar", callback_data="botao_voltar"))
    return teclado
        
def menu_loja():        
    
    teclado = types.InlineKeyboardMarkup()
    
    botao_adidas = types.InlineKeyboardButton("Adidas X Furia", callback_data="botao_adidas")        
    botao_batman = types.InlineKeyboardButton("Batman", callback_data="botao_batman")        
    botao_champion = types.InlineKeyboardButton("Champion", callback_data="botao_champion")        
    botao_future = types.InlineKeyboardButton("Future is Black", callback_data="botao_future")        
    botao_hero = types.InlineKeyboardButton("My Hero Academia", callback_data="botao_hero")        
    botao_zor = types.InlineKeyboardButton("Zor", callback_data="botao_zor")  
    botao_love = types.InlineKeyboardButton("Hard to Love X Harder to Kill", callback_data="botao_love")  
    botao_classic = types.InlineKeyboardButton("Classic", callback_data="botao_classic")  
    botao_new_era = types.InlineKeyboardButton("Furia X New Era", callback_data="botao_new_era")  
    botao_phantera = types.InlineKeyboardButton("Magic Panthera", callback_data="botao_phantera")  
       
    
    teclado.add(botao_adidas)
    teclado.add(botao_batman, botao_champion)
    teclado.add(botao_future, botao_hero)
    teclado.add(botao_zor, botao_classic)
    teclado.add(botao_new_era, botao_phantera)
    teclado.add(botao_love)

    teclado.add(types.InlineKeyboardButton("⬅️Voltar", callback_data="botao_voltar"))        
    return teclado
    
@bot.callback_query_handler(func=lambda call:True)
def acionamento_botao(call:types.CallbackQuery):

#Conteudo - Menu Inicial 

    time="""Quer conhecer ainda mais os nossos jogadores? 🔥

Agora ficou fácil!
Aqui embaixo você encontra o menu com o nome de cada atleta.
É só clicar no nome pra ver tudo sobre eles: perfil, conquistas e muito mais! 👊

Escolha seu favorito e bora mergulhar no mundo da FURIA! 🐆
    """
    historia="""
A FURIA Esports nasceu em 2017 e rapidamente se firmou como uma das grandes potências do CS:GO mundial. Conhecida por seu estilo agressivo e pela paixão inabalável, a organização ganhou respeito e admiração dentro e fora dos servidores. Com nomes como yuurih e KSCERATO, construiu campanhas históricas em grandes torneios, sempre carregando a identidade ousada que define a FURIA. Na transição para o CS2, o time manteve sua essência competitiva, adaptando-se ao novo jogo sem perder o espírito de luta. 

A trajetória da FURIA é mais do que resultados: é sobre inspirar uma geração e mostrar ao mundo a força do Brasil.        
    """    
    whatsapp="""Tá pronto pra ficar ainda mais perto da FURIA? 😎🔥

Agora você pode acessar tudo sobre seu time do coração direto no WhatsApp! É só clicar no link abaixo e trocar uma ideia com nosso chatbot oficial:
👉 https://api.whatsapp.com/send/?phone=5511993404466&text&type=phone_number&app_absent=0

Olha o que te espera lá:
⚡ Jogos ao vivo
🎯 Campeonato de Clipadores
📅 Calendário de Jogos
🛒 Lojinha da Pantera
📰 Esports News / Trend Topics
🎥 Criadores de Conteúdo e Streamers
🤑 FURIA Cash
💬 Modo Bate-Papo

Tá esperando o quê? Bora ganhar junto com a FURIA! 👊🐆    
    """ 
    redes="""Quer ficar por dentro de tudo que rola na FURIA?🔥

Então cola com a gente nas redes sociais!
É só clicar nos links aqui embaixo e seguir a tropa da Pantera:

Instagram: http://instagram.com/furiagg
Twiter: https://x.com/FURIA
Youtube: https://www.youtube.com/@FURIAgg 
Facebook: www.facebook.com/furiagg 

Vem viver a FURIA com a gente! 👊🐆
    """
    loja="""Quer vestir a camisa da FURIA e mostrar toda sua paixão? 🔥

Aqui embaixo você encontra o menu com as nossas coleções de roupas!
É só clicar e conferir cada coleção de perto. 😎👕

Ah, e se quiser dar uma geral na nossa loja principal, é só clicar aqui:
🛒 https://www.furia.gg/

Bora representar a Pantera com estilo! 👊🐆
    """
    contato="""Aqui a sua voz também faz parte da FURIA! 🔥

Quer mandar sugestões, críticas ou elogios?
É só clicar no link abaixo e deixar sua opinião:

📝 https://www.furia.gg/Formulario    

Sua participação é muito importante pra gente seguir evoluindo!
Vem construir a FURIA junto com a gente! 👊🐆
    """
    
#Conteudo - Time    
    fallen="""🇧🇷 FalleN "O Professor"

Gabriel "FalleN" Toledo (nascido em 30 de maio de 1991) é considerado um dos maiores jogadores de Counter-Strike da história do Brasil e do mundo, tendo sido eleito o segundo melhor jogador do mundo em 2016 e o quinto em 2017. Além dos seus dois títulos de major, FalleN também conquistou vários outros prêmios e reconhecimentos ao longo da sua carreira, incluindo uma vaga no hall da fama do CS:GO. Desde 03 de julho de 2023 atua como capitan-in-game no time de CS2 da FURIA

Siga FaleN em suas redes sociais:
Instagram: https://www.instagram.com/fallen/
X (Antigo Twiter): https://x.com/FalleNCS
    """
    molodoy="""🇰🇿 molodoy 

Danil "molodoy" Golubenko (nascido em 10 de janeiro de 2005) é o promissor jovem que se destacou como AWPer nos campeonatos do Cazaquistão, tendo ingressado na organização FURIA Esports em 11 de abril de 2025, sua partida de estreia será justamente no Cazaquistão, onde a Furia disputará a PGL Astana 2025 entre os dias 10 e 18 de maio.
    
Siga molodoy em suas redes sociais: 
X (Antigo Twiter): https://x.com/tvoy_molodoy  
    """
    yuurih="""🇧🇷 YUURIH 

Yuri "YUURIH" Boian (nascido em 22 de dezembro de 1999) é conhecido por suas atuações em grande nível e por sua história de dedicação ao esporte. YUURIH faz parte da organização FURIA Esports desde 08 de novembro de 2017 e já alcançou a marca de 1000 mapas disputados com a FURIA, sendo atualmente o jogador ativo mais antigo na equipe. 

Siga YUURIH em suas redes sociais:
Instagram: https://www.instagram.com/yuurihfps/  
X (Antigo Twiter): https://x.com/yuurih 
    """
    yekindar="""🇱🇻 YEKINDAR 

Mareks "YEKINDAR" Gaļinskis (nascido em 04 de outubro de 1999) é amplamente reconhecido por seu estilo de jogo agressivo como entry fragger. YEKINDAR é conhecido por sua capacidade de abrir espaços para sua equipe, sua mira precisa e sua habilidade em situações de clutch. Em 22 de abril de 2025 ingressou na organização Furia Esports como Stand-in. 

Siga YEKINDAR em suas redes sociais:
Instagram: https://www.instagram.com/yek1ndar/  
X (Antigo Twiter): https://x.com/yek1ndar  
    """
    kscerato="""🇧🇷 KSCERATO 

Kaike "KSCERATO" Cerato (nascido em 12 de dezembro de 1999) é conhecido por ser um jogador consistente e crucial para a equipe. Sua forte sinergia com companheiros de equipe como YUURIH tem sido um fator chave no sucesso da FURIA ao longo dos anos. KSCERATO faz parte da organização Furia Esports desde 06 de fevereiro de 2018, sendo o segundo jogador ativo mais antigo da Furia, atrás somente de YUURIH.

Siga KSCERATO em suas redes sociais:
Instagram: https://www.instagram.com/kscerato  
X (Antigo Twiter): https://x.com/kscerato  
    """
    
#Conteúdo - Loja    
    adidas="""Furia X Adidas
    
Parceria exclusiva com a renomada marca de artigos esportivos Adidas, patrocinadora oficial da FURIA e responsável pela confecção dos nossos uniformes.    

Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/collabs/adidas

"""
    batman="""Furia X Batman 🦇
    
Fruto de uma colaboração com a DC Comics, a coleção FURIA x Batman celebra os 85 anos do Cavaleiro das Trevas. Lançada inicialmente em 2022, a linha inclui camisetas, moletons, jaquetas e acessórios com elementos que unem a estética sombria do Batman à identidade da FURIA. A coleção foi reconhecida com o prêmio de Inovação pela Warner Bros. em 2023.    

Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/collabs/batman
    """
    champion="""Furia X Champion 🏆
    
Colaboração com a tradicional marca esportiva americana Champion. Traz jaquetas estilo college, moletons e camisetas que misturam o estilo clássico norte-americano com a identidade esportiva e urbana da FURIA. As peças carregam bordados e tecidos premium, focadas em quem busca um visual autêntico, vintage e esportivo.

Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/collabs/champion
    """   
    future="""Future is Black 🖤
    
Coleção lançada como um manifesto contra o racismo, em parceria com os artistas de grafite Irmãos Credo. As peças valorizam a cultura negra, utilizando elementos como grafismos africanos e tons dourados, marca registrada da FURIA.A linha inclui camisetas, calças e moletons, todos produzidos no Brasil, com foco em inclusão, identidade e orgulho racial.    

Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/colecoes/future-is-black
"""    
    hero="""Furia X My Hero Academia ⛩❤️🎮
    
Parceria com o anime "My Hero Academia" (Boku no Hero), focada em fãs da cultura pop japonesa e esports. A coleção traz camisetas, moletons e jaquetas com estampas de personagens icônicos como Deku, Bakugo e Todoroki. A linha mistura elementos do anime com o logo e o estilo urbano da FURIA, conquistando o público jovem e geek.

Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/collabs/my-hero-academia
    """
    
    zor="""Furia X Zor 🐾
    
A collab FURIA x ZOR une o estilo western ao lifestyle de Brino, influenciador conhecido por sua autenticidade. Inspirada no clipe "Todo Mundo Tá Tão Bem", a coleção traz peças que celebram a liberdade e as raízes do oeste americano, com toque urbano e moderno.

Com cores como cinza chumbo, preto, verde, bege e marrom, a linha mistura o casual com o funcional. Cada peça foi criada para contar uma história e refletir o estilo único de Brino, com modelagens marcantes e estampas exclusivas.

A coleção já está disponível em edição limitada no nosso site. Garanta a sua e mostre seu estilo com atitude!

Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/collabs/zor   
""" 
   
    love="""❤️Hard to Love X Harder to Kill💔
    
Esta coleção apresenta uma estética urbana e ousada, com peças como camisetas, moletons e croppeds. Os designs trazem frases impactantes e cores sóbrias, refletindo a resiliência e atitude da comunidade FURIA. Destaques incluem o Moletom Careca Azul Petróleo e a Camiseta Oversized Off White.        

Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/colecoes/hard-to-love-x-harder-to-kill
    """
    classic="""Furia Classic 🐾
    
Linha essencial da FURIA, com camisetas e moletons em cores neutras e design minimalista, ideal para quem busca versatilidade sem abrir mão da identidade da marca.

Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/colecoes/classic    
    """
    new_era="""Furia X New Era 🎮
    
Em agosto de 2023, a FURIA anunciou uma parceria com a renomada marca de headwear New Era, lançando uma coleção exclusiva de bonés e buckets. A linha inclui modelos clássicos como 9FIFTY, 9FORTY e 59FIFTY, essa colaboração visa integrar o estilo urbano ao universo gamer, reforçando o posicionamento da FURIA no segmento de lifestyle    

Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/collabs/new-era
    """
    panthera="""Magic Panthera 🐾
    
Parceria com o artista Guilherme Lemes, conhecido por misturar arte contemporânea com símbolos místicos. A "panthera" (pantera) é utilizada como símbolo de força, mistério e resistência. As peças têm uma vibe artística, com estampas exclusivas, camisetas, moletons e shorts, unindo streetwear com arte moderna. Reflete a ideia da FURIA como um movimento sociocultural, não apenas uma organização de esports.    
 
Confira a coleção em nosso site: 
👉https://www.furia.gg/produtos/colecoes/magic-panthera
    """
    
    match call.data:
        #Menu principal 
        case "botao_historia":    
            media = types.InputMediaPhoto(open("imagens/menu/furia_historia_image.jpg", "rb"), caption=historia)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_inicial())
        case "botao_time":
            media = types.InputMediaPhoto(open("imagens/menu/furia_time_image.jpg", "rb"), caption=time)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())
        case "botao_whatsapp":
            media = types.InputMediaPhoto(open("imagens/menu/furia_whatsapp_image.jpeg", "rb"), caption=whatsapp)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_inicial())
        case "botao_redes":
            media = types.InputMediaPhoto(open("imagens/menu/furia_redes_image.jpeg", "rb"), caption=redes)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_inicial())
        case "botao_loja":
            media = types.InputMediaPhoto(open("imagens/loja/furia_loja_image.jpg", "rb"), caption=loja)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
        case "botao_contato":
            media = types.InputMediaPhoto(open("imagens/menu/furia_contato_image.jpeg", "rb"), caption=contato)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=teclado_inicial())
        case "botao_voltar":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            enviar_menu(call.message.chat.id)

        #Menu do Time
        case "botao_fallen":
            media = types.InputMediaPhoto(open("imagens/time/furia_fallen_image.jpg", "rb"), caption=fallen)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())  
        case "botao_molodoy":
            media = types.InputMediaPhoto(open("imagens/time/furia_molodoy_image.jpeg", "rb"), caption=molodoy)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())
        case "botao_yuurih":
            media = types.InputMediaPhoto(open("imagens/time/furia_yuurih_image.jpeg", "rb"), caption=yuurih)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())      
        case "botao_yekindar":
            media = types.InputMediaPhoto(open("imagens/time/furia_yekindar_image.jpeg", "rb"), caption=yekindar)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())         
        case "botao_kscerato":
            media = types.InputMediaPhoto(open("imagens/time/furia_kscerato_image.jpg", "rb"), caption=kscerato)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_time())
        
        #Menu das Coleções
        case "botao_adidas":
            media = types.InputMediaPhoto(open("imagens/loja/furia_adidas_image.jpg", "rb"), caption=adidas)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
        case "botao_batman":
            media = types.InputMediaPhoto(open("imagens/loja/furia_batman_image.jpg", "rb"), caption=batman)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
        case "botao_champion":
            media = types.InputMediaPhoto(open("imagens/loja/furia_champion_image.jpg", "rb"), caption=champion)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())
        case "botao_future":                                        
            media = types.InputMediaPhoto(open("imagens/loja/furia_future_is_black_image.jpg", "rb"), caption=future)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())                   
        case "botao_hero":  
            media = types.InputMediaPhoto(open("imagens/loja/furia_my_hero_academia_image.jpg", "rb"), caption=hero)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())     
        case "botao_zor":                     
            media = types.InputMediaPhoto(open("imagens/loja/furia_zor_image.jpg", "rb"), caption=zor)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())            
        case "botao_love":
            media = types.InputMediaPhoto(open("imagens/loja/furia_hard_to_love_image.jpg", "rb"), caption=love)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())            
        case "botao_classic":    
            media = types.InputMediaPhoto(open("imagens/loja/furia_classic_image.jpg", "rb"), caption=classic)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())            
        case "botao_new_era":
            media = types.InputMediaPhoto(open("imagens/loja/furia_new_era_image.jpg", "rb"), caption=new_era)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())                       
        case "botao_panthera":    
            media = types.InputMediaPhoto(open("imagens/loja/furia_panthera_image.jpg", "rb"), caption=panthera)
            bot.edit_message_media(media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu_loja())            

bot.infinity_polling()