from random import random
from Cuentas.cuenta import *
from Cuentas.plazo_fijo import * 
from Cuentas.vip import *
import random
from datetime import datetime

def eleccion_cuenta():
    print("¿Qué tipo de cuenta quieres abrir?:", "\n")
    print("1) Cuenta normal", "\n")
    print("2) Cuenta a plazo fijo", "\n")
    print("3) Cuenta VIP", "\n")
    n = int(input("Introduce aquí el número para seleccionar: "))

    if n == 1:
        cuenta = Cuenta() #Creamos el objeto
        #Datos de la cuenta
        cuenta.identificador = 12345678
        cuenta.titular = "Pelayo Huerta Mijares"
        cuenta.apertura = fecha_aleatoria()
        cuenta.numero_cuenta = random.randint(10**12, 10**13)
        cuenta.saldo = 10000
        
    if n == 2:
        cuenta = Plazo_fijo() #Creamos el objeto

    if n == 3:
        cuenta = Vip() #Creamos el objeto

def fecha_aleatoria():

    inicio = datetime(2017, 1, 30)
    final =  datetime(2017, 5, 28)

    random_date = inicio + (final - inicio) * random.random()

    return random_date





