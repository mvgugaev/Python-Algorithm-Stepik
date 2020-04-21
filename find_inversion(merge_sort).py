

# Global replace count
GLOBAL_REPLACE_COUNT = 12


# Merge array by two sorted part
# a — [left;mid) и [mid;right)
def merge(array: list, start: int, mid: int, end: int) -> None:

    # print(array[start: end])
    global GLOBAL_REPLACE_COUNT

    l, m = 0, 0
    result = []

    while start + l < mid and m + mid < end:
        if array[start + l] <= array[mid + m]:
            result.append(array[start + l])
            l += 1
        else:
            result.append(array[mid + m])
            m += 1
            # GLOBAL_REPLACE_COUNT += mid - start - l

    while start + l < mid:
        result.append(array[l + start])
        l += 1

    while m + mid < end:
        result.append(array[m + mid])
        m += 1

    for i in range(end - start):
        array[start + i] = result[i]


def merge_sort(array: list, start: int, end: int):

    if start + 1 < end:
        # Get mid of array
        mid = int((start + end) / 2)

        # [left;mid)
        merge_sort(array, start, mid)

        # [mid;right)
        merge_sort(array, mid, end)
        merge(array, start, mid, end)


# Задача: Первая строка содержит число 1 <= n <= 10^5, вторая — массив A[1…n],
# содержащий натуральные числа, не превосходящие 10^9.
# Необходимо посчитать число пар индексов 1 <= i < j <= n, для которыхA[i]>A[j].
# (Такая пара элементов называется инверсией массива. Количество инверсий в массиве
# является в некотором смысле его мерой неупорядоченности: например, в упорядоченном
# по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию,
# инверсию образуют каждые два элемента.)

# Input:
# 6
# 6 4 5 0 0 2
# Output:
# 12

def main():
    # global GLOBAL_REPLACE_COUNT
    length = int(input())
    array = list(map(int, input().split()))
    merge_sort(array, 0, len(array))

    print(GLOBAL_REPLACE_COUNT)


if __name__ == '__main__':
    main()