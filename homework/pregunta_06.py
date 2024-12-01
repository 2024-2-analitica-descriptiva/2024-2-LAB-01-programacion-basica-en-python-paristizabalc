"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import itertools

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
    with open("files/input/data.csv", "r") as file:
        data = [i.split("\t")[4].replace("\n", "").split(",") for i in file.readlines()]

        data = [i.split(":") for i in list(itertools.chain(*data))]

    min_max = [
        (
            key,
            min(int(value) for k, value in data if k == key),
            max(int(value) for k, value in data if k == key),
        )
        for key in set(k for k, _ in data)
    ]

    return sorted(min_max)


if __name__ == "__main__":
    print(pregunta_06())