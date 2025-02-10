import csv

def leer_cotizaciones(fichero):
    """Lee un fichero CSV de cotizaciones y devuelve un diccionario con los datos organizados por columnas."""
    with open(fichero, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        encabezados = next(reader)
        datos = {col: [] for col in encabezados}
        
        for fila in reader:
            for i, valor in enumerate(fila):
                valor = valor.replace(',', '.')
                try:
                    valor = float(valor)
                except ValueError:
                    pass
                datos[encabezados[i]].append(valor)
    
    return datos

def calcular_estadisticas(datos, fichero_salida):
    """Calcula mínimo, máximo y media de cada columna y guarda el resultado en un nuevo fichero CSV."""
    estadisticas = {}
    
    for clave, valores in datos.items():
        if all(isinstance(v, float) for v in valores):
            estadisticas[clave] = {
                'Mínimo': min(valores),
                'Máximo': max(valores),
                'Media': sum(valores) / len(valores)
            }
    
    with open(fichero_salida, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["Columna", "Mínimo", "Máximo", "Media"])
        for clave, valores in estadisticas.items():
            writer.writerow([clave, valores['Mínimo'], valores['Máximo'], valores['Media']])


file_path = "C:/Users/delgado.hebru24_tria/Desktop/PYTHON/Ejercicios 2/cotizacion.csv"
datos = leer_cotizaciones(file_path)
calcular_estadisticas(datos, "C:/Users/delgado.hebru24_tria/Desktop/PYTHON/Ejercicios 2/estadisticas.csv")
