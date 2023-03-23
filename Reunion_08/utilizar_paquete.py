from recursos_humanos.nomina import Nomina


nomina_empleados = Nomina()
# pratto = EmpleadoFullTime('Lucas', 'Pratto', 6000)
# nomina_empleados.agregar_empleado(pratto)
nomina_empleados.agregar_empleado(EmpleadoFullTime('Lucas', 'Pratto', 6000))
nomina_empleados.agregar_empleado(EmpleadoFullTime('Lucas', 'Janson', 6500))
nomina_empleados.agregar_empleado(EmpleadoPorHora('Valentin', 'Gomez', 200, 50))
nomina_empleados.agregar_empleado(EmpleadoPorHora('Walter', 'Bou', 150, 100))
nomina_empleados.agregar_empleado(EmpleadoPorHora('Santi', 'Caseres', 100, 150))

nomina_empleados.print()