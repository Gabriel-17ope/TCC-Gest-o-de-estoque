import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()

class FirebaseSDK:
    FIREBASE_KEY_PATH = os.getenv("FIREBASE_KEY_PATH", "path/to/serviceAccountKey.json")

    # Inicialização do Firebase Admin
    cred = credentials.Certificate(FIREBASE_KEY_PATH)
    firebase_app = firebase_admin.initialize_app(cred)

    # Instância do Firestore
    db = firestore.client()

# Exporta a instância do Firestore como 'db'
db = FirebaseSDK.db
