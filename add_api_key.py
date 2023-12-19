import sqlite3
import time
import secrets

connection = sqlite3.connect("data.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS keys(
		auth_key TEXT PRIMARY KEY,
		creation_timestamp INTEGER
	)
""")

def generate_key():
	key = secrets.token_hex(16)
	cursor.execute("""
		INSERT INTO keys (auth_key, creation_timestamp)
		VALUES (?, ?)
	""", (key, int(time.time())))

	connection.commit()
	print(key)

generate_key()
connection.close()