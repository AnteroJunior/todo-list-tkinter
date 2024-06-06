from Models.Connection import Connection

class Task:

    def __init__(self, description) -> None:
        self.description = description
    
    @staticmethod
    def get_user_tasks(id):
        try:
            cnx = Connection()
            cnx.cursor.execute('SELECT id, taskDesc, taskStatus FROM tasks WHERE idUser = ?', (id,))

            res = cnx.cursor.fetchall()
            tasks = []
            for task in res:
                tasks.append({
                    'id': task[0],
                    'taskDesc': task[1],
                    'taskStatus': 'Doing' if task[2] == 0 else 'Done'
                })
                
            return tasks

        except ConnectionError:
            print('Erro durante a inserção do usuário. Tente novamente.')

    @staticmethod
    def add_task(desc: str, id: int):
        try:
            cnx = Connection()
            cnx.cursor.execute('INSERT INTO tasks (taskDesc, idUser) VALUES (?, ?)', (desc, id,))
            cnx.cnx.commit()

            cnx.cnx.close()

        except ConnectionError:
            print('Erro durante a inserção do usuário. Tente novamente.')

    @staticmethod
    def update_task(id: int, new_desc: str):
        try:
            cnx = Connection()
            cnx.cursor.execute('UPDATE tasks SET taskDesc = ? WHERE id = ?', (new_desc, id,))
            cnx.cnx.commit()
            cnx.cnx.close()

        except ConnectionError:
            print('Erro durante a inserção do usuário. Tente novamente.')
    
    @staticmethod
    def mark_as_done(id: int):
        try:
            cnx = Connection()
            cnx.cursor.execute('UPDATE tasks SET taskStatus = 1 WHERE id = ?', (id,))
            cnx.cnx.commit()

            cnx.cnx.close()

        except ConnectionError:
            print('Erro durante a inserção do usuário. Tente novamente.')
    
    @staticmethod
    def mark_as_inprogress(id: int):
        try:
            cnx = Connection()
            cnx.cursor.execute('UPDATE tasks SET taskStatus = 0 WHERE id = ?', (id,))
            cnx.cnx.commit()
            cnx.cnx.close()

        except ConnectionError:
            print('Erro durante a inserção do usuário. Tente novamente.')

    @staticmethod
    def delete_task(id: int):
        try:
            cnx = Connection()
            cnx.cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
            cnx.cnx.commit()
            cnx.cnx.close()

        except ConnectionError:
            print('Erro durante a inserção do usuário. Tente novamente.')