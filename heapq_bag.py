import time
import sys
import heapq


# Get max price of items in bag
def get_max_bag_price(items: list, bag: int) -> float:

    # Add part price for each item
    # We use -price / col to reverse 2n priority order with min in top and make -max in top
    items = [(-price / col, col) for price, col in items]

    # Create from [(part_price, count), (part_price, count), ....] to 2n priority order with min in top
    heapq.heapify(items)

    # Store points
    result_wight = 0

    while items and bag:
        part_price, count = heapq.heappop(items)
        max_size = min(bag, count)
        result_wight += -part_price * max_size
        bag -= max_size

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


def test():
    assert get_max_bag_price([(60, 20)], 0) == 0.0
    assert get_max_bag_price([(60, 20)], 25) == 60.0
    assert get_max_bag_price([(60, 20), (0, 100)], 25) == 60.0
    assert get_max_bag_price([(60, 20), (50, 50)], 25) == 60.0 + 5.0
    assert get_max_bag_price([(60, 20), (100, 50), (120, 30)], 50) == 180.0

    from random import randint

    # Get start time
    start = time.time()

    for _ in range(1000):
        n = randint(1, 1000)
        bag = randint(0, 2 * 10**6)
        items = []

        for i in range(n):
            items.append((randint(0, 2 * 10**6), randint(1, 2 * 10**6)))

        get_max_bag_price(items, bag)

    # Show execution time
    print('Time for 1000 tests: ', time.time() - start, 's')


def main():

    # Get data from file Input
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    items_length, bag = next(reader)
    items = list(reader)

    # Check correct items length
    assert len(items) == items_length

    # Get start time
    start = time.time()

    # Execute function
    result_gold = get_max_bag_price(items, bag)

    # Print result
    print('{:.3f}'.format(result_gold))

    # Show execution time
    print('Time: ', time.time() - start, 's')


if __name__ == "__main__":
    # main()
    test()
