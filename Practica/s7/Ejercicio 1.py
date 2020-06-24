def myrange(stop, start, step):
    lista = []

    while (start <= stop):

        if stop < 0:
            return "error"
        elif start < 0:
            return "error"
        elif step < 0:
            return "error"
        else:
            lista.append(start)
        start += step

    return lista


myrange(10, 1, 2)
print(myrange(10, 1, 2))