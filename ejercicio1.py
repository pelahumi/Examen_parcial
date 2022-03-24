#Creamos la clase
class Libro:
    
    #Definimos el constructor con los atributos de la clase
    def __init__(self, titulo, autor, paginas, isbn):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn

    #Creamos los getter
    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_paginas(self):
        return self.paginas

    def get_isbn(self):
        return self.isbn
    
