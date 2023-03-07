VALOR_DOLAR = 200

a=2+3 #una lìnea
print(a)
a= 2 + 3 + 4 + 5 \
    + 6 + 7 + 8 + \
    9 # sentencia dividida en lìneas
print(a) 

c= [2, 3, 4, 
    5, 6, 7, 8, 
        9, 10] # continuaciòn de lìnea implìcita
print (c) 


def sumar(numero_1, numero_2):
    """
    Suma dos numeros para calcular la sarasa
    """
    resultado = numero_1 + numero_2
    if resultado > 0:
        resultado = resultado * 2
    


