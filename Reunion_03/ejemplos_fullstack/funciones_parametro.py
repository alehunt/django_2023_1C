# def sumar(primer_numero, segundo_numero):
#     return primer_numero + segundo_numero
def sumar(primer_numero, segundo_numero, tercer_numero=0):
    """
    Suma tres numeros
    primer_numero: primer parametro
    """
    return primer_numero + segundo_numero + tercer_numero


sumar(1,2)
sumar(primer_numero=1,segudo_numero=2, tercer_numero=3)



def saludar_espanol():  
    print("Hola")

def saludar_ingles():  
    print("Hello")

saludadores = {
    'es': saludar_espanol,  
    'en': saludar_ingles
}

saludadores['es']()
saludadores['en']()


