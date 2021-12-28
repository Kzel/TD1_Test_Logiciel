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

