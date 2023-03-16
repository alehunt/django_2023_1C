class DivisorNegativoError(Exception):
    """Excepción lanzada se divide por números negativos"""
    def __init__(self, p_divisor, message="Enviaron un divisor negativo"):
        self.divisor = p_divisor
        self.message = message
        super().__init__(self.message)


class CalculoComplejoError(Exception):
    """Excepción del calculo complejo"""
