class CuentaBancaria:
# ¡No olvides agregar algunos valores predeterminados para estos parámetros!


#Constructor o inicializador 
    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes
        self.balance = balance
# tu código aquí (recuerda, los atributos de instancia van aquí)
# no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario

    def deposito(self, cantidad):
        self.balance += cantidad
        return self


    def retiro(self, cantidad):
        if self.balance < cantidad:
            self.balance -= 5
            print("Fondos insuficientes, te restaremos 5")
        else:
            self.balance -= cantidad
        return self

    def mostrar_info_cuenta(self):
        print("Balance actual: ", self.balance)
        return self


    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.tasa_interes)
        return self



