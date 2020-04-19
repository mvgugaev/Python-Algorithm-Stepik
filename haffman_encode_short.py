from collections import Counter, namedtuple
import heapq
import time

# Задача: По данной непустой строке s длины не более 10^4,
# состоящей из строчных букв латинского алфавита,
# постройте оптимальный беспрефиксный код. В первой строке выведите
# количество различных букв k, встречающихся в строке, и размер получившейся
# закодированной строки. В следующих kk строках запишите коды букв в
# формате "letter: code". В последней строке выведите закодированную строку.

# Input: abacabad
# Output:
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111
# Time:  0.00020194053649902344 s


class Node(namedtuple('Node', 'left right')):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def haffman_encode(s):
    h = []

    # len(h) need to block heapq sort by 2 tuple attribute
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    # Additional count to clock heapq sort by 2 tuple attribute
    count = len(h)

    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    # Result code dict
    code = {}

    if h:
        # Get root of 2n min priority order [element with max frequency]
        [(_freq, _count, root)] = h

        # Add code to dict
        root.walk(code, "")

    return code


def main():
    s = input()

    # Get start time
    start = time.time()

    code = haffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))

    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))

    print(encoded)

    # Show time
    print('Time: ', time.time() - start, 's')


if __name__ == '__main__':
    main()