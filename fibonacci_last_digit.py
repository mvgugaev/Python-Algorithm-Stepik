# import time


# Base line method (use list)
def fib_digit_list(n):

    data_list = [0, 1]

    if n < len(data_list):
        return data_list[n]

    while len(data_list) - 1 != n:
        data_list.append((data_list[len(data_list) - 2] + data_list[len(data_list) - 1]) % 10)

    return data_list[-1]


# Base line method (use vars for n - 1 and n - 2)
def fib_digit_var(n):

    before_value, last_value = 0, 1

    if n == 0:
        return 0

    if n == 1:
        return 1

    for _ in range(1, n):
        before_value, last_value = last_value, (before_value + last_value) % 10

    return last_value


# Input: 696352
# Output:
# 9
# Time:  0.2924020290374756 s
# 9
# Time:  0.04347491264343262 s

def main():
    n = int(input())

    # Get start time first method
    # start = time.time()

    # Execute function
    # print(fib_digit_list(n))

    # Show time
    # print('Time: ', time.time() - start, 's')

    # Get start time second method
    # start = time.time()

    # Execute function
    print(fib_digit_var(n))

    # Show time
    # print('Time: ', time.time() - start, 's')


if __name__ == "__main__":
    main()