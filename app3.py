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
    
    def  __init__(self,nombre, apellido, edad, sexo,altura, peso,fecha_nac):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.sexo=sexo
        self.altura =altura
        self.peso=peso
        self.fecha_nac=self.fecha_nac

    def imprimir_datos(self): 
        print("--------------------DATOS DE LA PERSONA ---------------------------")
        print("Nombre",self.nombre)
        print("Apellido",self.apellido)
        print("Edad",self.edad)
        print("Sexo",self.sexo)
        print("--------------------------------------------------------------------")



nombre =str(input("Ingrese su nombre:"))
apellido=str(input("Ingrese su apellido:"))
edad=int(input("Ingrese su edad:"))
sexo=str(input("Ingrese el sexo (M-F):"))
altura=float(input("Ingrese la altura en metros:"))
peso=float(input("Ingrese el peso:"))
fecha_nac =date(input("Ingrese la fecha de nacimiento"))

persona =Persona(nombre,apellido,edad,sexo,altura,peso,fecha_nac)
persona.imprimir_datos(persona)

            