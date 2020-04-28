import sys


def step_calculate(n: int):

    min_operations = [-1]
    operations = 0
    inf = 10 ** 10

    for i in range(1, n + 1):
        x, y, z = min_operations[i - 1] + 1, inf, inf

        if i % 2 == 0:
            y = min_operations[i // 2] + 1

        if i % 3 == 0:
            z = min_operations[i // 3] + 1

        min_operations.append(min(x, y, z))

    # print(min_operations)
    # print(list(range(n + 1)))

    result = [n]
    num = n
    operations_count = min_operations[-1]

    for i in range(n - 1, -1, -1):

        # print(i, operations_count, num)

        if min_operations[i] == operations_count - 1 and (num / 3 == i or num / 2 == i or num == i + 1):
            result.append(i)
            operations_count -= 1
            num = i

    return min_operations[-1], reversed(result[:-1])


def main():
    n = int(sys.stdin.readline())
    count, result = step_calculate(n)
    print(count)
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
