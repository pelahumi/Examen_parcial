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
        cuenta.identificador = 1234567
        cuenta.titular = "Pelayo Huerta Mijares"
        cuenta.apertura = fecha_aleatoria()
        cuenta.numero_cuenta = random.randint(10**12, 10**13)
        cuenta.saldo = 10000
        
    if n == 2:
        cuenta = Plazo_fijo() #Creamos el objeto
        #Datos de la cuenta
        cuenta.identificador = 1234568
        cuenta.titular = "Pelayo Huerta Mijares"
        cuenta.apertura = fecha_aleatoria()
        cuenta.numero_cuenta = random.randint(10**12, 10**13)
        cuenta.saldo = 10000
        cuenta.fecha_vencimiento = fecha_aleatoria()

    if n == 3:
        cuenta = Vip() #Creamos el objeto
        #Datos de la cuenta
        cuenta.identificador = 1356789
        cuenta.titular = "Pelayo Huerta Mijares"
        cuenta.apertura = fecha_aleatoria()
        cuenta.numero_cuenta = random.randint(10**12, 10**13)
        cuenta.saldo = 10000
        cuenta.saldo_negativo = random.randint(-1000, -500)

def fecha_aleatoria():

    inicio = datetime(2020, 1, 1)
    final =  datetime(2022, 3, 24)

    random_date = inicio + (final - inicio) * random.random()

    return random_date

def accion(cuenta):
    print("¿Qué acción desea hacer?:", "\n")
    r = str(input())

    if r == "Ingresar" or r == "ingresar":
        cuenta.ingreso()

    if r == "Retirar" or r == "retirar":
        cuenta.retirar()

    if r == "Consultar" or r == "consultar":
        cuenta.consultar_datos()

    if r == "Transferir" or r == "transferir":
        transferir()

def transferir(cuenta):
    print("¿Cuan")







