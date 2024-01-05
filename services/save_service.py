import sqlite3
from datetime import datetime


class SaveService:
    db_name = 'forager.db'

    def __init__(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS task_progress (
                id INTEGER PRIMARY KEY,
                task_name TEXT NOT NULL,
                date DATETIME NOT NULL,
                status TEXT NOT NULL
                )
                ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS email_status (
                id INTEGER PRIMARY KEY,
                email TEXT NOT NULL,
                status TEXT NOT NULL
                )
                ''')
            self.connection.commit()
            print("Connecting to DB")
        except sqlite3.Error as error:
            print("DB connection error", error)

    def db_add_data(self, email, status):

        if self.cursor.execute(
                'SELECT * FROM email_status WHERE email = ?',
                (email,)
        ).fetchall():
            self.db_update_data(email, status)
        else:
            try:
                self.cursor.execute(
                    'INSERT INTO task_progress (task_name, date, status) VALUES (?, ?, ?)',
                    ("email_verification", datetime.now(), "insert")
                )
                self.cursor.execute(
                    'INSERT INTO email_status (email, status) VALUES (?, ?)',
                    (email, status)
                )
                self.connection.commit()
                self.cursor.close()
                print('Values insert successfully')
            except sqlite3.Error as error:
                print("DB connection error", error)
            finally:
                if (self.connection):
                    self.connection.close()
                    print("Connection closed")

    def db_update_data(self, email, status):
        try:
            self.cursor.execute(
                'INSERT INTO task_progress (task_name, date, status) VALUES (?, ?, ?)',
                ("email_verification", datetime.now(), "updated")
            )
            self.cursor.execute(
                'UPDATE email_status SET status = ? WHERE email = ?',
                (email, status)
            )
            self.connection.commit()
            self.cursor.close()
            print('Values updated successfully')
        except sqlite3.Error as error:
            print("DB connection error", error)
        finally:
            if (self.connection):
                self.connection.close()
                print("Connection closed")
