#Creamos la clase
from tkinter.filedialog import SaveFileDialog


class Cuenta():
    
    #Definimos el constructor y los atributos de la clase
    def __init__(self, ID, titular, apertura, numero_cuenta, saldo):
        self.ID = ID #será una variable tipo int
        self.titular = titular #será una variable tipo str
        self.apertura = apertura #será una variable tipo int
        self.numero_cuenta = numero_cuenta #será una variable tipo int
        self.saldo = saldo #será una variable tipo int
