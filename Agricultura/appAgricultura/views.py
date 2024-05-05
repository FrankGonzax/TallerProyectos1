import requests
from django.http import JsonResponse
from .agricultor import crearCuenta, comprobarUsuario
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Ubicacion
from .key import get_apikey

def get_api_data(request):
    # Es importante utilizar correctamente las API keys en las URLs, sin corchetes '{}' de más.
    api_key = get_apikey()
    url = f'https://api.openweathermap.org/data/2.5/weather?lat=-12.06513&lon=-75.20486&appid={api_key}'

    # Realiza el pedido a la API
    response = requests.get(url)
    
    # Comprueba el código de estado de la respuesta HTTP
    if response.status_code == 200:
        # Si es 200 OK, parsea la respuesta JSON y envíala de vuelta como JsonResponse
        data = response.json()  # Convierte la respuesta a diccionario
        return JsonResponse(data)  # Usa JsonResponse para devolver un objeto de respuesta HTTP adecuado
    else:
        # Si la respuesta no es 200, maneja el error devolviendo un estado de error con JsonResponse
        return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)


def data_temp(ubicacion):
    lat = ''
    lon = ''
    if (ubicacion == 1):
        lat = '-12.06513'
        lon = '-75.20486'
    elif (ubicacion == 2):
        lat = '-12.0617'
        lon = '-75.2878'
    elif (ubicacion == 3):
        lat = '-11.91762'
        lon = '-75.31401'
    elif (ubicacion == 4):
        lat = '-11.77584'
        lon = '-75.49656'
    elif (ubicacion == 5):
        lat = '-11.41899'
        lon = '-75.68992'
    elif (ubicacion == 6):
        lat = '-11.7118'
        lon = '-75.47257'
    elif (ubicacion == 7):
        lat = '-11.15895'
        lon = '-75.99304'
    api_key = get_apikey()
    #url = f'https://api.openweathermap.org/data/2.5/weather?lat=-12.06513&lon=-75.20486&appid={api_key}'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Convierte la respuesta a diccionario
        temperatura = data['main']['temp']
        temperatura = temperatura - 273.15
        temp_red = round(temperatura, 2)
        return temp_red  # Usa JsonResponse para devolver un objeto de respuesta HTTP adecuado
    else:
        return None
    

@api_view(['POST'])
@csrf_exempt   
def crearUsuario(request):
   data = json.loads(request.body)  # Carga los datos como JSON
   cuenta = data['cuenta']
   password = data['password']
   ubicacion = data['u']
   msg = crearCuenta(cuenta, password, ubicacion)
   if(msg == False):
       respuesta = {"mensaje": "fallo", "status": "success"}
       return Response(respuesta, status=status.HTTP_200_OK)
   elif(msg == True):
        respuesta = {"mensaje": "exito", "status": "success"}
        return Response(respuesta, status=status.HTTP_200_OK)

@api_view(['POST'])
@csrf_exempt   
def iniciarSesion(request):
    data = json.loads(request.body)
    cuenta = data['cuenta']
    password = data['password']
    msg = comprobarUsuario(cuenta, password)
    if(msg == 1 or msg == 2 or msg == 3 or msg == 4 or msg == 5 or msg == 6 or msg == 7):
        u = Ubicacion.objects.get(pk = msg)
        ubicacion = u.nombre
        #temp = str(data_temp(msg))
        #respuesta = {"mensaje": "exito", "temperatura" : temp, "ubicacion" : ubicacion, "status": "success"}
        respuesta = {"mensaje": "exito", "temperatura" : '28', "ubicacion" : ubicacion, "status": "success"}
        return Response(respuesta, status=status.HTTP_200_OK)
    else:
        respuesta = {"mensaje": "fallo", "status": "success"}
        return Response(respuesta, status=status.HTTP_200_OK)