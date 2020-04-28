import sys


# Задача: Дано целое число 1≤n≤10^3 и массив A[1…n] натуральных чисел,
# не превосходящих 2⋅10^9 . Выведите максимальное 1≤k≤n, для которого найдётся
# подпоследовательность 1 ≤ i1 ​< i2 ​< … < ik ​≤ n длины k, в которой каждый элемент
# делится на предыдущий (формально: для  всех 1 ≤ j < k, A[ij] | A[i{j+1}]).

# Input:
# 4
# 3 6 7 12

# Output
# 3

def get_max_sequence_len(array: list, n: int) -> int:

    # Max len sequence
    max_len = 0

    # Array of sequence length
    len_arr = [-1] * n

    for i in range(0, n):

        # Set len 1 for first element
        len_arr[i] = 1

        for p in range(i - 1, -1, -1):
            if array[p] != 0 and array[i] >= array[p] and array[i] % array[p] == 0 and len_arr[p] > (len_arr[i] - 1):
                len_arr[i] = len_arr[p] + 1

        # Set max len
        if len_arr[i] > max_len:
            max_len = len_arr[i]

    return max_len


def main():
    n = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    print(get_max_sequence_len(array, n))


if __name__ == '__main__':
    main()
