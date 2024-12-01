"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import itertools

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv", "r") as file:
        data = [[int(i.split("\t")[1])] + [i.split("\t")[3]] for i in file.readlines()]

    data = [[char, item[0]] for item in data for char in item[1].split(",")]

    acumulado = {
        key: sum(int(value) for k, value in data if k == key)
        for key in set(k for k, _ in data)
    }

    return dict(sorted(acumulado.items()))


if __name__ == "__main__":
    print(pregunta_11())