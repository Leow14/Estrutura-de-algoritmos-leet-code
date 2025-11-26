# Implementação de todos os sorts vistos em aula:
# MergeSort 🆗
# QuickSort 🆗
# BubbleSort 🆗

# Exercícios complementares:
# https://leetcode.com/problems/sort-list/
# https://leetcode.com/problems/sort-an-array/
# https://leetcode.com/problems/sort-colors/description/
# https://leetcode.com/problems/relative-sort-array/


#
#
# BubbleSort em arrays
#
#


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

#
#
# QuickSort em arrays
#
#


def quicksort(arr, left, right):

    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi - 1)
        quicksort(arr, pi + 1, right)


def partition(arr, left, right):
    # Não selecionei o pivot da melhor maneira possível
    pivot = arr[right]
    # Iniciando o ponteiro "i"
    i = left - 1

    # Colocando todos os menores que o pivot para a esquerda
    for j in range(left, right):
        # Se o valor for menor que o do pivot, o i anda 1, e os ponteiros...
        # ..."i" + 1 e "j" trocam de lugar
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    # Chegaremos em um momento em que tudo a esquerda está organizado
    # E precisamos somente colocar o pivot no lugar certo
    # Por isso efetuamos a troca de right com i + 1
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

#
#
# MergeSort feito em linked lists
#
#


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_middle(head):
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_linked(arr1, arr2):
    head = Node()
    tail = head

    while arr1 and arr2:
        if arr1.val < arr2.val:
            tail.next = arr1
            arr1 = arr1.next
        else:
            tail.next = arr2
            arr2 = arr2.next
        tail = tail.next

    if arr1:
        tail.next = arr1
    else:
        tail.next = arr2

    return head.next


def mergesort_linked(head):
    if not head or not head.next:
        return head

    middle = find_middle(head)
    l2 = middle.next
    middle.next = None
    left = mergesort_linked(head)
    right = mergesort_linked(l2)

    return merge_linked(left, right)


def print_linked_list(head):
    # O head obviamente deve ser o head de uma linked list

    linked_print = "[" + str(head.val)
    head = head.next
    while head:
        linked_print += ", " + str(head.val)
        head = head.next
    linked_print += "]"
    return (linked_print)

# Criação da linked list


node6 = Node(2, None)
node5 = Node(3, node6)
node4 = Node(1, node5)
node3 = Node(8, node4)
node2 = Node(7, node3)
node1 = Node(9, node2)

quick_arr = [2, 8, 7, 5, 3, 1, 15, 12, 4, 9]

bubble_arr = [5, 6, 1, 2 ,12, 4, 3, 15]

# Testes com todos os sorts

# Teste com quicksort
print(f"ARRAY ORIGINAL : {quick_arr}")
quicksort(quick_arr, 0, len(quick_arr) - 1)
print(f"ARRAY ALTERADO COM QUICKSORT : {quick_arr}")

# Teste com bubblesort
print(f"ARRAY ORIGINAL : {bubble_arr}")
bubblesort(bubble_arr)
print(f"ARRAY ALTERADO COM BUBBLESORT : {bubble_arr}")

# Teste com mergesort
print(f"LINKED LIST ORIGINAL: {print_linked_list(node1)}")
my_list = mergesort_linked(node1)
print(f"LINKED LIST ALTERADO COM MERGESORT: {print_linked_list(my_list)}")
