from ufos import *
from datetime import datetime

print("\n")
# Test de la función lee_avistamientos
avistamientos = lee_avistamientos('C:/Users/delgado.hebru24_tria/Desktop/PYTHON/Ufos/data/ovnis.csv')
for a in avistamientos[:5]:
    print(a)

#Test de la función duracion_total
duracion = duracion_total(avistamientos, "fl")
print(f"Duración total de los avistamientos en Florida: {duracion}")
    
# Test de la función comentario_mas_largo
comentario = comentario_mas_largo(avistamientos, 2015, 'ufo')
print(f"Comentario más largo: {comentario}")

# Test de la función indexa_formas_por_mes
formas_mes = indexa_formas_por_mes(avistamientos)
for mes, formas in formas_mes.items():
    print(f"{mes}: {formas}")
    


# Test de la función avistamientos_fechas
avistamientos = avistamientos_fechas(avistamientos, datetime(2005, 5, 1), datetime(2005, 6, 1))
for a in avistamientos:
    print(a)
    



# Test de la función hora_mas_avistamientos
hora = hora_mas_avistamientos(avistamientos)
print(f"Hora con más avistamientos: {hora}")


#Test de la funciión dicc_estado_longitud_media_comentario
dicc = dicc_estado_longitud_media_comentario(avistamientos)
for estado, longitud in dicc.items():
    print(f"{estado}: {longitud}")
    