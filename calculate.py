import sys

# Задача: У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x:
# заменить x на 2x, 3x или x+1. По данному целому числу 1 ≤ n ≤ 10^5 определите минимальное число операций k,
# необходимое, чтобы получить n из 1. Выведите k и последовательность промежуточных чисел.

# Input
# 96234

# Output
# 14
# 1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234


# Calculate operations count and steps
def step_calculate(n: int):

    min_operations = [-1]
    inf = 10 ** 10

    for i in range(1, n + 1):
        x, y, z = min_operations[i - 1] + 1, inf, inf

        if i % 2 == 0:
            y = min_operations[i // 2] + 1

        if i % 3 == 0:
            z = min_operations[i // 3] + 1

        min_operations.append(min(x, y, z))

    result, num = [n], n
    operations_count = min_operations[-1]

    for i in range(n - 1, -1, -1):

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
