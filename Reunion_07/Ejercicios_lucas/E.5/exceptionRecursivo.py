"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/03/2023 Retroceder nunca, rendirse jamas

Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio por iteracion.

------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
# %%


# Funciones ---------------------------------------------------------------------------------------------------
# Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def get_int():
    # Contrato:
    # Precondicion:
    # Poscondicion:
    try:
        num = int(input("Ingresa un número entero: "))
        return num
    except ValueError:
        print("Error: Debes ingresar un valor entero válido. Intenta de nuevo.")
        return get_int()

# Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
    # El main como programa principal
    num = get_int()
    print("El número ingresado es:", num)
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == "__main__":
    main()
