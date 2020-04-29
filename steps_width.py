import sys

# Задача: Даны число 1 ≤ n ≤ 10^2 ступенек лестницы и целые числа
# -10^4 ≤ a1 ​, … , an ​≤ 10^4, которыми помечены ступеньки. Найдите максимальную сумму,
# которую можно получить, идя по лестнице снизу вверх (от нулевой до nn-й ступеньки),
# каждый раз поднимаясь на одну или две ступеньки.

# Input:
# 3
# -1 2 1

# Output
# 3


# steps = [-1, 2, 2, 4, -1] - width for each step
def find_steps_max_width(steps: list, n: int) -> int:

    # add zero step to array
    steps = [0] + steps
    position = 2

    l, x = 0, steps[1]

    while position < n + 1:
        l, x = x, max(l, x) + steps[position]
        position += 1

    return x


def main():
    n = int(sys.stdin.readline())
    steps = list(map(int, sys.stdin.readline().split()))
    print(find_steps_max_width(steps, n))


if __name__ == '__main__':
    main()
