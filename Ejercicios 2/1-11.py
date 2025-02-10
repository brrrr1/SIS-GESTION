print("Ejercicio 1: Números divisibles por 7")
numeros_divisibles_7 = [n for n in range(1, 1001) if n % 7 == 0]
print(numeros_divisibles_7)

print("\nEjercicio 2: Números que contienen al menos un 3")
numeros_con_3 = [n for n in range(1, 1001) if '3' in str(n)]
print(numeros_con_3)

print("\nEjercicio 3: Contar espacios en una cadena")
cadena = "Ejemplo de cadena con espacios"
numero_espacios = sum(1 for c in cadena if c == ' ')
print(numero_espacios)

print("\nEjercicio 4: Consonantes en la cadena dada")
cadena = "A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"
consonantes = [c for c in cadena.lower() if c.isalpha() and c not in "aeiouáéíóú"]
print(consonantes)

print("\nEjercicio 5: Índice y valor como tupla")
lista = ["hi", 4, 8.99, 'apple', ('t,b','n')]
indice_valor = [(i, v) for i, v in enumerate(lista)]
print(indice_valor)

print("\nEjercicio 6: Números comunes en dos listas")
lista_a = [1, 2, 3, 4]
lista_b = [2, 3, 4, 5]
numeros_comunes = [n for n in lista_a if n in lista_b]
print(numeros_comunes)

print("\nEjercicio 7: Obtener números de una oración")
oracion = 'En 1984 hubo 13 casos de protesta con más de 1000 asistentes'
numeros_en_oracion = [int(s) for s in oracion.split() if s.isdigit()]
print(numeros_en_oracion)

print("\nEjercicio 8: Lista de pares e impares")
numbers = range(20)
par_impar = ["par" if n % 2 == 0 else "impar" for n in numbers]
print(par_impar)

print("\nEjercicio 9: Tuplas de números coincidentes en dos listas")
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
numeros_coincidentes = [(n, n) for n in list_a if n in list_b]
print(numeros_coincidentes)

print("\nEjercicio 10: Palabras con menos de 4 letras")
cadena = "Este es un texto de ejemplo para encontrar palabras cortas"
palabras_cortas = [p for p in cadena.split() if len(p) < 4]
print(palabras_cortas)

print("\nEjercicio 11: Números divisibles por cualquier dígito 2-9")
numeros_divisibles = [n for n in range(1, 1001) if any(n % d == 0 for d in range(2, 10))]
print(numeros_divisibles)