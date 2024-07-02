"""
Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
"""
import random
from typing import List


def counting_sort(array: List[int]) -> List[int]:
    """
    Сортировка подсчетам

    :param array: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    max_val = max(array)

    # Создаем массив подсчета
    count = [0] * (max_val + 1)  # список заполненный нулями

    sorted_arr: list[int] = []

    # Подсчитываем количество вхождений каждого числа
    for i in array:
        count[i] += 1

    for ind, val in enumerate(count):
        sorted_arr.extend([ind] * val)

    return sorted_arr


if __name__ == "__main__":
    # Создаем массив из 10**6 случайных чисел, random.randint(13, 25)  с диапазоном
    arr = [random.randint(13, 25) for _ in range(10 ** 6)]
    print(counting_sort(arr))
