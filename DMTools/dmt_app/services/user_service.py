import sqlite3

import constants

def get_user_by_id(user_id):
    con = sqlite3.connect(constants.PY_SERVICES_DATABASE_NAME)
    cur = con.cursor()
    user = ''
    for row in cur.execute(f'SELECT * FROM users WHERE id = {user_id}'):
        user = row
        print(user)
    con.close()
    return user