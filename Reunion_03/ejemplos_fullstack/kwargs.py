def concatenar(**kwargs):
    result = ""
    # print(kwargs.values())
    # print(kwargs.keys())
    # print(kwargs.items())

    # Iteramos sobre los valores del diccionario
    for arg in kwargs.values():
        result += arg
    return result


# diccionario = { "clave1": 1, "clave2": 2, "clave3": 3}

# for clave, valor in diccionario.items():
#     print(clave + valor)

concatenar(primer="Hola", otraclave="Que onda")

print(concatenar(a="Codo!"))
print(concatenar(a="Codo ", b="A ", c="Codo", e="!"))


