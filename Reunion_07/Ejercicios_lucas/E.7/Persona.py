
# --------------------------------------------------------------------
# -- Definicion de la clase --#
# --------------------------------------------------------------------
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # --------------------------------------------------------------------
    # -- Getters & Setters --#
    # --------------------------------------------------------------------
    @property
    #getter
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    #setter
    def nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre.strip()
        else:
            raise ValueError("Cadena vacia")
    
    @property
    #getter
    def edad(self):
        return self._edad
    
    @edad.setter
    #setter
    def edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("Valor erroneo")
    
    @property
    #getter
    def dni(self):
        return self._dni
    
    @dni.setter
    #setter
    def dni(self, dni):
        if isinstance(dni, str) and dni.strip():
            self._dni = dni.strip()
        else:
            raise ValueError("No se puede ingresar un valor nulo")
    # --------------------------------------------------------------------
    # -- Fin de Getters & Setters --#
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    # -- Metodos pedidos --#
    # --------------------------------------------------------------------
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    # --------------------------------------------------------------------
    # -- Fin de metodos pedidos --#
    # --------------------------------------------------------------------
    
    # --------------------------------------------------------------------
    # -- Metodos especiales --#
    # --------------------------------------------------------------------
    # Metodo Especial para imprimir
    def __str__(self):
        return f'({self.nombre} , {self.edad} , {self.dni})'
    # Metodo Especial para imprimir mas para programadores

    def __repr__(self):
        return f'Persona({self.nombre} , {self.edad} , {self.dni})'
    # --------------------------------------------------------------------
    # -- Fin de metodos especiales --#
    # --------------------------------------------------------------------
