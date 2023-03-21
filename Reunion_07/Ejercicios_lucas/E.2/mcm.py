"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 16/03/2023 Retroceder nunca, rendirse jamas

Escribir una función que calcule el mínimo común múltiplo entre dos números
------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
# %%

# Funciones ---------------------------------------------------------------------------------------------------

## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def mcd(x, y):
#Contrato:
# Precondicion:
# Poscondicion:
    while y != 0:
        x, y = y, x % y
    return x

## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def mcm(a,b):
#Contrato:
# Precondicion:
# Poscondicion:
    return a * b // mcd(a, b)


## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal

    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    print("El valor es: ", mcm(a, b))
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()