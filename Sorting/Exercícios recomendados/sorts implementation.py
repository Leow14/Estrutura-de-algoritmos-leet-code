# Implementação de todos os sorts vistos em aula:
# MergeSort
# QuickSort
# BubbleSort 🆗

# Exercícios complementares:
# https://leetcode.com/problems/sort-list/
# https://leetcode.com/problems/sort-an-array/
# https://leetcode.com/problems/sort-colors/description/
# https://leetcode.com/problems/relative-sort-array/


# arr = [2, 1, 3, 4, 5]

def bubblesort(arr):
    i = 0
    limit = len(arr)
    is_changed = True
    steps = 0
    while is_changed is True:
        is_changed = False
        i = 0
        while i < limit - 1:
            j = i + 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                is_changed = True
            i += 1
            steps += 1
        limit -= 1
    print(steps)
    return arr

def quicksort(arr, low = 0, high = None):

    i = 0
    j = 1

    if high is None:
        high = len(arr) - 1

    if low >= high:
        return arr

    pivot = arr[high]

    if arr[i] > pivot and arr[j] < pivot:
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i + 1, j + 1
    elif arr[i] > pivot and arr[j] > pivot:
        j += 1
    else:
        i, j = i + 1, j + 1
    
    arr[i] = pivot

    

    # Colocar o pivô na ordem correta
    # Colocar tudo que é menor que o pivô a esquerda do pivô
    # Mesma coisa para tudo que é maior, que deve ficar a direita
    # Usar ponteiros para mostrar limitar o novo array
    # Usar uma lógica recursiva para pegar um novo pivô no sub array

    # Quando tivermos 0 ou 1 elementos, quer dizer que ele já está ordenado
    # Nesse caso, não fazemos nada e "voltamos" para o array

    return arr