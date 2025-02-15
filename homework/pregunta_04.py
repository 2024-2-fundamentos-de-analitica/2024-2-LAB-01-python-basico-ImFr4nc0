"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    ruta_archivo = 'files/input/data.csv'

    with open(ruta_archivo, 'r') as file:

        lines = file.readlines()

        conteo_por_mes = {}

        for line in lines:

            columns = line.strip().split('\t')

            fecha = columns[2]

            mes = fecha.split('-')[1]

            if mes in conteo_por_mes:
                conteo_por_mes[mes] += 1
            else:
                conteo_por_mes[mes] = 1

    lista_tuplas = sorted(conteo_por_mes.items(), key=lambda x: x[0])

    return lista_tuplas
