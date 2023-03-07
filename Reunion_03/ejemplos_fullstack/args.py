

def mi_suma(*args):
    result = 0
    # Itero sobre la tupla
    for x in args:
        result += x
    return result


print(mi_suma(1, 2, 3, 4, 5, 6))

print(mi_suma(1, 2, 3))
print(mi_suma(1))
print(mi_suma(2, 2, 2, 2, 2))