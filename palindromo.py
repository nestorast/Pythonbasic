def palindromo (nombre):
    nombre = nombre.replace(" ", "")
    nombre = nombre.lower()
    nombre_invertido = nombre[::-1] #genera una nueva varialbe invertida que recorre del final al principio en pasos de uno
    if nombre == nombre_invertido:
        return True
    else:
        return False    

def run():
    nombre = input("escribe un nombre: ")
    es_palindromo = palindromo(nombre)
    if es_palindromo == True:
        print ("Es palindromo")
    else:
        print ("No es palindromo")    

if __name__ == '__main__': #el punto de entrada siempre se encuenta en python empieza a correr lo que esta debajo
    run()
