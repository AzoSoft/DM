import os
from dotenv import load_dotenv

load_dotenv()

PY_SERVICES_DATABASE_NAME="db"
PY_SERVICES_FIREBASE_URL="https://your_storage.firebaseio.com"
PY_SERVICES_FIREBASE_API_KEY=os.getenv("DM_PY_FIREBASE_API_KEY")
PY_SERVICES_FIREBASE_REGISTER_URL="https://identitytoolkit.googleapis.com/v1/accounts:signUp"
PY_SERVICES_FIREBASE_LOGIN_URL="https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"