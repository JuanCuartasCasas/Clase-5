from Contraseña import Contraseña
def actividad():
    class Persona:
        def __init__(self,nombre,edad):
            self.nombre = nombre
            self.edad = edad
        
        def crearcontraseña(self):
            dec = input("(desea crear una contraseña?: \n A. Si\n B. NO \n Responda la letra de su opcion: ")
            if (dec=="A" or dec=="a"):
                cont = input("Introduzca la contraseña que desea crear: ")
                Contraseña(cont)
                Contraseña.validar(cont)
                self.cont =cont
            else:
                print("Muchas Gracias por participar")
            return self.cont 
        def visualizar(self):
            print(f"{self.nombre} de {self.edad} años de edad,su contraseña es {self.cont}")
    nombre  = input("Por favor ingrese su nombre: ")
    edd = input(" Cual es su edad en años?: ")
    persona1 = Persona(nombre,edd)  
    persona1.crearcontraseña()         
    persona1.visualizar()
def main():
    actividad()
    

if __name__ == "__main__":
    main()

        





















    #def calcularIMC(self,peso,altura):
     #   IMC = peso/altura
      #  print(f"Su indice de masa corporal,de acuerdo a su peso y altura es: {IMC}")
    