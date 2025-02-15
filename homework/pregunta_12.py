"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    ruta_archivo = 'files/input/data.csv'
    with open(ruta_archivo, 'r') as file:

        lines = file.readlines()
        suma_por_letra = {}

        for line in lines:
            columns = line.strip().split('\t')
            letra = columns[0]
            columna_5 = columns[4].split(',')
            suma = 0

            for par in columna_5:
                valor = int(par.split(':')[1])
                suma += valor
            if letra in suma_por_letra:
                suma_por_letra[letra] += suma
            else:
                suma_por_letra[letra] = suma

        suma_por_letra_ordenado = {k: suma_por_letra[k] for k in sorted(suma_por_letra)}

        return suma_por_letra_ordenado