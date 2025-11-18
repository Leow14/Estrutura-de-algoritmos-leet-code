# python 3.x
import random
import numpy as np
import matplotlib.pyplot as plt
import imageio
from copy import deepcopy

# 1) Helpers de visualização
def plot_bars(arr, title, fname=None):
    plt.figure(figsize=(6, 4))
    plt.bar(range(len(arr)), arr, color="#4C78A8")
    plt.title(title)
    plt.tight_layout()
    if fname:
        plt.savefig(fname, dpi=110)
        plt.close()
    else:
        plt.show()

def to_frames(arr, snapshots, algo_name):
    # snapshots: lista de arrays (estados intermediários)
    frames = []
    for i, snap in enumerate(snapshots):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(range(len(snap)), snap, color="#4C78A8")
        ax.set_title(f"{algo_name} – passo {i+1}/{len(snapshots)}")
        ax.set_xticks([])
        ax.set_yticks([])
        fig.tight_layout()
        fig.canvas.draw()
        # Converte canvas em array RGB
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(image)
        plt.close(fig)
    return frames

# 2) Algoritmos que coletam snapshots

def bubble_sort_with_snaps(a):
    arr = a[:]  # copia
    n = len(arr)
    snaps = []
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            if j % max(1, n // 10) == 0:  # amostra snapshots para não gerar frames demais
                snaps.append(arr[:])
        if not swapped:
            snaps.append(arr[:])
            break
    # garante snapshot final
    if not snaps or snaps[-1] != arr:
        snaps.append(arr[:])
    return snaps

def quick_sort_with_snaps(a):
    arr = a[:]
    snaps = []

    def partition(lo, hi):
        pivot = arr[(lo + hi) // 2]
        i, j = lo, hi
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                snaps.append(arr[:])
        return i, j

    def qs(lo, hi, depth=0):
        if lo >= hi:
            return
        i, j = partition(lo, hi)
        if lo < j:
            qs(lo, j, depth + 1)
        if i < hi:
            qs(i, hi, depth + 1)

    qs(0, len(arr) - 1)
    if not snaps or snaps[-1] != sorted(a):
        snaps.append(sorted(a))
    return snaps

def merge_sort_with_snaps(a):
    arr = a[:]
    snaps = []

    def merge(left, right, l, r):
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]; i += 1
            else:
                arr[k] = right[j]; j += 1
            k += 1
            if k % max(1, len(arr)//15) == 0:
                snaps.append(arr[:])
        while i < len(left):
            arr[k] = left[i]; i += 1; k += 1
            if k % max(1, len(arr)//15) == 0:
                snaps.append(arr[:])
        while j < len(right):
            arr[k] = right[j]; j += 1; k += 1
            if k % max(1, len(arr)//15) == 0:
                snaps.append(arr[:])

    def ms(l, r):
        if l >= r:
            return
        m = (l + r) // 2
        ms(l, m)
        ms(m + 1, r)
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        merge(left, right, l, r)

    ms(0, len(arr) - 1)
    snaps.append(arr[:])
    return snaps

# 3) Dataset e geração dos GIFs
random.seed(42)
n = 50
base = list(range(1, n + 1))
random.shuffle(base)

plot_bars(base, "Dataset inicial (embaralhado)", "dataset_inicial.png")

# Bubble
bubble_snaps = bubble_sort_with_snaps(base)
bubble_frames = to_frames(base, bubble_snaps, "Bubble Sort")
imageio.mimsave("bubble.gif", bubble_frames, duration=0.15)

# Quick
quick_snaps = quick_sort_with_snaps(base)
quick_frames = to_frames(base, quick_snaps, "Quick Sort")
imageio.mimsave("quick.gif", quick_frames, duration=0.15)

# Merge
merge_snaps = merge_sort_with_snaps(base)
merge_frames = to_frames(base, merge_snaps, "Merge Sort")
imageio.mimsave("merge.gif", merge_frames, duration=0.15)

# 4) Impressão de Big-O resumido
print("Complexidades (tempo | espaço):")
print("Bubble Sort: best O(n), average O(n^2), worst O(n^2) | space O(1), estável")
print("Quick Sort: best/avg O(n log n), worst O(n^2) | space O(log n) recursão, não estável (clássico)")
print("Merge Sort: best/avg/worst O(n log n) | space O(n) em arrays, estável")
print("Extra: Heap Sort avg/worst O(n log n), space O(1), não estável")