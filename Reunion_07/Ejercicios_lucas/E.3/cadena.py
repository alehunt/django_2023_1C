"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 16/03/2023 Retroceder nunca, rendirse jamas

Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
# %%
# Funciones ---------------------------------------------------------------------------------------------------
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
    print(contar_palabras(input("Ingrese la cadena: ")))
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()