import sys

# Задача: Вычислите расстояние редактирования двух данных непустых строк длины
# не более 10^2, содержащих строчные буквы латинского алфавита.

# Input
# short
# ports

# Output
# 3


def get_editing_distance(first: str, second: str) -> int:

    if len(first) == 0 or len(second) == 0:
        return max(len(second), len(first))

    second_array = list(range(len(first) + 1))
    current_array = [1] + [0] * len(first)

    for i in range(1, len(second) + 1):

        # fill cell
        for k in range(1, len(first) + 1):
            current_array[k] = min(second_array[k] + 1, (second_array[k - 1] + int(first[k - 1] != second[i - 1])), current_array[k - 1] + 1)

        # Array move
        second_array = current_array
        current_array = [i + 1] + [0] * len(first)

    return second_array[len(first)]


def main():
    first = sys.stdin.readline()
    second = sys.stdin.readline()
    print(get_editing_distance(first.strip(), second.strip()))


if __name__ == '__main__':
    main()
