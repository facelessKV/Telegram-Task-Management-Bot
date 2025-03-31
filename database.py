import sqlite3
import datetime

class Database:
    def __init__(self, db_file):
        """
        Инициализация подключения к базе данных
        :param db_file: Путь к файлу базы данных SQLite
        """
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self._create_tables()
    
    def _create_tables(self):
        """Создание необходимых таблиц, если они не существуют"""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT FALSE,
            date TEXT NOT NULL
        )
        """)
        self.connection.commit()
    
    def add_task(self, user_id, task_text):
        """
        Добавление новой задачи
        :param user_id: ID пользователя в Telegram
        :param task_text: Текст задачи
        :return: ID добавленной задачи
        """
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            "INSERT INTO tasks (user_id, text, done, date) VALUES (?, ?, ?, ?)",
            (user_id, task_text, False, date)
        )
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_all_tasks(self, user_id):
        """
        Получение всех задач пользователя
        :param user_id: ID пользователя в Telegram
        :return: Список задач пользователя
        """
        self.cursor.execute(
            "SELECT id, text, done, date FROM tasks WHERE user_id = ? ORDER BY date",
            (user_id,)
        )
        return self.cursor.fetchall()
    
    def get_task(self, task_id, user_id):
        """
        Получение конкретной задачи пользователя
        :param task_id: ID задачи
        :param user_id: ID пользователя в Telegram
        :return: Задача или None, если задача не найдена
        """
        self.cursor.execute(
            "SELECT id, text, done, date FROM tasks WHERE id = ? AND user_id = ?",
            (task_id, user_id)
        )
        return self.cursor.fetchone()
    
    def mark_done(self, task_id, user_id):
        """
        Отметить задачу как выполненную
        :param task_id: ID задачи
        :param user_id: ID пользователя в Telegram
        :return: True если задача найдена и обновлена, иначе False
        """
        if not self.get_task(task_id, user_id):
            return False
        
        self.cursor.execute(
            "UPDATE tasks SET done = TRUE WHERE id = ? AND user_id = ?",
            (task_id, user_id)
        )
        self.connection.commit()
        return True
    
    def remove_task(self, task_id, user_id):
        """
        Удалить задачу
        :param task_id: ID задачи
        :param user_id: ID пользователя в Telegram
        :return: True если задача найдена и удалена, иначе False
        """
        if not self.get_task(task_id, user_id):
            return False
        
        self.cursor.execute(
            "DELETE FROM tasks WHERE id = ? AND user_id = ?",
            (task_id, user_id)
        )
        self.connection.commit()
        return True
    
    def close(self):
        """Закрытие соединения с базой данных"""
        self.connection.close()