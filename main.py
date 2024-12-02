import random
import timeit

# Генерация массивов разного размера
small_array = [random.randint(-1000, 1000) for _ in range(100)]       # Маленький массив
medium_array = [random.randint(-1000, 1000) for _ in range(1000)]    # Средний массив
large_array = [random.randint(-1000, 1000) for _ in range(10000)]    # Большой массив

print("Массивы сгенерированы:")
print(f"Маленький массив (100 элементов): {small_array[:10]} ...")
print(f"Средний массив (1,000 элементов): {medium_array[:10]} ...")
print(f"Большой массив (10,000 элементов): {large_array[:10]} ...")

# Пузырьковая сортировка
def bubble_sort(arr):
    """
    Пузырьковая сортировка.
    Временная сложность:
        - Лучший случай: O(n)
        - Средний случай: O(n^2)
        - Худший случай: O(n^2)
    Пространственная сложность: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Быстрая сортировка
def quick_sort(arr):
    """
    Быстрая сортировка.
    Временная сложность:
        - Лучший случай: O(n log n)
        - Средний случай: O(n log n)
        - Худший случай: O(n^2)
    Пространственная сложность: O(n) (из-за рекурсивных вызовов и дополнительных списков)
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)

# Сортировка выбором
def selection_sort(arr):
    """
    Сортировка выбором.
    Временная сложность:
        - Лучший случай: O(n^2)
        - Средний случай: O(n^2)
        - Худший случай: O(n^2)
    Пространственная сложность: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Сортировка вставками
def insertion_sort(arr):
    """
    Сортировка вставками.
    Временная сложность:
        - Лучший случай: O(n) (массив отсортирован, только проверка)
        - Средний случай: O(n^2)
        - Худший случай: O(n^2)
    Пространственная сложность: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Функция для замера времени
def measure_time_with_timeit(func, arr):
    """
    Замер времени выполнения сортировки.
    :param func: Функция сортировки
    :param arr: Массив для сортировки
    :return: Время выполнения в секундах
    """
    return timeit.timeit(lambda: func(arr.copy()), number=1)

# Сравнение алгоритмов для массивов разного размера
results = []

for array, size in zip([small_array, medium_array, large_array], ["100", "1000", "10000"]):
    results.append({
        "size": size,
        "bubble_sort": measure_time_with_timeit(bubble_sort, array),
        "quick_sort": measure_time_with_timeit(quick_sort, array),
        "selection_sort": measure_time_with_timeit(selection_sort, array),
        "insertion_sort": measure_time_with_timeit(insertion_sort, array),
    })

# Вывод результатов
print("\nРезультаты сортировок (время выполнения в секундах):")
print(f"{'Размер массива':<15}{'Bubble Sort':<15}{'Quick Sort':<15}{'Selection Sort':<15}{'Insertion Sort':<15}")
for result in results:
    print(f"{result['size']:<15}{result['bubble_sort']:<15.6f}{result['quick_sort']:<15.6f}{result['selection_sort']:<15.6f}{result['insertion_sort']:<15.6f}")

# Итоговая таблица сложности
print("\nСложность алгоритмов:")
print(f"{'Алгоритм':<20}{'Лучший случай':<20}{'Средний случай':<20}{'Худший случай':<20}{'Пространство':<20}")
print(f"{'Bubble Sort':<20}{'O(n)':<20}{'O(n^2)':<20}{'O(n^2)':<20}{'O(1)':<20}")
print(f"{'Quick Sort':<20}{'O(n log n)':<20}{'O(n log n)':<20}{'O(n^2)':<20}{'O(n)':<20}")
print(f"{'Selection Sort':<20}{'O(n^2)':<20}{'O(n^2)':<20}{'O(n^2)':<20}{'O(1)':<20}")
print(f"{'Insertion Sort':<20}{'O(n)':<20}{'O(n^2)':<20}{'O(n^2)':<20}{'O(1)':<20}")
