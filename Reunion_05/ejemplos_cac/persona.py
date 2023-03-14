from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self,nombre,apellido,dni,email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__email = email

    #el decorator property manejo un metodo como una propiedad. Agrega el encapsulamiento
    #para atributo privados
    @property
    def nombre(self):
        return self.__nombre
    
    #Asociamos el getter con su setter Nombre_funcion.setter para indicar que la funcion 
    #sera un setter y en este caso modificar el valor de la propiedad
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def nombre(self,nuevo_apellido):
        self.__apellido = nuevo_apellido
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,nuevo_dni):
        self.__dni = nuevo_dni

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,nuevo_email):
        self.__email = nuevo_email

    @property
    def nombre_completo(self):
        return f'{self.__apellido}, {self.__nombre}'
    
    @abstractmethod
    def establecer_ocupacion():
        pass
    

class Estudiante(Persona):

    def __init__(self, nombre, apellido, dni, email,matricula):
        super().__init__(nombre, apellido, dni, email)
        self.__matricula = matricula
        self.__baja = 0

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,nuevo_matricula):
        self.__matricula = nuevo_matricula
    
    @property
    def baja(self):
        return self.__baja
    
    def establecer_ocupacion(self):
        return f'{self.nombre_completo} es un estudiante'
    
    def soft_delete(self):
        self.__baja = 1

class Docente(Persona):

    def __init__(self, nombre, apellido, dni, email,legajo):
        super().__init__(nombre, apellido, dni, email)
        self.__legajo = legajo

    @property
    def legajo(self):
        return self.__legajo
    
    @legajo.setter
    def legajo(self,nuevo_legajo):
        self.__legajo = nuevo_legajo
    
    def establecer_ocupacion(self):
        return f'{self.nombre_completo} es un docente'
    
# ERROR INSTANCIAR CLASE ABSTRACTA
# persona_uno = Persona('Mario','Gomez',23444111,'mario@gomez.com')
# print(persona_uno.nombre_completo)

# docente = Docente('Mario','Gomez',23444111,'mario@gomez.com','DT-23344')
# print(docente.nombre_completo)