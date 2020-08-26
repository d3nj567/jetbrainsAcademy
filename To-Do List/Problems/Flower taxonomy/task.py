iris = {}


def add_iris(id_n, species, petal_length, petal_width, **flowers):
    iris.update({id_n: {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}})
    for key, value in flowers.items():
        iris[id_n].update({key: value})
