#Listas (ejemplos de la presentación)

from re import sub


lista_vacia = [] #Lista vacía
print (type(lista_vacia))
numeros= [1,2,3,4,5] #Lista de números
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"] #Lista de strings


longitud = len(dias)
ultimo_elemento = dias[len(dias) - 1]
ultimo_elemento = dias[-1]
anteultimo_elemento = dias[2]

del dias[2]
print(dias)

dias.insert(2, "Miercoles")

#slicing
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]
martes_a_jueves = dias[1:4]
finde = dias[5:]
semana = dias[:5]

frutas = ["manzana", "banana", "cereza"]
frutas[1:3] = ["pera", "melon"]
print(frutas)

frutas[0:2] = ["pera", "melon", "ciruela", "durazno"]

lista_primera = [1,2,3]
lista_segunda = [124,5,6]
sublista_1 = [lista_primera,lista_segunda]
sublista_2 =  lista_primera + lista_segunda

lista=[3,4,5,6]
print(4 in lista) #True
print(8 in lista) #False

# Copiado de listas #
cajon_1 = ["manzana", "banana", "cereza"]
print("manzana" in cajon_1)
cajon_2 = cajon_1
cajon_2[1] = "Lechuga"

cajon_3 = cajon_1.copy()
cajon_3[1] = "Tomate"
cajon_4 = list(cajon_1)
cajon_4[1] = "Cerveza"


######### List comprehension  ###########

multiplos_2 = [x * 2 for x in range(10)]
print(multiplos_2)

multiplos_2 = []
for x in range(10):
    multiplos_2.append(x*2)


#without comprehension 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.append("orange")

fruits.insert(0, "orangita")
fruits.remove("orange")
fruits.index("banana")
newlist = []


for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#with comprehension 
newlist = [x for x in fruits if "a" in x]

print(newlist)
######### ------------------ ###########

dias= ["Lunes", "Martes", "Miércoles"]
d1, d2, d3 = dias
print(d1)
print(d2)
print(d3)

lista1= [1,2,3]
lista2= [4,5,6]
lista3= lista1 + lista2
print(lista3) #[1,2,3,4,5,6]

lista_desordenada = [180, 3, 1, 25, 30, 66]
lista_desordenada.sort()
print(lista_desordenada)
lista_desordenada.sort(reverse=True)
print(lista_desordenada)



lista=[3,4,5]
# lista= lista + [6] #[3,4,5,6]
lista[1]=7
print(lista) #[3,7,5]

lista=[3,4,5,6]
print(len(lista)) # 4
print(max(lista)) # 6
print(min(lista)) # 3
print(sum(lista)) # 18

lista= list(range(6))
print(lista) #[0,1,2,3,4,5]
print(lista) #[0,1,2,3,4,5]

lista=[3,4,5,6]
print(4 in lista) #True
print(8 in lista) #False

lista=[3,4,5]
lista.append(6)
print(lista) #[3,4,5,6]

lista=[3,4,5]
lista.insert(0,2) #Agrega en la posición 0 el número 2
print(lista) #[2,3,4,5]
lista.insert(3,25) #Agrega en la posición 3 el número 25
print(lista) #[2,3,4,25,5]

lista=[3,4,5]
dato_en_lista = lista.pop(1) # queda [3,5]

lista=[6,9,8]
lista.pop() # queda [6,9]

lista=[3,4,5]
lista.remove(3) # queda [4,5]

lista=[3,4,5]
print(lista.index(5)) #2

lista=[3,4,5,3,5,8,5]
print(lista.count(5)) #El número 5 está 3 veces
print(lista.count(2)) #El número 2 no está en la lista

for i in range(lista.count(20)):
    lista.remove(20)


lista=[3,4,5]
lista.clear()
print(lista) #[]

lista=[3,4,5]
lista.reverse()
print(lista) #[5,4,3]

lista=[5, 1, 7, 2]
lista.sort()
print(lista) #[1,2,5,7]

lista=[5, 1, 7, 2]
lista.sort(reverse=True)
print(lista) #[7,5,2,1]

#Mostrar la lista, separando los elementos con un espacio
def MostrarLista(param_lista):
    i = 0
    while i < len(param_lista):
        print(param_lista[i], end=" ")
        i = i + 1
    print()

#Declaración de la lista y llamado a la función
lista=["A", "B", "C", "D", "E"]
MostrarLista(lista)

def SumarLista(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma

#Declaración de la lista y llamado a la función
lista=[2,3,4,5,6]
print(SumarLista(lista))

vocales=['a','e','i','o','u']
for vocal in vocales:
    print(vocal, end="-")