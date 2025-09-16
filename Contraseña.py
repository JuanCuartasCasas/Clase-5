#Autores:Santiago Lopez,Juan Diego Cuartas,Andres Mauricio Cepeda
#Motivo:Actividad 3
import re

class Contraseña:
    def __init__(self,contraseña):
        self.contraseña =contraseña

    def validar(contraseña):
        if contraseña:
            tiene_mayuscula = re.search(r'[A-Z]', contraseña)
            tiene_minuscula = re.search(r'[a-z]', contraseña)
            tiene_numero = re.search(r'[0-9]', contraseña)
            if (tiene_mayuscula and tiene_minuscula and tiene_numero):
                print("Si cumple con los requisitos")
            else:
                print("No cumple con los requisitos")
