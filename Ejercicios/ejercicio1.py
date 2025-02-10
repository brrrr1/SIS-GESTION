morse_dicc = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '  '  
}

def texto_a_morse(texto):
    texto = texto.upper()  
    morse = []
    for char in texto:
        if char in morse_dicc:
            morse.append(morse_dicc[char])
        else:
            morse.append('') 
    return ' '.join(morse)

def morse_a_texto(morse):
    morse_dict_reversed = {v: k for k, v in morse_dicc.items()} 
    morse_lista = morse.split('  ')
    texto = []
    for palabra in morse_lista:
        letras = palabra.split()
        palabra_texto = ''.join([morse_dict_reversed.get(letra, '') for letra in letras])
        texto.append(palabra_texto)
    return ' '.join(texto)

def convertir(texto):
    if '.' in texto or '—' in texto:
        return morse_a_texto(texto)
    else:
        return texto_a_morse(texto)

texto_normal = "Hola Mundo"
morse_texto = texto_a_morse(texto_normal)
print(f"Texto a Morse: {morse_texto}")

morse_input = "... --- ..."
texto_convertido = convertir(morse_input)
print(f"Morse a Texto: {texto_convertido}")
