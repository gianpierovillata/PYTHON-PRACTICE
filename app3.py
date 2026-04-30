from datetime import date
class Persona:
    
    
    #propiedades
    nombre:str
    apllido:str
    edad:int
    sexo:str
    fecha_nac:date
    altura:float
    peso:float


    #metodos 
    
    def  __init__(self,nombre, apellido, edad, sexo,altura, peso):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.sexo=sexo
        self.altura
        self.peso=peso

    def imprimir_datos(self): 
        print("--------------------DATOS DE LA PERSONA ---------------------------")
        print("Nombre",self.nombre)
        print("Apellido",self.apellido)
        print("Edad",self.edad)
        print("Sexo",self.sexo)
        print("")



nombre =str(input("Ingrese su nombre:"))
apellido=str(input("Ingrese su apellido:"))
edad=int(input("Ingrese su edad:"))

            