def comparar_arrays(arr1, arr2, comunes):
    resultado = []
    
    if comunes:
        for elemento in arr1:
            encontrado = False
            for e in arr2:
                if elemento == e:
                    encontrado = True
                    break
            if encontrado:
                resultado.append(elemento)
    else:
        for elemento in arr1:
            encontrado = False
            for e in arr2:
                if elemento == e:
                    encontrado = True
                    break
            if not encontrado:
                resultado.append(elemento)
        
        for elemento in arr2:
            encontrado = False
            for e in arr1:
                if elemento == e:
                    encontrado = True
                    break
            if not encontrado:
                resultado.append(elemento)
    
    return resultado

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

print(comparar_arrays(arr1, arr2, True))

print(comparar_arrays(arr1, arr2, False))
