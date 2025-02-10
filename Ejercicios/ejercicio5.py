def evaluar_carrera(acciones, pista):
    pista_lista = list(pista)  
    for i, accion in enumerate(acciones):
        if i >= len(pista_lista):  
            return False
        
        if accion == "run":
            if pista_lista[i] == "|":
                pista_lista[i] = "/" 
            elif pista_lista[i] == "_":
                continue 
        elif accion == "jump":
            if pista_lista[i] == "_":
                pista_lista[i] = "x"  
            elif pista_lista[i] == "|":
                continue  

    carrera_superada = all(p == "_" or p == "|" for p in pista_lista)

    print("".join(pista_lista))
    
    return carrera_superada

acciones = ["run", "jump", "run", "jump"]
pista = "_|_||_"
resultado = evaluar_carrera(acciones, pista)
print(f"¿Ha superado la carrera? {resultado}")
