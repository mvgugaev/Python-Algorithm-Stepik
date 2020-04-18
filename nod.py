import time


def gcd(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    if a > b:
        return gcd(a % b, b)
    elif a < b:
        return gcd(a, b % a)

    return a


# Задача: По данным двум числам 1 <= a,b <= 2 * 10^9 найдите их наибольший общий делитель.

# Input: 1000000000 444
# Output:
# 4
# Time:  3.0040740966796875e-05 s


def main():
    a, b = map(int, input().split())

    # Get start time first method
    start = time.time()

    # Execute function
    print(gcd(a, b))

    # Show time
    print('Time: ', time.time() - start, 's')


if __name__ == "__main__":
    main()
