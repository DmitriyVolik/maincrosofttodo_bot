import sqlite3

class Database:


    def __init__(self):

        self.__db=sqlite3.connect('database.db', check_same_thread=False)
        self.__sql=self.__db.cursor()

        self.__sql.execute("""CREATE TABLE IF NOT EXISTS users (
        id int not null,
        state text
        )""") 

        self.__sql.execute("""create table IF NOT EXISTS reminders
        (
        user_id int not null,
        text int not null
        day int not null
        time text not null
        )""")

    def add_user(self,id):
        
        self.__sql.execute(f"SELECT id FROM users WHERE id= '{id}'")
        if self.__sql.fetchone()is None:
            self.__sql.execute(f"INSERT INTO users(id) VALUES ({id})")
            self.__db.commit()

    def get_state(self):
        self.__sql.execute(f"SELECT active_funk FROM users WHERE id='{id}'")
        return self.__sql.fetchone()[0]

    def set_state(self, id, state):
        self.__sql.execute(f'UPDATE users SET state = "{state}" WHERE id="{id}"')
        self.__db.commit()

    def
    










