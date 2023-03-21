#--------------------------------------------------------------------
# %%
# 
# --------------------------------------------------------------------
# -- Definicion de una clase --#
# --------------------------------------------------------------------
class Persona:
    def __init__(self, nombre ="", edad=0 ,dni =0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
# --------------------------------------------------------------------
# -- Definicion de una clase --#
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# -- Gettes & Setters --#
# --------------------------------------------------------------------
@property #Getter
def nombre(self):
    return self._nombre

@nombre.setter #Setter
def nombre(self , nombre):
    if isinstance(nombre, str) and nombre.strip():
        self._nombre= nombre.strip()
    else:
        raise ValueError("Cadena vacio o valor distinto a un string")
    
@property #Getter
def edad(self):
    return self._edad

@edad.setter #Setter
def edad(self , edad):
    if isinstance(edad, int) and edad >= 0:
        self._edad = edad
    else:
        raise ValueError("Valor nulo o diferente a un entero")
    
@property #Getter
def dni(self):
    return self._dni

@dni.setter #Setter
def dni(self , dni):
    if isinstance(dni, str) and dni.strip():
        self._dni = dni.strip()
    else:
        raise ValueError("cadena vacia o valor distinto a un string")
# --------------------------------------------------------------------
# -- Gettes & Setters --#
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# -- Metodos especiales --#
# --------------------------------------------------------------------
    def __str__(self):
        return f'({self.nombre} , {self.edad} , {self.dni})'
# Metodo Especial para imprimir mas para programadores
    def __repr__(self):
        return f'Fruta({self.nombre} , {self.edad} , {self.dni})'
# --------------------------------------------------------------------
# -- Metodos especiales --#
# --------------------------------------------------------------------

#--------------------------------------------------------------------
# %%
# 
perso = Persona("Lucas", 40, "29427235")

# %%
print(perso.edad)
# %%
perso.edad = 16
# %%
print(perso.edad)
# %%
