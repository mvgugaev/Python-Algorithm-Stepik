import sys

# Задача: Первая строка содержит число 1 ≤ n ≤ 10^4,
# вторая — n натуральных чисел, не превышающих 10.
# Выведите упорядоченную по неубыванию последовательность этих чисел.

# Input:
# 5
# 2 3 9 2 9
# Output
# 2 2 3 9 9


# Fast counting sort for small numbers <= 10
def counting_sort(array: list, n: int):

    b = [0] * 11
    result = [0] * n

    # Create counting array
    for number in array:
        b[number] += 1

    # Create point array
    for index in range(1, 11):
        b[index] += b[index - 1]

    for index in range(n - 1, -1, -1):
        result[b[array[index]] - 1] = array[index]
        b[array[index]] -= 1

    return result


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(' '.join(map(str, counting_sort(arr, n))))


if __name__ == '__main__':
    main()
