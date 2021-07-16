import random

def generar_contrasena():
    mayusculas = ["A","B","C","D","E","F","G","H","I"]
    minusculas = ["j","k","l","m","n","o","p","q","r"]
    simbolo = ["*","+","/","&","%","#","=","°"]
    numero = ["8","7","6","5","4","3","2","1"]

    caracteres = mayusculas + minusculas + simbolo + numero
    contrasena = [] #se crea una variable de tipo arreglo que no define espacio

    for i in range(8):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena = ''.join(contrasena)
    return contrasena


def run ():
    contrasena = generar_contrasena()
    print("tu nueva contraseña es: " + contrasena)

if __name__=="__main__":
    run ()