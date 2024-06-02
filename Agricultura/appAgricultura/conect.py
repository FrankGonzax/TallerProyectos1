import firebase_admin
from firebase_admin import credentials, db

# Inicializar Firebase
cred = credentials.Certificate('appAgricultura/credentials/credenciales.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://agriculturaapp-39eb8-default-rtdb.firebaseio.com/'
})

def pronostico(dia):
    d = int(dia)
    ref = db.reference('Pronostico')
    try:
        data = ref.get()
        if data is None:
            print("No data found at the specified reference.")
        ultima_llave = list(data.keys())[-d]
        ultimos_datos = data[ultima_llave]
        return ultimos_datos
    except Exception as e:
        print("Error retrieving data:", e)
        return None