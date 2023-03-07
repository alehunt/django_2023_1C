#Cadenas de caracteres (ejemplos de la presentación)

cad_1= "Lunes"
cad2= 'Martes'
marca="Alfa Romeo"
frase= 'Dijo "me encanta programar" y comenzó a' \
    "estudiar ingeniería en sistemas"
print(marca)
print(frase)

nombre= input("Ingrese su nombre: ")
saludo= "Hola "+ nombre
print(saludo) #Hola Pedro

edad= 25
mensaje= "La edad es: "+ str(edad) # La edad es: 25
altura= 1.75
mensaje= "La altura es: "+ str(altura) # La altura es: 1.75

risa='ja'
carcajada= risa*5
print(carcajada) #jajajajaja
asteriscos= "*"*10
print(asteriscos) #**********

pais= input("Ingrese su pais de nacimiento: ")
if pais == "Argentina":
    print("La nacionalidad es Argentino")
else:
    print("La nacionalidad NO es Argentino")

cad="Martes"
print(cad[2])

cad="Miércoles"
print(cad[1:5])

cad="Miércoles"
print(len(cad))

cad="Jueves"
if "ve" in cad:
    print("se encuentra en la cadena")
else:
    print("no se encuentra en la cadena")

if "iércol" in cad:
    print("se encuentra en la cadena")
else:
    print("no se encuentra en la cadena")

cad="Aprendé Python"
for letra in cad:
    print(letra)

cad="Python"
print(max(cad)) #y
print(min(cad)) #P

cad="Programación"
print(cad.count("a")) #2
print(cad.index("grama")) #3

cad="12345"
cad='-'.join(cad)
print(cad) #1-2-3-4-5

cad="Programando en Python"
lista= cad.split(' ')
print(lista) #['Programando', 'en', 'Python']

cad="Hoy es un día frío. Qué frío está!"
cad=cad.replace('frío', 'húmedo')
print(cad) # Hoy es un día húmedo. Qué húmedo está!

cad="Python"
cad2="Python3"
print(cad.isalpha()) # True
print(cad2.isalpha()) # False

cad="1234"
cad2="1234a"
print(cad.isdigit()) # True
print(cad2.isdigit()) # False

cad="Python"
cad2="python"
print(cad.isupper()) # False
print(cad2.islower()) # True
print(cad2.upper()) # PYTHON
print(cad.lower()) # python

cad="Aprendiendo programación en Python"
print(cad.capitalize()) # Aprendiendo programación en python
print(cad.title()) # Aprendiendo Programación En Python

cad1="Hola"
cad2=cad1.center(10,"*")
print(cad2) # ***Hola***

cad1="Hola"
cad2=cad1.ljust(10, '-')
cad3=cad1.rjust(10, '-')
print(cad2) # Hola------
print(cad3) # ------Hola

n=3
cad= str(n).zfill(5)
print(cad) # 00003

cad="---Hola-Mundo----"
cad2="---Hola-Mundo----"
cad= cad.lstrip("-")
print(cad) #Hola-Mundo----
cad2= cad2.rstrip("-")
print(cad2) #---Hola-Mundo

cad="---Hola-Mundo----"
cad= cad.strip("-")
print(cad) #Hola-Mundo

cad="---Hola-Mundo----"
pos= cad.find("Mundo")
print(pos) #8
cad="---Hola-Mundo--Mundo--"
pos= cad.rfind("Mundo")
print(pos) #15 (última aparición de Mundo)

legajo= 12212
nombre= "María"
nota= 10
#%-formato
print("Legajo: %d Nombre: %s Nota: %d" %(legajo,nombre,nota)) 
print("Legajo: {} Nombre: {} Nota: {}".format(legajo,nombre,nota)) 
# En ambos casos devuelve:
# Legajo: 12212 Nombre: María Nota: 10
#f-string
print(f"Legajo: {legajo} Nombre: {nombre} Nota: {nota}")