import sqlite3
import constants

def get_cursor():
    con = sqlite3.connect(constants.PY_SERVICES_DATABASE_NAME)
    return con.cursor()

def create_table():
    cur = get_cursor()
    cur.execute('''CREATE TABLE journal_entries (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            file_path TEXT NOT NULL,
            last_modified INTEGER NOT NULL,
            CONSTRAINT player_id FOREIGN KEY (id) REFERENCES users(id)
        );
        ''')
    
