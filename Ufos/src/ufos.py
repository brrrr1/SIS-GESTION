import	csv
from math import sqrt
from collections import namedtuple, Counter, defaultdict

from datetime import datetime


#Creación de una tupla con nombre para los avistamientos
#Todas las lineas del csv se convierten en un namedtuple
Avistamiento = namedtuple('Avistamiento', 'fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')


#Se le pasa como parámetro la ruta en la que está el fichero csv
def lee_avistamientos(fichero):
    res= []
    with open(fichero, encoding= 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for x in lector:
            fecha_hora = x[0]
            fechahora = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud= float(x[6])
            longitud= float(x[7])
            tupla = Avistamiento(fechahora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            res.append(tupla)

    return res   

def duracion_total(avistamientos, estado):
    duracion = 0
    for a in avistamientos:
        if a.estado == estado:
            duracion += a.duracion
    return duracion



def comentario_mas_largo(avistamientos, anyo, palabra):
    res = 0
    for a in avistamientos:
        if a.fechahora.year == anyo and palabra in a.comentarios:

                res = a
    return res


def indexa_formas_por_mes(avistamientos):
    res = defaultdict(set)
    for a in avistamientos:
        mes = a.fechahora.strftime('%B')
        res[mes].add(a.forma)
    return res


def avistamientos_fechas(avistamientos, fecha_inicial=None, fecha_final=None):
    res = []
    for a in avistamientos:
        if fecha_inicial is None and fecha_final is None:
            res.append(a)
        elif fecha_inicial is None and a.fechahora <= fecha_final:
            res.append(a)
        elif fecha_final is None and a.fechahora >= fecha_inicial:
            res.append(a)
        elif a.fechahora >= fecha_inicial and a.fechahora <= fecha_final:
            res.append(a)
    return sorted(res, key=lambda x: x.fechahora, reverse=True)


def hora_mas_avistamientos(registros):
    horas = [a.fechahora.hour for a in registros]
    return Counter(horas).most_common(1)[0][0]


def dicc_estado_longitud_media_comentario(registros):
    res = defaultdict(list)
    for a in registros:
        res[a.estado].append(len(a.comentarios))
    return {estado: sum(comentarios) / len(comentarios) for estado, comentarios in res.items()}



