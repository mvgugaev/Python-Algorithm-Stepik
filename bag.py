import random
import time
import sys


# Bag items quick sort with [[x, y, z], [x, y, z], [x, y, z], ...] by Z
def quick_sort_items(array: list, sort_start: int, sort_end: int) -> None:

    if sort_start >= sort_end:
        return

    first_pointer, last_pointer = sort_start, sort_end
    pivot = array[random.randint(sort_start, sort_end)][2]

    while first_pointer <= last_pointer:

        while array[first_pointer][2] < pivot:
            first_pointer += 1

        while array[last_pointer][2] > pivot:
            last_pointer -= 1

        if first_pointer <= last_pointer:
            array[first_pointer], array[last_pointer] = array[last_pointer], array[first_pointer]

            first_pointer, last_pointer = first_pointer + 1, last_pointer - 1

    quick_sort_items(array, sort_start, last_pointer)
    quick_sort_items(array, first_pointer, sort_end)


# Get optimal points count
def get_max_bag_gold(items: list, bag: int) -> float:

    # Add part price for each item
    items = [item + [item[0] / item[1]] for item in items]

    # Sort items array
    quick_sort_items(items, 0, len(items) - 1)

    # Store points
    result_wight = 0

    for item in reversed(items):
        if item[1] < bag:
            result_wight += item[1] * item[2]
            bag -= item[1]
        else:
            result_wight += bag * item[2]
            break

    return result_wight

# Первая строка содержит количество предметов 1 <= n <= 10^3
# и вместимость рюкзака 0 <= W <= 2 * 10^6. Каждая из следующих nn строк
# задаёт стоимость 0 <= Ci <= 2 * 10^6 и объём 0 < Wi <= 2 * 10^6
# предмета (n, W, Ci, Wi — целые числа). Выведите максимальную стоимость частей
# предметов (от каждого предмета можно отделить любую часть, стоимость и объём при
# этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее
# трёх знаков после запятой.

# Run: python3 bag.py < test_data/bag.txt (file mode)
# Input:
# 3 50
# 60 20
# 100 50
# 120 30
# Output:
# 180.000
# Time:  0.32701897621154785 s


# Get data from file like
# python3 bag.py < test_data/bag.txt
# reader - generator, which get data from sys.stdin
def get_data_from_file():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    items_length, bag = next(reader)
    items = list(reader)

    return items_length, bag, items


# Get data from terminal input
def get_data_from_terminal():
    items_length, bag = [int(i) for i in input().split()]

    items = []

    # Input ranges
    for i in range(0, items_length):
        items.append([int(i) for i in input().split()])

    return items_length, bag, items


def main():

    # Use file As input
    items_length, bag, items = get_data_from_file()

    # Use terminal As input
    # items_length, bag, items = get_data_from_terminal()

    assert len(items) == items_length

    # Get start time
    start = time.time()

    # Execute function
    result_gold = get_max_bag_gold(items, bag)

    print('{:.3f}'.format(result_gold))
    #
    # Show time
    print('Time: ', time.time() - start, 's')


if __name__ == "__main__":
    main()
