from cuenta import * 

#Definimos la clase
class Plazo_fijo(Cuenta):
    def __init__(self, fecha_vencimiento):
        self.fecha_vencimiento = fecha_vencimiento

    def retirar(self):
        
        cantidad = int(input("Introduce la cantidad que desea retirar: "))

        if 0 < cantidad < self.saldo:
            self.saldo = self.saldo - cantidad + (5/100 * cantidad)
            print("Se ha retirado correctamente")

        else:
            print("No tiene suficiente dinero")