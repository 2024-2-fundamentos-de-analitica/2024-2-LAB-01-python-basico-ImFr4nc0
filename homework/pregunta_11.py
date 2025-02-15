"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    ruta_archivo = 'files/input/data.csv'
    with open(ruta_archivo, 'r') as file:
        
        lines = file.readlines()
        suma_por_letra = {}
        
        for line in lines:
            columns = line.strip().split('\t')
            valor_columna_2 = int(columns[1])
            letras_columna_4 = columns[3].split(',')
            
            for letra in letras_columna_4:
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor_columna_2
                else:
                    suma_por_letra[letra] = valor_columna_2
                    
        suma_por_letra_ordenado = {k: suma_por_letra[k] for k in sorted(suma_por_letra)}
        
        return suma_por_letra_ordenado
