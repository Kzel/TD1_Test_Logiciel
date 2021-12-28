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

def verify_username_length(db_path, username):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    sql = 'SELECT username, LENGTH(username) FROM Users;'
    users = cursor.execute(sql ).fetchall()
    users = [user[0] for user in users]
    
    for i in users:
        if i == username:
            print(i)
            if len(i) <=3:
                return False
            else:
                return True
    return None

def verify_username_special_characters(db_path, username):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    sql = 'SELECT username FROM Users;'
    users = cursor.execute(sql ).fetchall()
    users = [user[0] for user in users]
    for i in users:
        if i == username:
            if (any(not i.isalnum() for i in username)):
                return True
            else:
                return False
    return None
        
def verify_key_length(db_path, username):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    sql = 'SELECT LENGTH(spublickey), LENGTH(sprivatekey), LENGTH(epublickey), LENGTH(eprivatekey) FROM Users WHERE username=?'
    keys = cursor.execute(sql, (username,)).fetchall()
    key = []
    for i in range(4):
        key += [key[i] for key in keys]
    for i in key:
        if i > 128:
            return False
        else:
            continue
    connect.commit()
    return True

def verify_password(db_path, username):
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    sql = 'SELECT password FROM Users WHERE username=?'
    passwords = cursor.execute(sql, (username,)).fetchall()
    password = [password[0] for password in passwords]
    is_digital = 0
    is_special = 0
    is_upper = 0
    is_lower = 0
    for i in password:
        if len(i) < 8:
            return False
        else:
            if (any(not c.isdigit() for c in password)):
                is_digital= 1
            if (any(not c.isalnum() for c in password)):
                is_special = 1
            if (any(not c.islower() for c in password)):
                is_lower = 1
            if (any(not c.isupper() for c in password)):
                is_upper = 1
            if is_digital and is_special and is_lower and is_upper:
                continue
            else:
                return False
    return True

