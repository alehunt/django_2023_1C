# Estructuras condicionales
# Condicional Simple
'''
Ingresar el sueldo de una persona, si supera los 3000 dólares mostrar un mensaje
en pantalla indicando que debe abonar impuestos.
'''

sueldo=float(input("Ingrese cual es su sueldo:"))
if sueldo>3000: #Preguntasmo si el sueldo es mayor a 3000
    print("Esta persona debe abonar impuestos")
print("Fin del programa")

# Condicional Doble o Compuesto
'''
Realizar un programa que solicite ingresar dos números distintos y muestre
por pantalla el mayor de ellos.
'''

num1=int(input("Ingrese el primer valor:"))
num2=int(input("Ingrese el segundo valor:"))
if num1>num2: 
    # Bloque de verdad
    print("num1 es mayor")
    # print("El valor mayor es", num1)
else:
    # Bloque de falsedad
    print("num2 es mayor")
    # print("El valor mayor es", num2)
print("Fin del programa")

# Condicionales anidados (if - if-else - else)
'''
Realizar un programa que solicite ingresar dos números distintos y muestre
por pantalla el mayor de ellos. Si NO son distintos mostra un mensaje de error.
'''
num1=int(input("Ingrese el primer valor:"))
num2=int(input("Ingrese el segundo valor:"))
if num1!=num2: 
    if num1>num2: 
        # Bloque de verdad
        print("num1 es mayor")
        # print("El valor mayor es", num1)
    else:
        # Bloque de falsedad
        print("num2 es mayor")
        # print("El valor mayor es", num2)
else:
    print("Error! los números son iguales.")
print("Fin del programa")

# Condicionales anidados (if-else-if-else)
'''
Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el 
promedio e imprima alguno de estos mensajes:
    Si el promedio es >=7 mostrar "Promocionado".
    Si el promedio es >=4 y <7 mostrar "Regular".
    Si el promedio es <4 mostrar "Reprobado".
'''
nota1= int(input("Ingrese nota 1: "))
nota2= int(input("Ingrese nota 2: "))
nota3= int(input("Ingrese nota 3: "))
promedio= (nota1+nota2+nota3)/3

print("El promedio es:", promedio)

if promedio >= 7:
    print("Promocionado")
else:
    if promedio >= 4 and promedio < 7: #Es equivalente: 4 <= promedio < 7
        print("Regular")
    else:
        print("Reprobado")

# Condicionales mùltiple (elif, que reemplaza la combinaciòn de else-if)
nota1= int(input("Ingrese nota 1: "))
nota2= int(input("Ingrese nota 2: "))
nota3= int(input("Ingrese nota 3: "))
promedio= (nota1+nota2+nota3)/3

print("El promedio es:", promedio)

if promedio >= 7:
    print("Promocionado")
elif promedio >= 4 and promedio < 7:
    print("Regular")
else:
    print("Reprobado")
#Esta estructura es equivalente a la anterior

'''
Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el 
promedio e imprima alguno de estos mensajes:
    Si el promedio es >=7 mostrar "Promocionado".
    Si el promedio es >=4 y <7 mostrar "Regular".
    Si el promedio es <4 mostrar "Reprobado".
    Extra: Si el promedio es entre 3 y 4: "Recupera".
'''

nota1= int(input("Ingrese nota 1: "))
nota2= int(input("Ingrese nota 2: "))
nota3= int(input("Ingrese nota 3: "))
promedio= (nota1+nota2+nota3)/3

print("El promedio es:", promedio)

if promedio >= 7:
    print("Promocionado")
elif promedio >= 4 and promedio < 7:
    print("Regular")
elif promedio >= 3 and promedio < 4:
    print("Recupera")
else: #Entra aquí si no cumple ninguna de las condiciones anteriores
    print("Reprobado")