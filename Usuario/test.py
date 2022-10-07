from CuentaBancaria import CuentaBancaria
from Usuario import Usuario



#cuenta_uno = CuentaBancaria(0.10, 200)
#print("Balance previo al deposito", cuenta_uno.balance)
#cuenta_uno.deposito(300).deposito(100).deposito(100).retiro(550).generar_interes().mostrar_info_cuenta()
#print ("Balance despues del deposito", cuenta_uno.balance)
#cuenta_uno.retiro(700).mostrar_info_cuenta()
#print("Balance actual",cuenta_uno.balance)
#cuenta_uno.generar_interés ().mostrar_info_cuenta()
#print ("Se agrego el siguiente interes", cuenta_uno.balance)

#cuenta_dos = CuentaBancaria(0.15, 150)

#cuenta_dos.deposito(250).deposito(550).retiro(200).retiro(200).retiro(500).retiro(100).generar_interes().mostrar_info_cuenta()


print( "DESDE AQUI COMIENZAN USUARIOS")

Usuario1 = Usuario("Chester", "chester@chico.com", 1)
#print(Usuario1.__dict__)
Usuario1.cuenta.deposito(500).mostrar_info_cuenta()

Usuario1.hacer_deposito(50).mostrar_balance_usuario()

Usuario1.abrir_nueva_cuenta(2).mostrar_info_cuentas_usuario()

