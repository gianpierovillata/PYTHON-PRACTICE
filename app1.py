

# variables
a = 10
b = 20
nombre = "Juan"
apellido = "Perez"
activo = True


# imprimir variables
print("a", a)
print("b",b)
print("nombre",nombre)
print("apellido",apellido)

# operadores aritmeticos
suma = a + b
resta = a - b
multiplicacion = a*b
division = a/b
print("Suma:", suma)
print("Resta", resta)

#condicionales
if a > b:
    print("A es mayor que B")
else:
    print("B es mayor que A")

if activo == True:
    print("El usuario esta activo")
else:
    print("El usuario no esta activo")

#estructuras de control
for i in range(1, 10):
    #codigo 
    print(i+" : "+a)
    

while activo == True:
    print("El usuario"+nombre+"esta activo")
    activo=False




          

