#Bruno Delgado Herrero 2ºDAM 01/10/2024

import math

#Ejercicio 1
print("Ejercicio 1")
def area_rectangulo(base, altura):
    return base * altura


base = 15
altura = 10
area = area_rectangulo(base, altura)
print(f"El área del rectángulo es: {area}")

#Ejercicio 2
print("\nEjercicio 2")
def area_circulo(radio):
    return math.pi * radio ** 2

radio = 5
area = area_circulo(radio)
print(f"El área del círculo es: {area}")

#Ejercicio 3
print("\nEjercicio 3")
def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
    
a = 5
b = 10
resultado1 = relacion(a, b)
resultado2 = relacion(b, a)
resultado3 = relacion(a, a)
print("El resultado de la relación entre a y b es:", resultado1)
print("El resultado de la relación entre b y a es:", resultado2)
print("El resultado de la relación entre a y a es:", resultado3)

# Ejercicio 4
print("\nEjercicio 4")
def intermedio(a, b):
    return (a + b) / 2

a = -12
b = 24

print(f"El número intermedio entre {a} y {b} es: {intermedio(a, b)}")

# Ejercicio 5
print("\nEjercicio 5")
def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero
    
numero = 15
minimo = 0
maximo = 10

print(f"El número {numero} recortado entre {minimo} y {maximo} es: {recortar(numero, minimo, maximo)}")

# Ejercicio 6
print("\nEjercicio 6")
def separar(lista):
    pares = []
    impares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
            
    return pares, impares

pares, impares = separar([6,5,2,1,7])
print("Pares:", pares)
print("Impares:", impares)