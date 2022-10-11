#Imprime todos los números enteros del 0 al 150.

for numeros in range (0, 151):
    print(numeros)

#Imprime todos los múltiplos de 5 entre 5 y 1,000.    
for multiplos in range (0, 1001, 5):
    print(multiplos)

#Imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".    

for divisibles in range (1, 101):

    if (divisibles % 10 == 0):
        print("Coding Dojo") 

    elif (divisibles % 5 == 0):
        print("Coding")

    else:
        print (divisibles)    




#Agrega los enteros impares del 0 al 500,000, e imprime la suma final.
suma_impares = 0

for impares in range (0, 500000):
    if (impares % 2!=0):
        suma_impares = suma_impares + impares
print(suma_impares)



#Imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.

for num_positivos in range (2018,0,-4):
    print(num_positivos)


#Establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprime solo los enteros que sean múltiplos de mult. 
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

lowNum = 12
highNum = 23
mult = 3

for contadorFlexibe in range (lowNum, highNum+1):
    if contadorFlexibe % mult==0:
        print(contadorFlexibe)




