#Creamos la clase
class Cuenta():
    
    #Definimos el constructor y los atributos de la clase
    def __init__(self, ID, titular, apertura, numero_cuenta, saldo):
        self.ID = ID #será una variable tipo int
        self.titular = titular #será una variable tipo str
        self.apertura = apertura #será una variable tipo int
        self.numero_cuenta = numero_cuenta #será una variable tipo int
        self.saldo = saldo #será una variable tipo int

    def ingreso(self):

        cantidad = int(input("Introduce la cantidad que desea ingresar: "))

        self.saldo = self.saldo + cantidad
        print("Se ha ingresado correctamente")



    def retirar(self):
        
        cantidad = int(input("Introduce la cantidad que desea retirar: "))

        if 0 < cantidad < self.saldo:
            self.saldo = self.saldo - cantidad
            print("Se ha retirado correctamente")

        else:
            print("No tiene suficiente dinero")

    
