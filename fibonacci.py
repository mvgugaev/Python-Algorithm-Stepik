import time


# Base line method (use list)
def find_fib_list(n):

    data_list = [0, 1]

    if n < len(data_list):
        return data_list[n]

    while len(data_list) - 1 != n:
        data_list.append(data_list[len(data_list) - 2] + data_list[len(data_list) - 1])

    return data_list[-1]


# Base line method (use vars for n - 1 and n - 2)
def find_fib_var(n):

    before_value, last_value = 0, 1

    if n == 0:
        return 0

    if n == 1:
        return 1

    for _ in range (1, n):
        before_value, last_value = last_value, before_value + last_value

    return last_value


# Input: 100000
# Output:
# 2597406934.....
# Time:  0.37818288803100586 s
# 2597406934.....
# Time:  0.10604596138000488 s

def main():
    n = int(input())

    # Get start time first method
    start = time.time()

    # Execute function
    print(find_fib_list(n))

    # Show time
    print('Time: ', time.time() - start, 's')

    # Get start time second method
    start = time.time()

    # Execute function
    print(find_fib_var(n))

    # Show time
    print('Time: ', time.time() - start, 's')


if __name__ == "__main__":
    main()