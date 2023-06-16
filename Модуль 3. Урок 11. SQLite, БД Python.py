import sqlite3


class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


def create_table_user(cursor):
    command = """
    CREATE TABLE IF NOT EXISTS user (
      id INTEGER PRIMARY KEY,
      name TEXT,
      surname TEXT,
      gender TEXT)
    """
    cursor.execute(command)



def add_user(cursor,user):
    command = '''
    INSERT INTO user(name, surname, gender)
    VALUES (?,?,?)
    '''
    cursor.execute(command, (user.name, user.surname, user.gender))



def get_users_list(cursor):
    command = '''
      SELECT * FROM user 
    ''' # * - вся инфа



    result = cursor.execute(command)
    print(result)
    users = result.fetchall() #превращает инфу ячейки памяти в привычный вид
    print(users)



def update_user_name(cursor, value, user_id):
    command = '''
        UPDATE user
        SET name = ?
        WHERE id = ?
    '''
    cursor.execute(command, (value, user_id))

def delete_users(cursor):
    command = '''
    DELETE FROM user
    '''
    cursor.execute(command)

def delete_custom_user(cursor):
    command = '''
    DELETE FROM user
    WHERE id = 1
    '''
    cursor.execute(command)

def get_user(cursor, name):
    command = '''
      SELECT * FROM user
      WHERE name = ?
      '''
    cursor.execute(command,(name,)) #запятая дописывается, если элемент только один

# def get_male_users(cursor, male):
#     command = '''
#       SELECT * FROM user
#       WHERE gender = 'male'
#       '''
#     cursor.execute(command,(male,)) #запятая дописывается, если элемент только один


with sqlite3.connect('data.db') as cursor:
 create_table_user(cursor)
 # delete_users(cursor)

 add_user(cursor, User('Иван', 'Иванов', 'male'))
 add_user(cursor, User('Анна', 'Петровна', 'female'))


 get_user(cursor, 'Пётр')
 update_user_name(cursor, 'Никита', 1)
 delete_custom_user(cursor)

 get_users_list(cursor)
