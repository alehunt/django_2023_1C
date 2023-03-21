"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 16/03/2023 Retroceder nunca, rendirse jamas

Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.


------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
# %%
# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def clave_con_max_valor(diccionario):
    max_valor = max(diccionario.values())
    for clave, valor in diccionario.items():
        if valor == max_valor:
            return clave, max_valor
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def contar_palabras(cadena):
#Contrato:
# Precondicion:
# Poscondicion:
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    print(clave_con_max_valor(contar_palabras(input("Ingrese la cadena: "))))
# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()