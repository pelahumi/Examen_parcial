from cuenta import *

#Definimos la clase
class Vip(Cuenta):

    def __init__(self, saldo_negativo):
        self.saldo_negativo = saldo_negativo #será un int negativo

