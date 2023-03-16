from exceptions import DivisorNegativoError, CalculoComplejoError


def mostrar_division_entera(dividendo, divisor):
    try:
        # assert divisor >= 0, "Mandaron un número negativo"
        # El assert valida lo mismo que el raise de la excepción personalizada pero lanza AssertionError
        if divisor < 0:
            raise DivisorNegativoError(divisor, "Mandaron un número negativo")
            #     raise DivisorNegativoError(divisor)
        print("Intentando hacer la división")
        resultado = dividendo // divisor
        print(f"El resultado entero de la divisón es: {resultado}")
    except TypeError:
        print('Revisar los operandos hay un dato mal cargado...')
    except ZeroDivisionError as zde:
        print(f'No se puede dividir por cero... {zde}')
        raise zde
    except Exception as ex:
        print(f'Algo anduvo mal: {ex}')
        raise
    else:
        print("Este programa nunca falla..")
    finally:
        print('El super programa ha finalizado..')


def calculo_complejo():
    try:
        mostrar_division_entera(3, 0)
    except ZeroDivisionError as zde:
        print("Dividió por cero")
        raise CalculoComplejoError from zde


def super_calculo():
    try:
        calculo_complejo()
    except CalculoComplejoError as cce:
        print(cce)


def funcion_prueba():
    try:
        otra_funcion()
    except DivisorNegativoError as dne:
        print(dne)


def otra_funcion():
    mostrar_division_entera(2, -1)


# mostrar_division_entera(2, -1)
# mostrar_division_entera(2, 0)
# funcion_prueba()
# mostrar_division_entera("1", "2")
# mostrar_division_entera(1, 2)
super_calculo()
