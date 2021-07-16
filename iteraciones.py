#contador_externo = 0
#contador_interno = 0

#while contador_externo < 5:
#    while contador_interno < 6:
#        print(contador_externo, contador_interno)
#        contador_interno += 1
#    contador_externo += 1
#    contador_interno = 0

#frutas = ['manzana', 'pera', 'mango']
#for fruta in frutas:
#    print(frutas)


#objetivo = int(input("escoge un numero "))
#respuesta = 0

#while respuesta**2 < objetivo:
#    respuesta += 1
#if respuesta **2 == objetivo:
#    print('la raiz cuadrada de {objetivo} es {respuesta}')
#else :
#    print( "{objetivo} No tiene raiz cudrada exacta")


#objetivo_raiz = int(input("escoge un numero"))
#epsilon = 0.1 #que tan cerca llegamos a la respuesta
#paso = epsilon**2 #que tanto nos vamos a acercar 
#respuesta = 0.0 #el valor que toma la respuesta

#while abs(respuesta**2 - objetivo_raiz) >= epsilon and respuesta <= objetivo_raiz :
#    respuesta += paso  # respuesta = respuesta + paso
    
#if abs(respuesta**2 - objetivo_raiz) >= epsilon:
#    print("no se encontro la razi")
#else :
#    print ("la raiz cuadrada de " + str(objetivo_raiz) + "es " + str(respuesta))

objetivo2_raiz = int(input("escoge un numero"))
epsilon = 0.1 #que tan cerca llegamos a la respuesta
bajo = 0.0
alto = max(1.0 , objetivo2_raiz) #metodo max que permite escoger el mayor entre 1 y el valor ingresado 
respuesta = (alto + bajo) / 2 

while abs(respuesta**2 - objetivo2_raiz) >= epsilon :
    print (" alto " + str(alto) + " bajo " + str(bajo) + " respuesta " + str(respuesta))
    if respuesta**2 < objetivo2_raiz:
        bajo = respuesta
    else :
        alto = respuesta

    respuesta = (alto + bajo) / 2
print ("la raiz cuadrada de " + str(objetivo2_raiz) + " es " + str(respuesta))

