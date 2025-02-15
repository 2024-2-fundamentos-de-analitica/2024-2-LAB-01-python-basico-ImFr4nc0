"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    ruta_archivo = 'files/input/data.csv'

    with open(ruta_archivo, 'r') as file:

        lines = file.readlines()

        suma_por_letra = {}

        for line in lines:

            columns = line.strip().split('\t')

            letra = columns[0]

            valor = int(columns[1])

            if letra in suma_por_letra:
                suma_por_letra[letra] += valor
            else:
                suma_por_letra[letra] = valor

    lista_tuplas = sorted(suma_por_letra.items(), key=lambda x: x[0])

    return lista_tuplas
