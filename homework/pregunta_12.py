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
    with open("files/input/data.csv", "r") as file:
        data = [
            [i.split("\t")[0]] + [i.split("\t")[4].replace("\n", "")]
            for i in file.readlines()
        ]

    data = [
        [
            item[0],
            int(char.split(":")[-1]),
        ]
        for item in data
        for char in item[1].split(",")
    ]

    acumulado = {
        key: sum(int(value) for k, value in data if k == key)
        for key in set(k for k, _ in data)
    }

    return dict(sorted(acumulado.items()))


if __name__ == "__main__":
    print(pregunta_12())