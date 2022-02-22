import sqlite3
from firebase import firebase

import constants


def get_user_token(user_email):
    firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', authentication=None)
    authentication = firebase.FirebaseAuthentication('THIS_IS_MY_SECRET', 'ozgurvt@gmail.com', extra={'id': 123})
    firebase.authentication = authentication
    user = authentication.get_user()
    return user.firebase_auth_token