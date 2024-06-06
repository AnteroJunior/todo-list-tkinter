from Models.Connection import Connection

class User:

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

    def add_user(self):
        try:    
            cnx = Connection()
            cnx.cursor.execute('INSERT INTO users (userName, userEmail, userPassword) VALUES (?, ?, ?)', (self.name, self.email, self.password,))
            cnx.cnx.commit()
            cnx.cnx.close()
        except ConnectionError:
            print('Erro durante a inserção do usuário. Tente novamente.')