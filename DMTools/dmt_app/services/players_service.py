import sqlite3
import constants

def get_cursor():
    con = sqlite3.connect(constants.PY_SERVICES_DATABASE_NAME)
    return con.cursor()

def create_table():
    cur = get_cursor()
    cur.execute('''CREATE TABLE players (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            CONSTRAINT player FOREIGN KEY (id) REFERENCES users(id),
            CONSTRAINT project FOREIGN KEY (id) REFERENCES project(id)
        );
        ''')