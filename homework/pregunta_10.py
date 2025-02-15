"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    ruta_archivo = 'files/input/data.csv'
    with open(ruta_archivo, 'r') as file:
        
        lines = file.readlines()
        resultado = []
        
        for line in lines:
            columns = line.strip().split('\t')
            letra = columns[0]
            columna_4 = columns[3].split(',')
            columna_5 = columns[4].split(',')
            cantidad_columna_4 = len(columna_4)
            cantidad_columna_5 = len(columna_5)
            resultado.append((letra, cantidad_columna_4, cantidad_columna_5))
            
        return resultado
