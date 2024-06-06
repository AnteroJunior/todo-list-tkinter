import sqlite3

class Connection:

    def __init__(self) -> None:
        try:
            self.cnx = sqlite3.connect('todo_list.db')
            self.cursor = self.cnx.cursor()
        except ConnectionError:
            print('Could not connect to database todo_list.db')