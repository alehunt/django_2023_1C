# %% [markdown]
# # Clase completa llamandoa  la otra
# ## Retroceder Nunca, Rendirse Jamas..
# **La clase**
# --------------------------------------------------------------------
# -- Import --#
# --------------------------------------------------------------------
from Persona import Persona
# --------------------------------------------------------------------
# -- Fin import --#
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# -- clase cuenta - Definicion de la clase --#
# --------------------------------------------------------------------
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    # --------------------------------------------------------------------
    # -- Getters & Setters --#
    # --------------------------------------------------------------------
    # titular
    @property
    #getter
    def titular(self):
        return self._titular
    
    @titular.setter
    #setter
    def titular(self, titular):
        if isinstance(titular, Persona):
            self._titular = titular
        else:
            raise NameError("Es posible que la instancia no existe o la haya escrito mal")
    # def set_titular(self, titular):
    #     self.titular = titular
    # def get_titular(self):
    #     return self.titular
    #--------------------------------------------------------------------
    # Cantidad
    @property
    #getter
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    #setter
    def cantidad(self,cantidad):
        if isinstance(cantidad,float):
            self._cantidad = cantidad
        else:
            raise ValueError("No es un dato valido")
    # def set_cantidad(self, cantidad):
    #     self.cantidad = cantidad
    # def get_cantidad(self):
    #     return self.cantidad
    # --------------------------------------------------------------------
    # -- Fin Getters & Setters --#
    # --------------------------------------------------------------------
    
    # --------------------------------------------------------------------
    # -- Metodos normales --#
    # --------------------------------------------------------------------
    def mostrar(self):
        print("Titular: ", self.titular)
        print("Cantidad: ", self.cantidad)
    #--------------------------------------------------------------------
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    #--------------------------------------------------------------------
    def retirar(self, cantidad):
        self.cantidad -= cantidad
    # --------------------------------------------------------------------
    # -- Fin Metodos normales --#
    # --------------------------------------------------------------------
# --------------------------------------------------------------------
# -- clase cuenta - Definicion de la clase --#
# --------------------------------------------------------------------
#--------------------------------------------------------------------
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""
# %%
#persona1 = Persona("Eusebio", 28, "65613548")
#--------------------------------------------------------------------
# %%
# 
#print(persona1)
#--------------------------------------------------------------------
# %%
# 
#cuenta1 = Cuenta(persona1,400000.12)
#--------------------------------------------------------------------
# %%
# 
#print(cuenta1)
#--------------------------------------------------------------------
# %%
# 
#cuenta1.mostrar()
