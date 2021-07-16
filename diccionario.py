#def run ():
#    poblacion_paises = {
#        'argentina' : 20435567,
#        'Colombia' : 50980987,
#        'Mexico': 349567809,
#    }

#    for pais in poblacion_paises.keys():
#        print(pais)
#    for pais in poblacion_paises.values():
#        print(pais)
#     poblacion_paises['Colombia'] = 6000000 # esta linea asigna a colombia otro valor  
#     poblacion_paises['España'] = 9500987 # esta linea crea un nuevo registro a el diccionario poblacion_paises

#if __name__=="__main__":
#    run()

#iter('cadena') # cadena
#iter(['a', 'b', 'c']) # lista   #se puede modificar 
# a = [1, 2, 3]
# b = list (a) # en este caso con el metodo list B y A no ocupan el mismo espacion en memoria y tienen los mismos valores pero puedo modificar A o B sin afectar lo que haya en el otro 
# c = a [::] # en C le asigna los valores de a que son 1,2,3 pero lo hace recorriendo los espacios 
#iter(('a', 'b', 'c')) #         #tupla no se puede modificar
#mitupla = (1, "a", "b")
#othertupla = (2, 3, 4)
#mitupla += othertupla  # es lo mismo que decir mitupla = mitupla + othertupla realiza una union de las dos tuplas
#print (mitupla)
#iter({'a', 'b', 'c'}) # conjunto
#iter({'a': 1, 'b': 2, 'c': 3}) # diccionario

#my_list = list(range(100))
#print (my_list)
#double = [ i*2 for i in my_list]  # a cada valor de la lista lo recorre con (i) y el valor que se encuentra en el espacio lo multiplica por 2
#print (double)
#pares = [i for i in my_list if i % 2 == 0] 
#recorre cada espacio de la lista + a cada valor que se encuentra en la posicion (i) if la division de ese valor por 2 es exactamente igual a 0 lo muestra si no continua 

