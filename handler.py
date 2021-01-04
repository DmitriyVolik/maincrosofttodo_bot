import keyboards as kb
import sql

class Handler:

    

    def __init__(self, bot):
         self.__bot=bot
         self.__db=sql.Database()
         
         
    def start_handler(self, message):

        self.__db.add_user(message.from_user.id)
        self.__bot.send_message(message.from_user.id,"Привет! Я бот напоминалка, буду помагать тебе меньше прокрастинировать)", reply_markup=kb.main_keyboard)

    def handle_text(self, message):

        if message.text=="Добавить напоминание":
            
            self.__bot.send_message(message.from_user.id, "Введите текст напоминания:")
            self.__db.set_state(message.from_user.id, "get_remind_text")

        elif self.__db.get_state()=="get_remind_text":
            print("fef")


            
            

