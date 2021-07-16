#Pruebas de caja negra

import unittest

def suma (num_1, num_2):
    return num_1 + num_2 #regresa la suma a donde se esta llamando la funcion

class CajaNegraTest(unittest.TestCase): #se crea una clase
   
    def test_suma_dos_positivos(self): # se crea una funcion
        num_1 = 10
        num_2 = 5
        resultado = suma(num_1, num_2) # se envia los valores a la funcion suma

        self.assertEqual(resultado, 15) # permite validar la condicion que el resultado sea igual a 15
    
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

if __name__=="__main__":
    unittest.main() #funcion que viene dentro del modulo unittest        


def es_mayor_de_edad(edad):
    if edad >= 18 :
        return True
    else:
        return False

class PruebaCristalTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        edad = 18
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)

if __name__=="__main__":
    unittest.main()