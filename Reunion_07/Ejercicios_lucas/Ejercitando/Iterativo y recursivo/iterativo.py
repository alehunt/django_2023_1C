# %% [markdown]
# # Decremental
# ## Retroceder Nunca, Rendirse Jamas..
# **Hola como estas**
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# Ejemplo de uso
print(factorial(5)) # Salida: 120

#--------------------------------------------------------------------
# %% [markdown]
# # Decremental
# ## Retroceder Nunca, Rendirse Jamas..
# **Hola como estas**
def factorial(n):
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
    return resultado

# Ejemplo de uso
print(factorial(5)) # Salida: 120