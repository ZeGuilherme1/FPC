import numpy as np
import time
import matplotlib.pyplot as plt

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if (array[j] < array[min_idx]):
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

tamanhos = [100, 200, 400, 800, 1600]
tempos_bubble = []
tempos_selection = []
tempos_quick = []

for n in tamanhos:
    array = np.random.randint(0, 1000, size=n)

    bubble_array = array.copy()
    start_time = time.time()
    bubble_sort(bubble_array)
    tempos_bubble.append(time.time() - start_time)

    selection_array = array.copy()
    start_time = time.time()
    selection_sort(selection_array)
    tempos_selection.append(time.time() - start_time)

    quick_array = array.copy()
    start_time = time.time()
    quick_sort(quick_array)
    tempos_quick.append(time.time() - start_time)

plt.figure(figsize=(10, 6))
plt.loglog(tamanhos, tempos_bubble, label='Bubble Sort', marker='o')
plt.loglog(tamanhos, tempos_selection, label='Selection Sort', marker='o')
plt.loglog(tamanhos, tempos_quick, label='Quick Sort', marker='o')
plt.xlabel('Tamanho do vetor (N)')
plt.ylabel('Tempo (s)')
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.title('Desempenho dos Algoritmos de Ordenação')
plt.show()
