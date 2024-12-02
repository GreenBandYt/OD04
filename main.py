# O(1) - константная сложность алгоритма

def get_element(array, index):
    return array[index]

array = [1, 2, 3, 4, 5]
print(get_element(array, 4))

# O(n) - линейная сложность алгоритма

def line_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

array = [10, 20, 30, 40, 50]
print(line_search(array, 30))
print(line_search(array, 60))

# O(log n) - логарифмическая сложность

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(array, 7))
print(binary_search(array, 11))



# O(n^2) - квадратичная сложность алгоритма

# O(n^3) - кубическая сложность алгоритма

# O(2^n) - экспоненциальная сложность

# O(n!) - факториальная сложность



# O(nlog n) - линейно-логарифмическая сложность

# O(n^log n) - квадратично-логарифмическая сложность
