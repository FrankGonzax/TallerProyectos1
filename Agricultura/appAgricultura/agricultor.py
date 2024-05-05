from .models import Cuenta, Ubicacion

class Info():
    msg = str
    ubicacion = str
    temperatura = str
    recomendacion = str





def crearCuenta(cuenta, password, ubicacion):
    try:
        Cuenta.objects.get(cuenta = cuenta)
        return False
    except Cuenta.DoesNotExist:
        try:
            ub = Ubicacion.objects.get(pk = ubicacion)
            cuenta = Cuenta(cuenta = cuenta, password = password, ubicacion = ub)
            cuenta.save()
            return True
        except Ubicacion.DoesNotExist:
            return False
        
def comprobarUsuario(cuenta, password):
    try:
        c = Cuenta.objects.get(cuenta = cuenta, password = password)
        pk = c.ubicacion.pk
        return pk
    except Cuenta.DoesNotExist:
        return None