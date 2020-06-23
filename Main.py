import telebot

bot = telebot.TeleBot("1233774770:AAE66yGNxBdMqjiIyKprdCpukqlGfztLksQ")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)

bot.polling( none_stop = True )
#conecting zenbook