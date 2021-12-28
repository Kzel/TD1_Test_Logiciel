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

def get_password(db_path, username):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	sql = 'SELECT password FROM Users WHERE username=?'
	passwords = cursor.execute(sql,(username,)).fetchall()
	return passwords[0][0]

def log(db_path, username, password):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    sql = "SELECT username, password FROM Users WHERE username=?"
    log = cursor.execute(sql, (username,)).fetchall()
    users = str(log[0][0])
    passwords = get_password(db_path, username)
    if users == username and passwords == password:
        return True
    else:
        return False
    
def get_spubkey(db_path, username):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	sql = 'SELECT spublickey FROM Users WHERE username=?'
	spubkeys = cursor.execute(sql, (username,)).fetchall()
	return spubkeys[0][0]

def get_sprikey(db_path, username):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	sql = 'SELECT sprivatekey FROM Users WHERE username=?'
	sprikeys = cursor.execute(sql, (username,)).fetchall()
	return sprikeys[0][0]

def get_epubkey(db_path, username):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	sql = 'SELECT epublickey FROM Users WHERE username=?'
	epubkeys = cursor.execute(sql, (username,)).fetchall()
	return epubkeys[0][0]

def get_eprikey(db_path, username):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	sql = 'SELECT eprivatekey FROM Users WHERE username=?'
	eprikeys = cursor.execute(sql, (username,)).fetchall()
	return eprikeys[0][0]