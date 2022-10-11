class CuentaBancaria:
# ¡No olvides agregar algunos valores predeterminados para estos parámetros!

    todas_las_cuentas = []
#Constructor o inicializador 
    def __init__(self, numero_cuenta, tasa_interes, balance): 
        self.numero_cuenta = numero_cuenta
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)



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



