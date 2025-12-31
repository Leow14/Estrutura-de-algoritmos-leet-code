
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

print(bubblesort([1,2,3,4,5,6]))