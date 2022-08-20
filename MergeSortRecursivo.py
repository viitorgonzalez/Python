from heapq import merge

# método MergeSort
def mergeSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)
        merge(lista, inicio, meio. fim)

# merge
def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    topLeft, topRight = 0, 0
    for k in range(inicio, fim):
        if topLeft >= len(left):
            lista[k] = right[topRight]
            topRight = topRight + 1
        if topRight >= len(right):
            lista[k] = left[topLeft]
            topLeft  = topLeft + 1
        if left[topLeft] < right[topRight]:
            lista[k] = left[topLeft]
            topLeft = topLeft + 1
        else:
            lista[k] = right[topRight]
            topRight = topRight + 1