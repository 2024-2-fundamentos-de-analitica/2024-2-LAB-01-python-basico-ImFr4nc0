"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    ruta_archivo = 'files/input/data.csv'
    with open(ruta_archivo, 'r') as file:

        lines = file.readlines()
        conteo_claves = {}

        for line in lines:
            columns = line.strip().split('\t')
            columna_5 = columns[4]
            pares_clave_valor = columna_5.split(',')

            for par in pares_clave_valor:
                clave = par.split(':')[0]
                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1

        conteo_claves_ordenado = {k: conteo_claves[k] for k in sorted(conteo_claves)}

        return conteo_claves_ordenado
