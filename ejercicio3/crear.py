from Cuentas.cuenta import *
from Cuentas.plazo_fijo import * 
from Cuentas.vip import *

def eleccion_cuenta():
    print("¿Qué tipo de cuenta quieres abrir?:", "\n")
    print("1) Cuenta normal", "\n")
    print("2) Cuenta a plazo fijo", "\n")
    print("3) Cuenta VIP", "\n")
    n = int(input("Introduce aquí el número para seleccionar: "))

    if n == 1:
        cuenta = Cuenta()

    if n == 2:
        cuenta = Plazo_fijo()

    if n == 3:
        cuenta = Vip()


