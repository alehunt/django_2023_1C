# #Condicionales (ejemplos de la presentación)

# # EJERCICIO: Ingresar un número y determinar si es menor que 10.
# from urllib.request import CacheFTPHandler


# a=float(input("Ingrese un número:"))
# if a < 10:
#     print("El número ingresado es menor que 10")




# # EJERCICIO: Ingresar un número distinto de cero y decir si es par o impar.
# b=int(input("Ingrese un número:"))
# if b % 2 == 0:
#     print(b, "es par")
# else:
#     print(b, "es impar")

# # EJERCICIO: Ingresar un número entero e imprimir un mensaje indicando si es cero, par o impar.
# c=int(input("Ingrese un número:"))
# if c == 0:
#     print("El número ingresado es cero.")
# else:
#     if c % 2 == 0:
#         print("El número", c, "es par.")
#     else:
#         print("El número", c, "es impar.")

# EJERCICIO: Leer un número entero e imprimir un mensaje indicando si es cero, uno, dos o cualquier otro número.
d=int(input("Ingrese un número:"))
if d == 0:
    print("El número ingresado es 0 (cero).")
elif d == 1:
    print("El número ingresado es 1 (uno).")
elif d == 2:
    print("El número ingresado es 2 (dos).")
else:
    print("El número no es 0, 1 ni 2. Es otro número.")

# EJERCICIO: Realizar un programa que permita ingresar un número y decir si tiene de dos cifras o no.
e=int(input("Ingrese un número:"))
if e >=10 and e <= 100:
    print("El número ingresado es de dos cifras")
else:
    print("El número ingresado no tiene dos cifras")

   #Se puede abreviar usando la siguiente notación:
    if 10 <= e <= 100:
        print("El número ingresado es de dos cifras")
    else:
        print("El número ingresado no tiene dos cifras")


# EJERCICIO: Ingresar dos números enteros y decir si alguno es divisible por el otro.
num1=int(input("Ingrese un número:"))
num2=int(input("Ingrese otro número:"))
if num1 % num2 == 0 or num2 % num1 == 0:
    print("Uno de los números es divisible por el otro")
else:
    print("Ninguno de los números es divisor del otro")