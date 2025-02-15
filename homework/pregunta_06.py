"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    ruta_archivo = 'files/input/data.csv'

    with open(ruta_archivo, 'r') as file:

        lines = file.readlines()

        valores_por_clave = {}

        for line in lines:

            columns = line.strip().split('\t')

            columna_5 = columns[4]

            pares_clave_valor = columna_5.split(',')

            for par in pares_clave_valor:

                clave, valor = par.split(':')
                valor = int(valor)

                if clave in valores_por_clave:
                    min_actual, max_actual = valores_por_clave[clave]
                    if valor < min_actual:
                        min_actual = valor
                    if valor > max_actual:
                        max_actual = valor
                    valores_por_clave[clave] = (min_actual, max_actual)
                else:
                    valores_por_clave[clave] = (valor, valor)

    lista_tuplas = sorted([(clave, min_val, max_val) for clave, (min_val, max_val) in valores_por_clave.items()], key=lambda x: x[0])

    return lista_tuplas