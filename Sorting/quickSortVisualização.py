def partition_debug(arr, low, high):
    pivot = arr[high]
    i = low - 1
    print(f"\nINÍCIO partition(low={low}, high={high})")
    print(f"Estado inicial: arr={arr}, pivot=arr[{high}]={pivot}, i={i}")
    for j in range(low, high):
        print(f"\nj={j} -> comparando arr[{j}]={arr[j]} com pivot={pivot}")
        if arr[j] <= pivot:
            i += 1
            print(f"  arr[{j}] <= pivot, então i -> {i} e vamos trocar arr[{i}] com arr[{j}]")
            arr[i], arr[j] = arr[j], arr[i]
            print(f"  após troca: arr={arr}")
        else:
            print(f"  arr[{j}] > pivot, nenhuma troca. i permanece {i}")
    print(f"\nFim do loop. Agora colocamos o pivô no lugar correto: swap arr[{i+1}] com arr[{high}]")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"Após posicionar pivô: arr={arr}")
    print(f"Retornando posição do pivô: {i + 1}\n")
    return i + 1


arr = [10, 7, 8, 9, 1, 5]  
pi = partition_debug(arr, 0, 5)