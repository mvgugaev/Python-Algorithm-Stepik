import time

# Задача: По данному числу 1 <= n <=10^9 найдите максимальное число k,
# для которого nn можно представить как сумму k различных натуральных слагаемых.
# Выведите в первой строке число k, во второй — k слагаемых.

# Input:
# 6
# 120 30
# Output:
# 3
# 1 2 3
# Time:  4.935264587402344e-05 s


def main():
    n = int(input())

    # Get start time
    start = time.time()

    result, part = [], 1

    while n != 0:
        while part * 2 >= n and part != n:
            part += 1

        result.append(part)
        n -= part

        part += 1

    print(str(len(result)) + '\n' + ' '.join([str(i) for i in result]))

    # Show time
    print('Time: ', time.time() - start, 's')


if __name__ == "__main__":
    main()
