import sqlite3

def create_db(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	cursor.execute('CREATE TABLE Users ([id_user] INTEGER PRIMARY KEY,[username] text UNIQUE, [password] text, [spublickey] text, [sprivatekey] text, [epublickey] text,[eprivatekey] text)')
	connect.commit()

def drop_db(db_path):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    cursor.execute('DROP TABLE IF EXISTS Users')
    connect.commit()

def add_user(db_path, username, password, spublickey, sprivatekey, epublickey, eprivatekey):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    sql = 'INSERT INTO Users (username, password, spublickey, sprivatekey, epublickey, eprivatekey) VALUES (?,?,?,?,?,?)'
    cursor.execute(sql,(username, password, spublickey, sprivatekey, epublickey, eprivatekey))
    connect.commit()
    return True

def delete_user(db_path, username):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	sql = 'DELETE FROM Users WHERE username=?'
	cursor.execute(sql,(username,))
	connect.commit()

def get_users(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	sql = 'SELECT username FROM Users;'
	users = cursor.execute(sql).fetchall()
	users = [user[0] for user in users]
	return users