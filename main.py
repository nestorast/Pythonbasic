#menu = """
#Bienvenido al convertidor de monedas
#1- pesos colombianos
#2- pesos argentinos
#3- pesos mexicanos
#"""
#opcion = int(input (menu))
#if opcion == 1:
#    pesos = input ("cuantos pesos colombianos tienes? ")
#    pesos = float(pesos) ##convierte pesos en una cifra decimal
#    valor_dolar = 3875
#    dolares = pesos/valor_dolar
#    dolares = round (dolares, 2)
#    dolares = str(dolares) ##convierte dolares en texto
#    print("tienes $"+ dolares + " dolares") ##imprime el valor texto de dolares
#elif opcion == 2:
#    pesos = input ("cuantos pesos argentinos tienes? ")
#    pesos = float(pesos) ##convierte pesos en una cifra decimal
#    valor_dolar = 65
#    dolares = pesos/valor_dolar
#    dolares = round (dolares, 2)
#    dolares = str(dolares) ##convierte dolares en texto
#    print("tienes $"+ dolares + " dolares") ##imprime el valor texto de dolares
#elif opcion == 3:
#    pesos = input ("cuantos pesos mexicanos tienes? ")
#    pesos = float(pesos) ##convierte pesos en una cifra decimal
#    valor_dolar = 24
#    dolares = pesos/valor_dolar
#    dolares = round (dolares, 2)
#    dolares = str(dolares) ##convierte dolares en texto
#    print("tienes $"+ dolares + " dolares") ##imprime el valor texto de dolares
#else:
#    print ("ingrese un valor correcto")

##CONDICIONALES

# edad = int(input("escribe tu edad: "))
#if edad > 17:
#    print ("eres mayor de edad")
#else:
#    print ("eres un menor de edad")        

#numero = int(input("escribe un numero"))
#if numero > 5:
#    print ("es mayor a 5")
#elif numero == 5:
#    print ("es igual a 5")
#else:
#    print ("es menor a 5")

#FUNCIONES
# def conversacion (mensaje):
#    print ("hola " + mensaje + " adios ")

#opcion = int (input("elige la opcion 1, 2 o 3:  "))
#if opcion == 1:
#    conversacion ("elegiste la opcion 1")
#elif opcion == 2:
#    conversacion ("elegiste la opcion 2")
#elif opcion == 3:
#    conversacion ("elegiste la opcion 3")
#else :
#    print ("opcion incorrecta")


#menu = """
#Bienvenido al convertidor de monedas
#1- pesos colombianos
#2- pesos argentinos
#3- pesos mexicanos
#"""
#def convertir (pesos, cambio):
#    pesos = float(pesos)
#    dolares = pesos/cambio 
#    dolares = round (dolares, 2)
#    dolares = str(dolares) ##convierte dolares en texto
#    print("tienes $"+ dolares + " dolares") ##imprime el valor texto de dolares

#opcion = int(input (menu))
#if opcion == 1:
#    pesos = input ("cuantos pesos colombianos tienes? ")
#    cambio = 3875
#    convertir (pesos, cambio)
#elif opcion == 2:
#    pesos = input ("cuantos pesos argentinos tienes? ")
#    cambio = 65
#    convertir (pesos, cambio)
#elif opcion == 3:
#    pesos = input ("cuantos pesos mexicanos tienes? ")
#    cambio = 24
#    convertir (pesos, cambio)
#else:
#    print ("ingrese un valor correcto")


#nombre = "Nestor"
#print (nombre [2])
#print (nombre [0:2] + nombre [2:5])
#print (nombre[0:2:5])
#nombre = "nestor"
#nombre.upper() #Coloca todo en mayuscula#
#nombre.capitalize() #colocar la primera en mayuscula
#nombre = nombre.capitalize() # guarda la primera en mayuscula 
#nombre.strip() #Elimina espacios 
#nombre.lower() #todo el texto en minuscula
#nombre.replace('o', 'a') #cambia las o por la a
#lent(nombre) #cuantos caracteres tiene

#contador = 0
#print ("2 elevado a " + str (contador) + " es igual a: " + str(2**contador))

#def run():
#    LIMITE = 1000 #definir una variable con mayuscula indica que no va a cambiar
#    contador = 0
#    potencia_2 = 2**contador
#    while potencia_2 < LIMITE: 
#        print ("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
#        contador = contador + 1
#        potencia_2 = 2**contador

#if __name__ == "__main__":
#    run () 

#contador = contador + 1 es igual a contador +=

#for contador in range(1000): #la variable contador tomará los valores del rango de 0 hasta 1000
#    print(contador) #imprime lo que haya en contador

#for i in range(10): #para la variable i en el rango del 0 al 9 
#    print(11*i) #imprime la tabla del 11 

#def run():
#    nombre = input ("escribe tu nombre: ")
#    for letra in nombre: #para cada letra en nombre imprime cada letra
#        print(letra)
#    frase = input ("escribe una frase: ")    
#    for caracter in frase:
#        print(caracter.upper()) 

#if __name__ == "__main__":
#    run () 

#def run():
#    for contador in range(10): #para contador en el rango de 10 o de 0 a 9
#        if contador % 2 == 0:  #si contador dividido entre 2 es exactamente igual a 0 continue
#            continue
#        else:
#            print (contador)  #si no es igual a cero entonces imprima lo que hay en contador 
#    for i in range(15):
#        print(i)
#        if i==10:
#            break
#          
#   
#if __name__ == "__main__":
#    run () 

#def lista_dividida(divisor, lista):
#    return [i / divisor for i in lista] 
#devuelve una lista en la cual cada espacio en i lo divide en el valor entregado 
#a la funcion recorriendo la lista en cada espacio i de la lista recibida


#lista = list(range(10))
#divisor = 2 

#print (lista_dividida(divisor, lista))



