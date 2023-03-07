# CONJUNTOS
# Ejemplos de conjuntos
set()			                                # conjunto vacío
{'un valor'}		                            # conjunto con un valor
{'uno', 'dos', 'tres'}                  	    # conjunto de cadenas
{'Palotes, Juan de', (1930, 11, 13), 3000936}   # datos de persona

# Creación
conjunto  = { 1, 9, 0 }

# Accesos
conjunto = {'Palotes, Juan de', (1930, 11, 13), 3000936}
a = set(conjunto)
print(a)
[print (elem) for elem in a]
print(a)