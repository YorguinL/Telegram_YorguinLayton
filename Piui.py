import telebot

TOKEN = '950165408:AAG6-1ERYNRik7-ssybW12LWIcxLUhhHHu4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Heeeey!")

@bot.message_handler ( func = lambda  m : True )
def  echo_all(message):
    print(message.chat.id)
    bot.reply_to(message, message.text)

bot.send_message('673273081', 'JAJ es broma')
bot.send_message('673273081', '')


bot.polling()
