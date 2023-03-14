from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property
    @abstractmethod
    def salario(self):
        pass


class EmpleadoFullTime(Empleado):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor_nuevo):
        if valor_nuevo > 1000:
            self.__salario = valor_nuevo
        else:
            self.__salario = 1000

    def __repr__(self):
        return self.nombre_completo

    def __str__(self):
        return f"{self.__nombre}"


class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, apellido, horas_trabajadas, valor_hora):
        super().__init__(nombre, apellido)
        self.__horas_trabajadas = horas_trabajadas
        self.__valor_hora = valor_hora

    @property
    def salario(self):
        return self.__horas_trabajadas * self.__valor_hora

    def __repr__(self) -> str:
        return self.nombre_completo


class EmpleadoPasante(Empleado):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)

    # Si no le defino la propiedad abstracta no puedo instanciar un EmpleadoPasante
    @property
    def salario(self):
        return 0


class Nomina:
    def __init__(self):
        self.__lista_empleados = []

    def agregar_empleado(self, empleado):
        self.__lista_empleados.append(empleado)

    def print(self):
        for empleado in self.__lista_empleados:
            if isinstance(empleado, Empleado):
                print(f"{empleado.nombre_completo} \t ${empleado.salario}")
                # ROMPE ENCAPSULAMIENTO print(f"{empleado._Empleado__nombre} \t ${empleado.salario}")
            else:
                print(f"En la nómina hay un no empleado: {empleado}")


nomina_empleados = Nomina()

# pratto = EmpleadoFullTime('Lucas', 'Pratto', 6000)
# nomina_empleados.agregar_empleado(pratto)
nomina_empleados.agregar_empleado(EmpleadoFullTime('Lucas', 'Pratto', 6000))
nomina_empleados.agregar_empleado(EmpleadoFullTime('Lucas', 'Janson', 6500))
nomina_empleados.agregar_empleado(
    EmpleadoPorHora('Valentin', 'Gomez', 200, 50))
nomina_empleados.agregar_empleado(EmpleadoPorHora('Walter', 'Bou', 150, 100))
# nomina_empleados.agregar_empleado(5)
nomina_empleados.agregar_empleado(
    EmpleadoPorHora('Santi', 'Caseres', 100, 150))
# Un empleado no se puede instanciar porque es una clase abstracta
# nomina_empleados.agregar_empleado(Empleado('Diego', 'Armando', 10))
# Si tiene la implementación de salario si se puede instanciar, sino no.
nomina_empleados.agregar_empleado(EmpleadoPasante('Diego', 'Godin'))

nomina_empleados.print()


# Herencia múltiple
class Estudiante():
    def __init__(self, legajo):
        self.__legajo = legajo

    @property
    def legajo(self):
        return self.__legajo

    def __str__(self):
        return f"Legajo: {self.__legajo}"


class EstudiantePasante(Empleado, Estudiante):
    def __init__(self, nombre, apellido, legajo):
        Empleado.__init__(self, nombre, apellido)
        Estudiante.__init__(self, legajo)

    # Tengo que implementar la propiedad salario porque hereda de empleado
    @property
    def salario(self):
        return 0

    def __str__(self):
        return f"{self.nombre_completo}. Legajo: {self.legajo}"


mis_estudiantes = []
mis_estudiantes.append(Estudiante(999))
mis_estudiantes.append(5)
mis_estudiantes.append(EstudiantePasante("Fabian", "Cubero", 5))


for estudiante in mis_estudiantes:
    if isinstance(estudiante, Estudiante):
        print(estudiante)
    else:
        print(f"El valor {estudiante} no es un estudiante")
