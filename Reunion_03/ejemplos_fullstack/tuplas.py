# TUPLAS
# Ejemplos de tuplas
()                                              # tupla vacía
'un valor',                                     # tupla con un valor
('uno', 'dos', 'tres')	             	        # cadenas	
('Palotes, Juan de', (1930, 11, 13), 3000936)   # datos de persona
'Palotes, Juan de', (1930, 11, 13), 3000936     # datos de persona

# Creación
tupla  = ('uno', 'dos', 'tres')
# Empaquetado (zip)
tupla  = 'Palotes, Juan de', (1930, 11, 13), 3000936
# Desempaquetado (unpack)
nombre,  nacimiento, dni  =( 'Palotes, Juan de', (1930, 11, 13), 3000936)

tupla = [1, 2, 3], [4, 5, 6]


# Accesos
tupla = ('Palotes, Juan de', (1930, 11, 13), 3000936)
nombre, fecha, dni = tupla
print('Nombre: ', nombre, '. Fecha nac.: ', fecha, '. DNI: ', dni)
print('Nombre: ', tupla[0], '. Fecha nac.: ', tupla[1], '. DNI: ', tupla[2])
print(tupla[::])