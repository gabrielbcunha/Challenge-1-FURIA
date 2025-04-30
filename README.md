# 🐾 Challenge 1 - ChatBot FURIA

Bot interativo do Telegram inspirado na organização de eSports FURIA. Desenvolvido como parte do Challenge #1 da FURIA, este bot oferece informações sobre a equipe, produtos oficiais e canais de contato.

---

## 📸 Demonstração

"Clique [aqui](https://t.me/furiagg_bot) para acessar e interagir com o bot. 


---

## 🚀 Funcionalidades

- 📜 **Nossa História**: Conheça a trajetória da FURIA.  
- 🏆 **Nosso Time**: Informações sobre os jogadores da equipe.  
- 📱 **Bot WhatsApp**: Acesso direto ao bot oficial no WhatsApp.  
- 🎥 **Redes Sociais**: Links para as redes sociais da FURIA.  
- 🛒 **Lojinha da Pantera**: Catálogo de produtos oficiais.  
- ✉️ **Contate-nos**: Formas de entrar em contato com a equipe.  

---

## 🧰 Tecnologias Utilizadas

- [Python 3.13.1](https://www.python.org/)
- [Flask  3.1.0](https://github.com/pallets/flask/)
- [pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI)  
- [python-dotenv  1.1.0](https://github.com/motdotla/dotenv)
- [Render (para deploy)](https://render.com/)   

---

## 📦 Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/gabrielbcunha/Challenge-1-FURIA.git
cd Challenge-1-FURIA
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente:
🔐Obtenha o token de seu bot através do @BotFather no Telegram.  
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```bash
CHAVE_API=seu_token_do_bot
```

### 4. Inicie o bot:
```bash
python bot/telegram_bot.py
```
---

## 🛠️ Estrutura do Projeto 

```bash
Challenge-1-Chatbot-FURIA/
├── bot/
│   ├── telegram_bot.py
│   └── handlers/
│       ├── menu.py
│       ├── time.py
│       ├── loja.py
│       └── ...
├── static/
│   └── imagens/
│       └── ...
├── utils/
│   └── keep_alive.py
├── .env
├── LICENSE.md
├── README.md
└── requirements.txt
```

---

## 📄 Licença

Este projeto está licenciado sob a [MIT](LICENSE.md) License.

---

### 🤝 Contribuição

Contribuições são bem-vindas!   
Sinta-se à vontade para abrir issues ou enviar um pull request.
