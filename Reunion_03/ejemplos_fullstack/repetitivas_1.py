#Repetitivas (ejemplos de la presentación)

#While 
#EJERCICIO: Leer números y mostrarlos hasta que se ingrese un número negativo (ciclo condicional).
num1 = int(input("Ingrese un número: "))
while num1 > 0:
    print(num1)
    num1 = int(input("Ingrese un número: "))
print("Fin del ejercicio")

#EJERCICIO: Desarrollar un programa que cuente hasta 4, utilizando una sola variable para contar (ciclo exacto).
cont= 1 #Inicializamos la variable
while cont <= 4:
    print(cont)
    cont = cont + 1     # Incrementamos la variable en 1
                        # Siempre debemos modificar la variable
                        # que determinará nuestra Condición
                        # Sino, se genera un CICLO INFINITO!
print("Fin del ejercicio")

#EJERCICIO: Ingresar números enteros y sumar solamente los números positivos, el programa finalizará ingresando 0 (cero) (ciclo condicional).
suma= 0
nro= int(input("Ingrese un número (cero para finalizar): "))
while nro != 0:
    if nro > 0:
        suma += nro
    nro= int(input("Ingrese otro número (cero para finalizar): "))
print("FIN! Ingresó cero. La suma de los valores ingresados es:", suma)

#EJERCICIO: Ingresar 5 valores por teclado, obtener su suma y su promedio.
cont= 1
suma= 0
while cont <= 5:
    num= int(input("Ingrese un número: "))
    suma = suma + num   # Acumulamos, es equivalente suma += num 
    cont = cont + 1     # Incrementamos, es equivalente cont += 1

print("La suma es:", suma)
print("El promedio es:", suma/cont)

#For
# EJERCICIO: Mostrar los números del 1 al 10.
for i in range(1,10,1): #No incluye al 10 (se puede poner 10+1)
    print(i)

# EJERCICIO: Mostrar los múltiplos de 5 comprendidos entre 12 y 80.
for i in range(12,81,5):
    print(i)

# EJERCICIO: Imprimir los números del 9 al 1.
for i in range(9,0,-1): #En este caso, como el valor inicial es mayor al valor final, el paso debe ser necesariamente un número negativo.
    print(i)

# EJERCICIO: Mostrar los números del 10 al 20
for i in range(10,21):
    print(i)

# EJERCICIO: Ingresar cinco números y mostrar su suma
suma= 0
for i in range(5):
    a = int(input("Ingrese un número: "))
    suma += a
print("La suma es:", suma)