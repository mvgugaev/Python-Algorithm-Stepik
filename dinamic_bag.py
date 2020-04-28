import sys


# items = [[width, price], ......]
def find_max_bag_width(bag_width: int, item_count: int, items: list) -> int:

    # data_matrix = [[0] * (bag_width + 1)] * (item_count + 1)
    data_matrix = [[0] * (bag_width + 1) for item in range(item_count + 1)]

    for i in range(1, item_count + 1):
        for w in range(1, bag_width + 1):
            data_matrix[i][w] = data_matrix[i - 1][w]

            # If we can store this item
            if w >= items[i - 1][0]:
                # print(i, w)
                data_matrix[i][w] = max(data_matrix[i][w], data_matrix[i - 1][w - items[i - 1][0]] + items[i - 1][1])

    # for item in data_matrix:
    #     print(item)

    return data_matrix[item_count][bag_width]


def main():
    bag_width, item_count = map(int, sys.stdin.readline().split())
    items = [[width, width] for width in map(int, sys.stdin.readline().split())]
    print(find_max_bag_width(bag_width, item_count, items))


if __name__ == '__main__':
    main()
