import telebot

main_keyboard=telebot.types.ReplyKeyboardMarkup(True, True)  
main_keyboard.row('Добавить напоминание', 'Управление напоминаниями')

