#Definimos la clase padre que engloba al resto
class Animal():
    #Definimos su constructor y sus atributos
    def __init__(self):
        pass

#Definimos las clases hijo que heredan los atributos y métodos de la clase padre y además pueden tener otros propios
class Mamifero(Animal):
    #Definimos el constructor con los atributos de la clase padre y los suyos propios
    def __init__(self, pelo):
        self.pelo = pelo #Los mamíferos son los únicos animales con pelo

class Oviparo(Animal):
    def __init__(self, huevo):
        self.huevo = huevo #Los ovíparos son los únicos animales que ponen huevos

#Definimos ahora las clases que heredan de las clases hijo
class Gato(Mamifero): #Es como la clase mamífero pero únicamente con las características de los gatos
    def __init__(self):
        pass

class Pollo(Oviparo): #Es como la clase oviparo pero únicamente con las características de los pollos
    def __init__(self):
        pass

class Ornitorrinco(Mamifero, Oviparo): #Herencia múltiple porque el ornitorrinco es un mamifero oviparo
    def __init__(self):
        pass


