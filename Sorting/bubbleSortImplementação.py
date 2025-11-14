def bubblesort(arr):
    left = 0
    right = 1
    limit = len(arr)
    while limit >= 1:
        
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

        left, right = left + 1, right + 1

        if right >= len(arr):
            left, right, limit = 0, 1, limit - 1

    return arr

    

print(bubblesort([5, 3, 1, 4, 2, 8, 90, 10, 3, 45, 2, 1, 1 ,1 ,1 ,1 ,1, 67, 3, 3 ,33 ,46]))