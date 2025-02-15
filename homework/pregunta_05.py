"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    ruta_archivo = 'files/input/data.csv'

    with open(ruta_archivo, 'r') as file:

        lines = file.readlines()

        valores_por_letra = {}
        
        for line in lines:

            columns = line.strip().split('\t')

            letra = columns[0]

            valor = int(columns[1])

            if letra in valores_por_letra:
                max_actual, min_actual = valores_por_letra[letra]
                if valor > max_actual:
                    max_actual = valor
                if valor < min_actual:
                    min_actual = valor
                valores_por_letra[letra] = (max_actual, min_actual)
            else:
                valores_por_letra[letra] = (valor, valor)

    lista_tuplas = sorted([(letra, max_val, min_val) for letra, (max_val, min_val) in valores_por_letra.items()], key=lambda x: x[0])
    
    return lista_tuplas
