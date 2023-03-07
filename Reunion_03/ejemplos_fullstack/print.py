#Print
print("Imprimir en una línea.") #Incluye saltod e línea al final
print("Imprimir y continuar en la misma línea. ", end='') #En vez de poner un salto de línea al final coloco una cadena vacía
print("Esto sigue en la misma línea")
print() #Salto de línea
cadena= "Juan Pablo"
print("Hola",cadena) #La coma le agrega un espacio intermedio
print("Hola"+cadena) #El + no le agrega un espacio intermedio
edad= 35
print("Hola",cadena, "mi edad es", edad) #Podemos agregar más texto
#print("Hola",cadena, "mi edad es"+ edad) #Error, solo podemos concatenar cadenas con enteros
print("Hola",cadena, "mi edad es"+ str(edad)) #Parseamos entero a string
