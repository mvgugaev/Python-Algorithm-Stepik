

# Classic non-recursive binary search
def bin_search(array: list, find: int) -> int:
    start, end = 0, len(array) - 1

    while start <= end:

        # Get center of result
        center = int((start + end) / 2)

        if find == array[center]:
            return center
        elif find > array[center]:
            start = center + 1
        else:
            end = center - 1

    return -2


# Задача: В первой строке даны целое число 1≤n≤10^5и массив A[1…n] из n различных натуральных чисел,
# не превышающих 10^9, в порядке возрастания, во второй — целое число 1≤k≤10^5
# и k натуральных чисел b1....bk, не превышающих 10^9. Для каждого i от 1 до k
# необходимо вывести индекс 1 ≤ j ≤ n, для которого A[j] = bi, или -1, если такого j нет.

# Input:
# 5 1 5 8 12 13
# 5 8 1 23 1 11
# Output
# 3 1 -1 1 -1

def main():
    array_len, *array = map(int, input().split())
    find_len, *find_array = map(int, input().split())

    for find in find_array:
        print(bin_search(array, find) + 1, end=" ")


if __name__ == '__main__':
    main()
