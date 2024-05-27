import firebase_admin
from firebase_admin import credentials, db

# Inicializar Firebase
cred = credentials.Certificate('appAgricultura/credentials/credenciales.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://agriculturaapp-39eb8-default-rtdb.firebaseio.com/'
})

def pronostico():
    ref = db.reference('Pronostico/2')
    return ref.get()

def pronostico2():
    ref = db.reference('Pronostico')
    try:
        data = ref.get()
        if data is None:
            print("No data found at the specified reference.")
        return data
    except Exception as e:
        print("Error retrieving data:", e)
        return None

