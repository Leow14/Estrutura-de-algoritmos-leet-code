# Visualização do Quicksort com matplotlib (Lomuto partition)
# pip install matplotlib

import random
import time
import matplotlib.pyplot as plt
from matplotlib import colors

# Configurações
N = 30                 # tamanho do array
DELAY = 0.05           # atraso entre frames (segundos)
RANDOM_SEED = 42       # defina None para aleatório a cada execução

if RANDOM_SEED is not None:
    random.seed(RANDOM_SEED)

arr = list(range(1, N + 1))
random.shuffle(arr)

# Cores
C_NORMAL = "#4C78A8"
C_PIVOT  = "#F58518"
C_SWAP   = "#E45756"
C_OK     = "#72B7B2"   # elementos já confirmados <= pivô durante a varredura
C_RANGE  = "#B5B5B5"   # fora do subarray atual

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(range(len(arr)), arr, color=C_NORMAL, align="center")

ax.set_title("Quicksort - Visualização (Lomuto partition)", fontsize=14)
ax.set_xlabel("Índice")
ax.set_ylabel("Valor")
ax.set_xlim(-0.5, len(arr) - 0.5)
ax.set_ylim(0, max(arr) * 1.1)

text_step = ax.text(0.02, 0.95, "", transform=ax.transAxes, va="top", fontsize=11)
text_info = ax.text(0.02, 0.88, "", transform=ax.transAxes, va="top", fontsize=10)

def draw(current_low=None, current_high=None, pivot_idx=None, i=None, j=None, note=""):
    # Atualiza alturas
    for idx, bar in enumerate(bars):
        bar.set_height(arr[idx])

    # Reseta cores
    for idx, bar in enumerate(bars):
        bar.set_color(C_RANGE)

    # Marca o subarray atual
    if current_low is not None and current_high is not None:
        for idx in range(current_low, current_high + 1):
            bars[idx].set_color(C_NORMAL)

    # Marca elementos <= pivô já posicionados (até i)
    if i is not None and current_low is not None:
        for idx in range(current_low, i + 1):
            bars[idx].set_color(C_OK)

    # Marca pivot
    if pivot_idx is not None:
        bars[pivot_idx].set_color(C_PIVOT)

    # Marca j (elemento em inspeção)
    if j is not None:
        bars[j].set_color(C_SWAP)

    text_step.set_text(f"Subarray atual: [{current_low}, {current_high}]  |  pivot: {pivot_idx}  |  i: {i}  |  j: {j}")
    text_info.set_text(note)

    plt.pause(DELAY)

def partition(low, high):
    pivot = arr[high]
    i = low - 1
    draw(low, high, pivot_idx=high, i=i, j=None, note=f"Iniciando partition com pivô arr[{high}]={pivot}")

    for j in range(low, high):
        draw(low, high, pivot_idx=high, i=i, j=j, note=f"Comparando arr[{j}]={arr[j]} com pivô={pivot}")
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw(low, high, pivot_idx=high, i=i, j=j, note=f"Trocando arr[{i}] e arr[{j}] (<= pivô)")

    # Coloca pivô na posição correta (i+1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw(low, high, pivot_idx=i + 1, i=i, j=high, note=f"Posiciona pivô em {i+1}")
    return i + 1

def quicksort_recursive(low, high):
    if low < high:
        pi = partition(low, high)
        quicksort_recursive(low, pi - 1)
        quicksort_recursive(pi + 1, high)
    else:
        # Pequeno toque visual quando a partição é de 0/1 elemento
        draw(low, high, note="Subarray de tamanho <= 1: já ordenado.")

def run():
    draw(note="Array embaralhado. Iniciando quicksort...")
    quicksort_recursive(0, len(arr) - 1)
    draw(note="Concluído! Array ordenado.")
    plt.show()

if __name__ == "__main__":
    run()