"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    ruta_archivo = 'files/input/data.csv'
    
    with open(ruta_archivo, 'r') as file:

        lines = file.readlines()
        
        conteo_letras = {}
        
        for line in lines:

            columns = line.strip().split('\t')

            letra = columns[0]

            if letra in conteo_letras:
                conteo_letras[letra] += 1
            else:
                conteo_letras[letra] = 1

    lista_tuplas = sorted(conteo_letras.items(), key=lambda x: x[0])

    return lista_tuplas