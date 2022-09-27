#quicksort
def quickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quickSort(lista, inicio, p - 1)
        quickSort(lista, p + 1, fim)

#partition
def partition(lista, inicio, fim):
        pivot = lista[fim]
        i = inicio
        for j in range(inicio, fim):
            if lista[j] <= pivot:
                lista[j], lista[i] = lista[i], list[j]
                i = i + 1
        lista[i], lista[fim] = lista[fim], lista[i]
        return i