'''Tipos de operadores:
- De asignación
- Matemáticos
- Lógicos
- Relacionales
'''
print(0 or 5/0)


#Matemáticos/Aritmèticos
print(12+13) #Suma
print(12-13) #Resta
print(12*13) #Multiplciación
print(12/13) #División con decimales
print(13//5) #División entera
print(13%5) #Resto o módulo de la división entera
resultado= 13%5
print(resultado)
print(2%2) #Par
print(5%2) #Impar
print(5**2) #Potencia (25)
print("Raíz cuadrada de 9:", 9**(1/2)) #Raíz cuadrada (3)
print("Raíz cúbica de 8:", 8**(1/3)) #Raíz cúbica (2)

#Relacionales: > < >= <= == !=
print(8>8) #False
print(8>=8) #True
print(3<3) #False
print(3<=3) #True
print(5==5) #True
print(5!=5) #False
print(not((5+5)>10)) #jerarquía entre operadores: 1° (5+5); 2° (10)>10; 3° not False = True

#Lógicos (AND, OR, NOT)



print(True and False) #AND
print(True or False) #OR
print(not False) #NOT (True)
resultado= not (10>5) #(not True)
print("Resultado:", resultado)

#Asignación
print("+= y -=")
x=5
x+=2
print(x)
x-=2
print(x)
print()

print("*= y /=")
x=10
x*=2
print(x)
x/=4
print(x)
print()

print("%= //= y **=")
x=15
x%=2
print(x)
x=15
x//=6
print(x)
x**=3
print(x)
print()

#Pertenencia
lista= [1, 3, 2, 7, 9, 8, 6]
print(lista)
print(4 in lista) #False
print(3 in lista) #True
print(4 not in lista) #True