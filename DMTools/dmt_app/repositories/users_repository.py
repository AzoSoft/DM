import sqlite3
import constants

def get_connection():
    return sqlite3.connect(constants.PY_SERVICES_DATABASE_NAME)

def create_table():
    con = get_connection()
    cur = con.cursor()
    cur.execute('''CREATE TABLE users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            authentication_id TEXT NOT NULL,
            CONSTRAINT users_UN_auth UNIQUE (authentication_id),
            CONSTRAINT users_UN UNIQUE (id)
        );
        CREATE INDEX users_id_IDX ON users (id);''')

def get_user_by_id(user_id):
    con = get_connection()
    cur = con.cursor()
    user = ''
    for row in cur.execute(f'SELECT * FROM users WHERE id = {user_id}'):
        user = row
        print(user)
    con.close()
    return user

    CREATE TABLE project (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT(255),
	description TEXT(255),
	CONSTRAINT dungeon_master FOREIGN KEY (id) REFERENCES users(id)
);
