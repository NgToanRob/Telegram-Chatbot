import telebot
from chatterbot import ChatBot

TOKEN_API = '5946477684:AAFDSQS9OKwy80yJIc1Py5Mz_Pr1sXk4lvI'
bot = telebot.TeleBot(TOKEN_API)

chat_engine = ChatBot("Chatpot")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def custom_reply(message):
    mes_reply = chat_engine.get_response(message.text)
    bot.send_message(message.chat.id, mes_reply)


bot.infinity_polling()
