import sys

# Задача: Дано целое число 1 ≤ n ≤ 10^5 и массив A[1…n],
# содержащий неотрицательные целые числа, не превосходящие 10^9.
# Найдите наибольшую невозрастающую подпоследовательность в A.
# В первой строке выведите её длину k, во второй —
# её индексы 1 ≤ i1 ​< i2 ​< … < ik ​≤ n (таким образом, A[i1] ≥ A[i2] ≥ … ≥ A[in]).

# Input:
# 5
# 5 3 4 4 2

# Output
# 4
# 1 3 4 5


def get_max_sequence_len(array: list, n: int) -> list:

    # Infinitive
    inf = 10 ** 10

    # Max number of non decrease sequence length i
    # In array [5, 3, 4, 4, 2, 5, 9] max number of sequence len 1 = 9 [sec: 9],
    # max number of sequence len 2 = 5 [sec: 5 5], len 3 = 4 (5 4 4)
    # len 4 = 2 (5 4 4 2) => for [5, 3, 4, 4, 2, 5, 9] -> [9, 5, 4, 2]
    # For correct work binary search we add -Inf to 0 position and Inf to other position
    # Start: max_sequence_end_number = [Inf, -Inf, -Inf, -Inf, -Inf, -Inf, -Inf, -Inf]
    # End: max_sequence_end_number = [Inf, 9, 5, 4, 2, -Inf, -Inf, -Inf]
    max_sequence_end_number = [inf] + [-inf] * n

    # Previous sequence node
    prev_sequence_node = [] * (n + 1)

    # Fill max_sequence_end_number and prev_sequence_node
    for i in range(n):
        left, right = 0, n

        while right - left > 1:

            middle = (left + right) // 2

            if max_sequence_end_number[middle] < array[i]:
                right = middle
            else:
                left = middle

        max_sequence_end_number[right] = array[i]
        prev_sequence_node.append([right, i, array[i]])

    # Find correct end of array max_sequence_end_number
    i = n
    while max_sequence_end_number[i] == -inf:
        i = i - 1

    # Restore correct array from prev_sequence_node
    counter = len(max_sequence_end_number[1: i + 1])
    result_array = []

    for element in reversed(prev_sequence_node):
        if element != -1 and element[0] == counter:
            counter -= 1
            result_array.append(element[1] + 1)

    return list(reversed(result_array))


def main():
    n = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    result = get_max_sequence_len(array, n)
    print(len(result), '\n', ' '.join(map(str, result)), end='', sep='')


if __name__ == '__main__':
    main()
