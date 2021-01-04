import config
import telebot
import datetime
import keyboards as kb
import handler
import sql

bot = telebot.TeleBot(config.TOKEN)



hd=handler.Handler(bot)

print("Start")

print(bot.get_me())

@bot.message_handler(commands=['start'])
def handle_command(message): #Проверяем команды от пользователя
    hd.start_handler(message)
    

@bot.message_handler(content_types=['text']) 
def handle_message(message):
    hd.handle_text(message)




bot.polling(none_stop=True, interval=0)