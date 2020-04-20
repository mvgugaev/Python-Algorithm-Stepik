def bin_search_with_index_equal(array: list) -> bool:
    start, end = 0, len(array) - 1

    while start <= end:

        # Get center of result
        center = int((start + end) / 2)

        if center == array[center]:
            return True
        elif center < array[center]:
            end = center - 1
        else:
            start = center + 1

    return False


def main():
    array = list(map(int, input().split()))
    print(bin_search_with_index_equal(array))


if __name__ == '__main__':
    main()
