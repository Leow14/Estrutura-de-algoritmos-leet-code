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

def quicksort(arr):
    # Definir o pivô
    # Colocar o pivô na ordem correta
    # Usar ponteiros para mostrar limitar o novo array 
    
    return 0

def mergesort(arr):
