import random
import sys

# Задача: В первой строке задано два целых числа 1 ≤ n ≤ 50000 500001 ≤ m ≤ 50000 —
# количество отрезков и точек на прямой, соответственно. Следующие nn строк содержат по два целых
# числа a(i) и b(i) — координаты концов отрезков.Последняя строка содержит m целых чисел — координаты точек.
# Все координаты не превышают 10^8 по модулю. Точка считается принадлежащей отрезку, если
# она находится внутри него или на границе. Для каждой точки в порядке появления во
# вводе выведите, скольким отрезкам она принадлежит.

# Input:
# 2 3
# 0 5
# 7 10
# 1 6 11
# Output:
# 1 0 0


# Partition array [start, end), [   <    |  =   |    >    ]
def partition(array: list, start: int, end: int):

    # Array len will be > 1
    if end - start >= 2:

        m = random.randint(start, end - 1)
        i, j, p = start + 1, start, start

        array[start], array[m] = array[m], array[start]

        for i in range(start + 1, end):
            if array[i] < array[start]:
                p += 1
                j += 1
                array[i], array[j] = array[j], array[i]
                array[p], array[j] = array[j], array[p]
            elif array[i] == array[start]:
                j += 1
                array[i], array[j] = array[j], array[i]

        array[start], array[p] = array[p], array[start]

        return j, p

    return -1, -1


# Sort [start, end), re
def quick_sort(array: list, start: int, end: int) -> None:

    i, p = partition(array, start, end)

    if i != -1:
        quick_sort(array, start, p)
        quick_sort(array, i + 1, end)


# [start, end)
def get_count_equal_or_less(array: list, point: int, start: int, end: int):

    if end - start >= 2:

        center = int((start + end)/2)

        if point >= array[center]:
            return center - start + get_count_equal_or_less(array, point, center, end)

        return get_count_equal_or_less(array, point, start, center)

    elif array[start] <= point:
        return 1

    return 0


# [start, end)
def get_count_less(array: list, point: int, start: int, end: int):

    if end - start >= 2:

        center = int((start + end)/2)

        if point > array[center]:
            return center - start + get_count_less(array, point, center, end)

        return get_count_less(array, point, start, center)

    elif array[start] < point:
        return 1

    return 0


def main():
    n, _ = map(int, sys.stdin.readline().split())

    ranges_x, ranges_y = [], []

    for i in range(n):
        x, y = map(int, input().split())
        ranges_x.append(x)
        ranges_y.append(y)

    points = list(map(int, sys.stdin.readline().split()))

    quick_sort(ranges_x, 0, n)
    quick_sort(ranges_y, 0, n)

    for point in points:
        print(get_count_equal_or_less(ranges_x, point, 0, n) - get_count_less(ranges_y, point, 0, n), end=' ')


if __name__ == '__main__':
    main()
