def es_primo (numero):
  contador = 0
  for i in range(1, numero + 1): # para i en el rango que va desde el 1 hasta el numero pero el verdadore es el numero ingresado mas 1
      if i == 1 or i == numero:
          continue
      if numero % i == 0: #si numero dividido por i es igual a 0 entonces aumente el contador si no salga del for e inice 
          contador += 1   #se aumenta uno al contador cuando el numero no sea primo 
  if contador == 0:  #si al correr todo el cicloe el contador nunca aumento entonces retorna true 
      return True
  else :
      return False
  

def run () :
    numero = int(input("escribe un numero: "))
    if es_primo(numero) == True: #se puede colocar sin ==True pues es redundante
        print ("es primo")
    else:
        print ("No es primo")


if __name__== "__main__":
    run ()