#funciones
""" def suma(a,b):
    return a+b
 """
def calculo_pagar(cuotas,precio_cuotas):
    if cuotas>=0:
        total_pagar = float(cuotas*precio_cuotas)
        return total_pagar
    else:
        return 0.0
    

def imprmir_datos(nombre,dni,edad,telefono):
    cuotas =int(input("Numero de cuotas:"))
    precio_cuotas =float(input("Precio de cada cuota:"))
    total_pagar =calculo_pagar(cuotas,precio_cuotas)
    print("----------------Formulario de datos ----------------")
    print("Nombre: ",nombre)
    print("DNI: ",dni)
    print("Edad: ",edad)
    print("Telefono:",telefono)
    if edad>18:
        print("Mayor de edad")
    print("-----------------------------------------------------")
    print("-----------------COUTAS---------------------------")
    print("Cuotas: ", cuotas)
    print("Precio de cuotas", precio_cuotas)
    print("Total a pagar:" ,total_pagar)
    print("---------------------------------------------------")


""" suma=suma(10,20)
print("El valor de la suma es:",suma) """

nombre=str(input("Ingrese su Nombre:"))
dni=int(input("Ingrese su DNI: "))
edad=int(input("Ingrese su Edad: "))
telefono=int(input("Ingrese su Telefono:"))

imprmir_datos(nombre,dni,edad,telefono)