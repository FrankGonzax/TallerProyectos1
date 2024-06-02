from django.urls import path
from . import views

app_name = 'agricultura'  

urlpatterns = [
    path('', views.get_api_data, name='data'),
    path('crear/', views.crearUsuario, name='crearUsuario'),
    path('iniciarSesion/', views.iniciarSesion, name='inicioSesion'),
    path('heladas/', views.pronosticoHelada, name='helada'),
]
