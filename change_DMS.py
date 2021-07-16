import math

def calcular (latitud, longitud):
      if latitud[0] == "N" :
          gradolat = int(latitud[1])
          minutolat = int(latitud[2:4])
          segundolats = float(latitud[4:9])
          latitud_decimal = gradolat + minutolat/60 + segundolats/3600
          #print ("la latitud ingresada es " + str(gradolat) + " " + str(minutolat) + " " + str(segundolats))
          print("el valor decimal es: " + str(round (latitud_decimal, 4)))
      else :
          gradolat = int(latitud[1])
          minutolat = int(latitud[2:4])
          segundolats = float(latitud[4:9])
          latitud_decimal = gradolat + minutolat/60 + segundolats/3600
          #print ("la latitud ingresada es " + str(gradolat) + " " + str(minutolat) + " " + str(segundolats))
          print("el valor decimal de la latitud es: " + str(round (latitud_decimal, 4)))
      if longitud[0] == "W" :
          gradolon = int(longitud[1:3])
          minutolon = int(longitud[3:5])
          segundolon = float(longitud[5:10])
          longitud_decimal = 0-(gradolon + minutolon/60 + segundolon/3600)
          #print ("la latitud ingresada es " + str(gradolat) + " " + str(minutolat) + " " + str(segundolats))
          print("el valor decimal de la longitud es: " + str(round (longitud_decimal, 4)))
     
def conver ():
    
    print ("CONVERTIR DE DMS a DECIMAL")
    print ("ejemplo para ingresar datos N51025.35 o S51025.35 lo mismo para la longitud W o E")
    latitud =  input("ingrese la latitud grados minutos segundos: ")
    longitud = input("ingrese la longitud grados minutos segundos: ")
    calcular (latitud, longitud)
        
     

if __name__== "__main__":
    conver ()


