"""
print("Eyeyeyey pibitas del mundo")

#Aritmetica

print(2+3)

res = None

res= "hola"

print(res)

cadena_salto_de_linea = "Hola\nmundo"

cadena_tabulacion = "Hola\tmundo"

print(cadena_salto_de_linea)

print(cadena_tabulacion)

#Para escapar el \n
print (r"C:\nombre\directorio")



print(cadena_mas_de_dos_lineas)

print("Hola" + "mundo")

"""


"""


#LISTAS

lista = [1,2,3,4,5]

print(lista)

#Acceder a un elemento de la lista

print(lista[0])

#Acceder al ultimo elemento de la lista

print(lista[-1])

#Acceder a un rango de elementos

print(lista[0:3])

#Agregar un elemento a la lista

lista.append(6)

print(lista)

#Agregar un elemento en una posicion especifica

lista.insert(1,1.5)

print(lista)

#Agregar varios elementos a la lista

lista.extend([7,8,9])

print(lista)

#Eliminar un elemento de la lista

lista.remove(1.5)

print(lista)

#Eliminar el ultimo elemento de la lista

lista.pop() 

print(lista)

#Eliminar un elemento de la lista por su indice

del lista[0]

print(lista)

#Eliminar un rango de elementos de la lista

del lista[0:2]

print(lista)

#Eliminar todos los elementos de la lista

lista.clear()

print(lista)

# Listas anidadas

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]

print(r)

"""

"""

#Lectura por teclado

nombre = input("Cual es tu nombre? ")

print("Hola " + nombre)

valor = input("Introduce un número o flotante:")

valor = float(valor)

print(valor*2)


"""

#Condicionales

a = 5
if a == 2:
    print("a vale 2")
if a == 5:
    print("a vale 5")

#Iteraciones

#Bucle while

c = 0
while c <= 5:
    c+=1
    print("c vale", c)
else:
    print("Se ha completado toda la iteración y c vale", c)

# For con listas

numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1

# For clásico
for numero in numeros:  # Para [variable] en [lista]
    print(numero)

# Podemos utilizar la función enumerate() para conseguir el índice y el valor en cada iteración fácilmente:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
print(numeros)


# La función range()

for i in range(5):
    print(i)

# Pinta los 5 primeros de la lista

# Si queremos conseguir la lista literal podemos transformar el range a una lista:

list(range(10))

# Tuplas

#¿Qué es una tupla?

#Una tupla es una colección de objetos que no puede modificarse (es inmutable). Las tuplas son secuencias, al igual que las listas. La principal diferencia entre tuplas y listas es que las tuplas no pueden modificarse, a diferencia de las listas. Una tupla va entre paréntesis y los elementos separados por comas.

tupla = (100,"Hola",[1,2,3],-50)

print(tupla)
print(tupla[0])
print(tupla[-1])
print(tupla[2:])
print(tupla[2][-1])

# Los elementos de una tupla no se pueden modificar, pero sí podemos extraer porciones de una tupla, cortarla, y también podemos comprobar si un elemento se encuentra en la tupla.

#tupla[0] = 50 # Esto da error

# Funcion len() en tuplas

len(tupla)

# Funcion index() en tuplas

tupla.index(100)

#Dice en que posición se encuentra el valor 100

# Conjuntos

conjunto = set()

conjunto = {1,2,3}

# Metodo add

conjunto.add(4)

# Conversiones con listas

lista = [1,2,3,3,2,1]

print(lista)

conjunto = set(lista)
lista = list(conjunto)

print(lista)

cadena = "Al pan pan y al vino vino"
set(cadena)

