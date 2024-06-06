import sqlite3
from Models.Connection import Connection

from Utils.hash_password import HashPassword

class Database:

    def __init__(self) -> None:
        self.connection = Connection()
    
    def create_tables(self):
        self.connection.cursor.execute(""" CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, userName VARCHAR(100) NOT NULL, userEmail VARCHAR(100) NOT NULL UNIQUE, userPassword VARCHAR(100) NOT NULL, CHECK(userName <> ''), CHECK(userEmail <> ''))""")

        self.connection.cursor.execute(""" CREATE TABLE IF NOT EXISTS tasks (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, taskDesc VARCHAR(100) NOT NULL, taskStatus INTEGER(1) NOT NULL DEFAULT 0, idUser INTEGER NOT NULL REFERENCES users(id), CHECK(taskDesc <> ''), CHECK(taskStatus IN (0, 1)))""")

    def check_user(self, email):
        self.connection.cursor.execute(f'SELECT * FROM users WHERE userEmail = ?', (email,))
        user = self.connection.cursor.fetchone()
        return user