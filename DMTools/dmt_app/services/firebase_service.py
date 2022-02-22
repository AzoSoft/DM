import sqlite3
import requests

from ..constants import *

class FirebaseService:
    def register_user(user_email, user_password):
        try:
            user_token_response = requests.post(
            PY_SERVICES_FIREBASE_LOGIN_URL,
            params={"key": PY_SERVICES_FIREBASE_API_KEY},
            data={'email': user_email, 
                'password': user_password,
                'returnSecureToken': True},
                verify=True)
            
            if user_token_response.status_code == 400:
                response_json = user_token_response.json()
                if response_json["error"]["message"] == "EMAIL_EXISTS":
                    print(f"The email {user_email} is already in use.")
                    raise Exception(f"The email {user_email} is already in use.")
            if user_token_response.status_code == 200:
                response_json = user_token_response.json()
                return {"email": user_email, "token": response_json["idToken"]}
            else:
                print(f"An error ocurred trying to login user {user_email}")
                raise Exception(f"An error ocurred trying to login user {user_email}")
        except ValueError:
            print(f"An error ocurred trying to register for user {user_email}")
            raise Exception(f"An error ocurred trying to register for user {user_email}")

    def get_user_data(user_email, user_password):
        try:
            user_token_response = requests.post(
            PY_SERVICES_FIREBASE_LOGIN_URL,
            params={"key": PY_SERVICES_FIREBASE_API_KEY},
            data={'email': user_email, 
                'password': user_password,
                'returnSecureToken': True},
                verify=True)

            if user_token_response.status_code == 200:
                response_json = user_token_response.json()
                return {"email": user_email, "token": response_json["idToken"]}
            else:
                print(f"An error ocurred trying to login user {user_email}")
                raise Exception(f"An error ocurred trying to login user {user_email}")
        except ValueError:
            print(f"An error ocurred trying to obtain the token for user {user_email}")
            pass