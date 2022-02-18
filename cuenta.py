# Crear la clase cuenta

class Cuenta:
    titular = ""
    saldo = 0
    descubierto_permitido = 0

    def __init__(self, titular, saldo_inicial, descubierto_permitido_inical):
        self.titular = titular
        self.saldo = saldo_inicial
        self.descubierto_permitido = descubierto_permitido_inical   

    def retirar(self, cantidad_solicitada):
        if cantidad_solicitada <= (self.saldo + self.descubierto_permitido):
            # Operación permitida
            self.saldo = self.saldo - cantidad_solicitada
            return True
        
        # Operación denegada
        return False
    
    def ingresar(self, cantidad_ingresar):
        self.saldo = self.saldo + cantidad_ingresar

        return True
