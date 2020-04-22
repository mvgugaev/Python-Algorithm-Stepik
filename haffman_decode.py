import time
from typing import Union

# Задача: Восстановите строку по её коду и беспрефиксному коду символов. В первой строке
# входного файла заданы два целых числа k и l через пробел — количество различных букв,
# встречающихся в строке, и размер получившейся закодированной строки, соответственно. В
# следующих k строках записаны коды букв в формате "letter: code". Ни один код не является префиксом другого.
# Буквы могут быть перечислены в любом порядке. В качестве букв могут встречаться лишь строчные буквы латинского
# алфавита; каждая из этих букв встречается в строке хотя бы один раз. Наконец, в последней строке записана
# закодированная строка. Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная строка
# имеет минимальный возможный размер.В первой строке выходного файла выведите строку s. Она должна состоять из
# строчных букв латинского алфавита. Гарантируется, что длина правильного ответа не превосходит 10^4

# Input:
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111
# Output:
# abacabad
# Time:  0.37802600860595703 s


# Class for tree node
class TreeLink:

    # Create tree element
    def __init__(self, child_list: dict, letter: Union[None, str]):
        self.child_list = child_list
        self.letter = letter


# Recursive add element to tree
def add_element_to_tree(head: TreeLink, code: str, letter: str):

    # If last symbol in code
    if len(code) == 1:
        head.child_list[code[:1]] = TreeLink({}, letter)
        return
    elif code[:1] not in head.child_list:
        head.child_list[code[:1]] = TreeLink({}, None)

    add_element_to_tree(head.child_list[code[:1]], code[1:], letter)


def main():
    letter_count, _ = [int(i) for i in input().split(' ')]

    # Get start time
    start = time.time()

    code_tree_head = TreeLink({}, None)

    # Add symbols to tree
    for _ in range(0, letter_count):
        letter, code = input().replace(':', '').split()

        add_element_to_tree(code_tree_head, code, letter)

    # get result string
    result_string = input()

    head = code_tree_head

    # Print decode string
    for item in result_string:

        if item in head.child_list:
            head = head.child_list[item]
        else:
            head = code_tree_head.child_list[item]

        if head.letter:
            print(head.letter, end='')

    # Show time
    print('\nTime: ', time.time() - start, 's')


if __name__ == "__main__":
    main()
