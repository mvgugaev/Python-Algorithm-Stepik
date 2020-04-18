import time


# Get Pisano array
def get_pisano_array(n: int, m: int) -> list:

    pisano = [0]

    if m == 1:
        return pisano

    pisano.append(1)

    if n <= 1:
        return pisano

    pisano.append((pisano[len(pisano) - 1] + pisano[len(pisano) - 2]) % m)

    while not (pisano[- 1] == 1 and pisano[- 2] == 0):
        pisano.append((pisano[len(pisano) - 1] + pisano[len(pisano) - 2]) % m)

    return pisano[:-2]


def fib_mod(n, m):

    pisano = get_pisano_array(n, m)

    return pisano[n % len(pisano)]


# Задача: Даны целые числа 1 <= n <= 10^18 и 2 <= m <= 10^5,
# необходимо найти остаток от деления n-го числа Фибоначчи на mm.

# Input: 1000000000 444
# Output:
# 339
# Time:  0.0002770423889160156 s


def main():
    n, m = map(int, input().split())

    # Get start time
    start = time.time()

    # Execute function
    print(fib_mod(n, m))

    # Show time
    print('Time: ', time.time() - start, 's')


if __name__ == "__main__":
    main()