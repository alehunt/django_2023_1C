def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Ejemplo de uso
print(factorial(5)) # Salida: 120