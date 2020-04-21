

# Merge array by two sorted part
# a — [left;mid) и [mid;right)
def merge(array: list, start: int, mid: int, end: int) -> None:

    l, m = 0, 0
    result = []

    while start + l < mid and m + mid < end:
        if array[start + l] <= array[mid + m]:
            result.append(array[start + l])
            l += 1
        else:
            result.append(array[mid + m])
            m += 1

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

# Input:
# 6
# 6 4 5 0 0 2
# Output:
# [0, 0, 2, 4, 5, 6]


def main():
    length = int(input())
    array = list(map(int, input().split()))
    merge_sort(array, 0, len(array))

    print(array)


if __name__ == '__main__':
    main()