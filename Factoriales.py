
numero = int(input("escribe un numero "))

for i in range(numero):
    if i == 0:
        continue 
    else :
        numero = numero * i
        i += 1
        print (numero)

print ("El factorial es: " + str (numero)) 


def factorial(n):
    print (n)
    if n==1 :
        return 1
    else :
        return n * factorial(n-1)  # se ejecuta la funcion 5 veces en las cuales cada vez el valor de n dentro de la funcion disminuye
                                   #pero se guarda en n el valor acumulado de la multiplicacion
                                   #una vez se sale de la condicion imprime el valor guardado de n     


n = int(input("escribe un numero "))
print (factorial(n))



