"""------------------------------------------------------------------------------------------------------------
Ing.Lucas F. Quiroga H. Fecha: 17/04/2023 Retroceder nunca, rendirse jamas

Escribir una función que calcule el máximo común divisor entre dos números.

------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
import math
# %%


# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def divisorComunMayor(num1, num2):
#Contrato: Calculo el DCM
# Precondicion: Necesito numeros enteros
# Poscondicion: Devolvere el Divisor comun mayor
    mcd = math.gcd(num1, num2)
    print("El MCD de", num1, "y", num2, "es:", mcd)
    return None

# Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
    # El main como programa principal
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el primer numero: "))
    divisorComunMayor(num1 , num2)
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()
