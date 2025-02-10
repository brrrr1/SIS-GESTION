def capitalizar_palabras(texto):
    resultado = ""
    en_palabra = False  

    for i, char in enumerate(texto):
        if char.isalpha():
            if not en_palabra:
                resultado += char.upper()
                en_palabra = True
            else:
                resultado += char.lower()
        else:
            resultado += char
            en_palabra = False

    return resultado

texto = "esto es un ejemplo de texto"
resultado = capitalizar_palabras(texto)
print(resultado)
