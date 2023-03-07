def super_funcion(comida, valor):
    valor = 4 
    comida[1] = "pera"
    for x in comida:
        que_comi = "Me comí un/a %s" % x
        que_comi = "Me comí un/a {comida}".format(comida=x)
        que_comi = f"Me comí un/a {x}"
        print(que_comi)


frutas = ["manzana", "banana", "cereza"]

x=3
super_funcion(frutas, x)
print(x)
print(frutas)
