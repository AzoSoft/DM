import sqlite3
import constants

def get_cursor():
    con = sqlite3.connect(constants.PY_SERVICES_DATABASE_NAME)
    return con.cursor()

def create_table():
    cur = get_cursor()
    cur.execute('''CREATE TABLE project (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT(255),
            description TEXT(255),
            CONSTRAINT dungeon_master FOREIGN KEY (id) REFERENCES users(id)
        );''')
    
