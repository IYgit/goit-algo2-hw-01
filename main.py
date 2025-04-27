import random

def find_min_max(arr):
    # Базовий випадок: якщо масив містить один елемент, повертаємо цей елемент як мінімум і максимум
    if len(arr) == 1:
        return arr[0], arr[0]

    # Розділяємо масив на дві частини
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Повертаємо мінімум і максимум серед двох частин
    return min(left_min, right_min), max(left_max, right_max)



def test_1():
    # Приклад масиву
    arr = [3, 1, 7, 5, 9, 2, 4]

    # Викликаємо функцію find_min_max
    min_value, max_value = find_min_max(arr)

    # Виводимо результат
    print(f"Мінімум: {min_value}, Максімум: {max_value}")



def quick_select(arr, left, right, k):
    """
    Функція для пошуку k-го найменшого елемента в несортованому масиві.

    :param arr: список чисел
    :param left: лівий індекс масиву
    :param right: правий індекс масиву
    :param k: позиція шуканого елемента (1-based)
    :return: k-й найменший елемент
    """
    if left == right:
        return arr[left]

    # Вибір випадкового опорного елемента
    pivot_index = random.randint(left, right)
    pivot_index = partition(arr, left, right, pivot_index)

    # Позиція опорного елемента
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, right, k)


def partition(arr, left, right, pivot_index):
    """
    Функція для перестановки елементів з урахуванням опорного елемента.

    :param arr: список чисел
    :param left: лівий індекс масиву
    :param right: правий індекс масиву
    :param pivot_index: індекс опорного елемента
    :return: новий індекс опорного елемента
    """
    pivot_value = arr[pivot_index]

    # Перестановка опорного елемента в кінець масиву
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # Переміщаємо опорний елемент на його правильну позицію
    arr[right], arr[store_index] = arr[store_index], arr[right]

    return store_index


def test_2():
    # Приклад масиву
    arr = [3, 1, 7, 5, 9, 2, 4]
    k = 3

    # Викликаємо Quick Select для пошуку k-го найменшого елемента
    result = quick_select(arr, 0, len(arr) - 1, k - 1)  # k-1 для 0-based індексації
    print(f"{k}-й найменший елемент: {result}")


def main():
    test_1()
    test_2()

# Запуск програми
if __name__ == "__main__":
    main()
