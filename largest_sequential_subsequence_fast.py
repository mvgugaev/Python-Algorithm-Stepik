import sys
import bisect


def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            r = mid - 1
        else:
            l = mid + 1
    return l


def get_max_sequence_len(array: list, n: int) -> list:

    inf = 10 ** 10

    F = [-inf] * (len(array) + 1)
    PREV = [-1] * (len(array) + 1)
    F[0] = inf

    for i in range(len(array)):
        left = 0
        right = len(array)
        while right - left > 1:

            middle = (left + right) // 2

            if F[middle] < array[i]:
                right = middle
            else:
                left = middle

        F[right] = array[i]
        PREV.append([right, i, array[i]])

    # print(F)

    i = n

    # print(F)

    while F[i] == -inf:
        i = i - 1

    # print('Result F:', F[1: i + 1])
    counter = len(F[1: i + 1])
    # print('Counter: ', counter)

    # print(PREV)
    # print(len(F))

    result_array = []

    for element in reversed(PREV):
        if element != -1 and element[0] == counter:
            counter -= 1
            result_array.append(element[1] + 1)

    return list(reversed(result_array))


def main():
    n = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    result = get_max_sequence_len(array, n)
    print(len(result))

    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()