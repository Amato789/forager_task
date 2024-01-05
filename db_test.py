import sqlite3

connection = sqlite3.connect('forager.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM email_status')
emails = cursor.fetchall()
for email in emails:
    print(email)

cursor.execute('SELECT * FROM task_progress')
emails = cursor.fetchall()
for email in emails:
    print(email)


# cursor.execute('SELECT * FROM email_status WHERE email = ?', ('maximsidorchuk@gmail.com', ))
# print(cursor.fetchall())

cursor.close()
connection.close()



# def sql_connect():
#     try:
#         connection = sqlite3.connect('forager.db')
#         cursor = connection.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS task_progress (
#             id INTEGER PRIMARY KEY,
#             task_name TEXT NOT NULL,
#             date TEXT NOT NULL,
#             status TEXT NOT NULL
#             )
#             ''')
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS email_status (
#             id INTEGER PRIMARY KEY,
#             email TEXT NOT NULL,
#             status TEXT NOT NULL
#             )
#             ''')
#         connection.commit()
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при подключении к sqlite", error)
#     finally:
#         if (connection):
#             connection.close()
#             print("Соединение с SQLite закрыто")


# def sql_add_data(email, status):
#     try:
#         connection = sqlite3.connect('forager.db')
#         cursor = connection.cursor()
#         cursor.execute(
#             'INSERT INTO task_progress (task_name, date, status) VALUES (?, ?, ?)',
#             ("email_verification", "date", "success")
#         )
#         cursor.execute(
#             'INSERT INTO email_status (email, status) VALUES (?, ?)',
#             (email, status)
#         )
#         connection.commit()
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при подключении к sqlite", error)
#     finally:
#         if (connection):
#             connection.close()
#             print("Соединение с SQLite закрыто")
#
#
# def sql_update_data():
#     try:
#         connection = sqlite3.connect('forager.db')
#         cursor = connection.cursor()
#         cursor.execute(
#             'UPDATE email_status SET status = ? WHERE email = ?',
#             ('verified', 'maximsidorchuk@gmail.com')
#         )
#         connection.commit()
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при подключении к sqlite", error)
#     finally:
#         if (connection):
#             connection.close()
#             print("Соединение с SQLite закрыто")
#
#
# def sql_delete_data():
#     try:
#         connection = sqlite3.connect('forager.db')
#         cursor = connection.cursor()
#         cursor.execute(
#             'DELETE FROM email_status WHERE email = ?',
#             ('maximsidorchuk@gmail.com',)
#         )
#         connection.commit()
#     except sqlite3.Error as error:
#         print("Ошибка при подключении к sqlite", error)
#     finally:
#         if (connection):
#             connection.close()
#             print("Соединение с SQLite закрыто")
#
#
# def sql_select_all():
#     try:
#         connection = sqlite3.connect('forager.db')
#         cursor = connection.cursor()
#         cursor.execute('SELECT * FROM email_status')
#         emails = cursor.fetchall()
#         for email in emails:
#             print(email)
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка при подключении к sqlite", error)
#     finally:
#         if (connection):
#             connection.close()
#             print("Соединение с SQLite закрыто")
#
