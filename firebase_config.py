import firebase_admin
from firebase_admin import credentials, firestore, storage
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "uma_chave_padrão")
    FIREBASE_KEY_PATH = os.getenv("FIREBASE_KEY_PATH", "firebase-key.json")
    FIREBASE_STORAGE_BUCKET = os.getenv("FIREBASE_STORAGE_BUCKET", "stockcloud35")  # Nome correto do bucket

# Inicializar Firebase apenas se ainda não foi inicializado
if not firebase_admin._apps:
    cred = credentials.Certificate(Config.FIREBASE_KEY_PATH)
    firebase_app = firebase_admin.initialize_app(cred, {
        'storageBucket': Config.FIREBASE_STORAGE_BUCKET
    })

# Inicializar o Firestore e o Firebase Storage
db = firestore.client()  # Referência ao Firestore
bucket = storage.bucket(Config.FIREBASE_STORAGE_BUCKET)  # Passando o nome do bucket diretamente
