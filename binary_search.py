def bin_search(array: list, find: int) -> int:
    start, end = 0, len(array) - 1

    while start <= end:

        # Get center of result
        center = int((start + end) / 2)

        if find == array[center]:
            return center
        elif find > array[center]:
            start = center + 1
        else:
            end = center - 1

    return -2


def main():
    array_len, *array = map(int, input().split())
    find_len, *find_array = map(int, input().split())

    for find in find_array:
        print(bin_search(array, find) + 1, end=" ")


if __name__ == '__main__':
    main()
