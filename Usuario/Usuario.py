from CuentaBancaria import CuentaBancaria

class Usuario:

#Constructor o inicializador 
    def __init__(self, nombre, correo, numero_cuenta):
        self.nombre = nombre 
        self.correo = correo
        self.mis_cuentas = []
        self.cuenta = CuentaBancaria(numero_cuenta,tasa_interes=0.15, balance=0)
        self.mis_cuentas.append(self.cuenta)


    def abrir_nueva_cuenta(self, numero_cuenta):
        nueva_cuenta = CuentaBancaria(numero_cuenta,tasa_interes=0.15, balance=0)
        self.mis_cuentas.append(nueva_cuenta)
        return self 

    def mostrar_info_cuentas_usuario(self):
        for cuenta in self.mis_cuentas:
            print(f"La cuenta # {cuenta.numero_cuenta} del cliente {self.nombre} tiene un balance de {cuenta.balance}") 
        return self   

    def hacer_deposito(self, monto):
        self.cuenta.deposito(monto) 
        return self


    def hacer_retiro(self, monto):
        self.balance_cuenta -= monto
        return self

    def mostrar_balance_usuario(self):
        self.cuenta.mostrar_info_cuenta()
        #print(f"{self.nombre} tiene actualmente en su cuenta $ {self.balance_cuenta}")
        return self

    def transfer_dinero(self, otro_usuario, cantidad):
        self.hacer_retiro(cantidad)
        otro_usuario.hacer_deposito(cantidad)
        return self