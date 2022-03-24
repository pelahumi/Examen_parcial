from cuenta import *

#Definimos la clase
class Vip(Cuenta):

    def __init__(self, saldo_negativo):
        self.saldo_negativo = saldo_negativo #será un int negativo

    def retirar(self):

        cantidad = int(input("Introduce la cantidad que desea retirar: "))

        if cantidad > self.saldo and cantidad >= self.saldo_negativo:
            self.saldo = self.saldo - cantidad
            self.saldo_negativo = self.saldo_negativo + cantidad
            print("Se ha retirado correctamente")

        elif cantidad < self.saldo_negativo:
            print("Ha excedido el límite de saldo negativo")

        else:
            print("No tiene suficiente dinero")


