#global nonlocal

#Global Scope
x = 0
def funcion():
    #Enclosed scope
    # global x 
    x = 1

    def funcion_interna():
        #Local scope
        # nonlocal x
        x= 2
        print(f"Local scope x={x}")

    funcion_interna()
    print(f"Enclosed scope x={x}")

funcion()
print(f"Global scope x={x}")