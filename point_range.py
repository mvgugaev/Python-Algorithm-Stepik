import random
import time


# Ranges quick sort with [[x, y], [x, y], [x, y], ...] by Y
def quick_sort_ranges(array: list, sort_start: int, sort_end: int) -> None:

    if sort_start >= sort_end:
        return

    first_pointer, last_pointer = sort_start, sort_end
    pivot = array[random.randint(sort_start, sort_end)][1]

    while first_pointer <= last_pointer:

        while array[first_pointer][1] < pivot:
            first_pointer += 1

        while array[last_pointer][1] > pivot:
            last_pointer -= 1

        if first_pointer <= last_pointer:
            array[first_pointer], array[last_pointer] = array[last_pointer], array[first_pointer]

            first_pointer, last_pointer = first_pointer + 1, last_pointer - 1

    quick_sort_ranges(array, sort_start, last_pointer)
    quick_sort_ranges(array, first_pointer, sort_end)


# Get optimal points count
def get_ranges_layer_points_min_length(ranges: list) -> list:

    # Sort ranges array
    quick_sort_ranges(ranges, 0, len(ranges) - 1)

    # Store points
    points_array = []

    for single_range in ranges:
        if len(points_array) == 0 or single_range[0] > points_array[-1]:
            points_array.append(single_range[1])

    return points_array

# Задача: По данным n отрезкам необходимо найти множество точек минимального размера,
# для которого каждый из отрезков содержит хотя бы одну из точек.
# В первой строке дано число 1 < n < 100 отрезков. Каждая из последующих n строк содержит
# по два числа 0 <= l <= r <= 10^9, задающих начало и конец отрезка.
# Выведите оптимальное число mm точек и сами mm точек.
# Если таких множеств точек несколько, выведите любое из них.

# Input:
# 4
# 4 7
# 1 3
# 2 5
# 5 6
# Output:
# 2
# 3 6
# Time:  0.6745350360870361 s


def main() -> None:
    range_length = int(input())

    # Get start time
    start = time.time()

    ranges = []

    # Input ranges
    for _ in range(0, range_length):
        ranges.append([int(i) for i in input().split(' ')])

    points_result = get_ranges_layer_points_min_length(ranges)

    print(len(points_result))

    for point in points_result:
        print(point, end=' ')

    print('\n')

    # Show time
    print('Time: ', time.time() - start, 's')


if __name__ == "__main__":
    main()
