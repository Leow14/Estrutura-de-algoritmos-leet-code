def bubblesort(arr):
    is_changed = True
    while is_changed:
        is_changed = False
        i = 0  # ← Resetar i aqui!
        while i < len(arr) - 1:
            j = i + 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                is_changed = True
            i += 1
    return arr

print(bubblesort([1,5,4,3,2,6]))