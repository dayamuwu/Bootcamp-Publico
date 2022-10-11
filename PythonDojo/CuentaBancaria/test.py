from CuentaBancaria import CuentaBancaria

cuenta_uno = CuentaBancaria(0.10, 200)
#print("Balance previo al deposito", cuenta_uno.balance)
cuenta_uno.deposito(300).deposito(100).deposito(100).retiro(550).generar_interes().mostrar_info_cuenta()
#print ("Balance despues del deposito", cuenta_uno.balance)
#cuenta_uno.retiro(700).mostrar_info_cuenta()
#print("Balance actual",cuenta_uno.balance)
#cuenta_uno.generar_interés ().mostrar_info_cuenta()
#print ("Se agrego el siguiente interes", cuenta_uno.balance)

cuenta_dos = CuentaBancaria(0.15, 150)

cuenta_dos.deposito(250).deposito(550).retiro(200).retiro(200).retiro(500).retiro(100).generar_interes().mostrar_info_cuenta()
