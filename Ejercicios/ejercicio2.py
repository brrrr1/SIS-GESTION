def verificar_equilibrado(expresion):
    pila = []
    delimitadores = {'(': ')', '{': '}', '[': ']'}

    for char in expresion:
        if char in delimitadores:
            pila.append(char)
        elif char in delimitadores.values():
            if not pila or delimitadores[pila.pop()] != char:
                return False

    return len(pila) == 0

expresion1 = "{ [ a * ( c + d ) ] - 5 }"
expresion2 = "{ a * ( c + d ) ] - 5 }"

print(verificar_equilibrado(expresion1))
print(verificar_equilibrado(expresion2))