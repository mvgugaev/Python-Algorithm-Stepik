import time
from typing import Union

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

class TreeLink:

    # Create tree element
    def __init__(self, width: int, child_list: Union[None, list], letter: Union[None, str]):
        self.width = width
        self.child_list = child_list
        self.letter = letter


# Work with TreeLink elements 0(n)
class Order:

    def __init__(self, array: list):
        self.array = array

    def extract_min_element(self) -> Union[TreeLink, None]:

        if len(self.array) <= 0:
            return None

        min_index = 0

        for index in range(1, len(self.array)):
            if self.array[index].width < self.array[min_index].width:
                min_index = index

        result_element = self.array[min_index]

        self.array = self.array[:min_index] + self.array[min_index + 1:]

        return result_element

    def get_len(self):
        return len(self.array)

    def add_element(self, element: TreeLink) -> None:
        self.array.append(element)


# Create list [TreeLink, TreeLink, ...] form string
def create_tree_link_list(data: str) -> list:

    result_dict = {}

    for word in data:

        if word in result_dict:
            result_dict[word].width += 1
        else:
            result_dict[word] = TreeLink(1, None, word)

    return list(result_dict.values())


# Return head of tree
def haffman_tree_generator(data: str) -> TreeLink:

    tree_link_order = Order(create_tree_link_list(data))

    while tree_link_order.get_len() > 1:
        first_min = tree_link_order.extract_min_element()
        second_min = tree_link_order.extract_min_element()

        new_element = TreeLink(first_min.width + second_min.width, [first_min, second_min], None)

        tree_link_order.add_element(new_element)

    return tree_link_order.array[0]


get_code_from_tree


def main():
    data = str(input())

    # Get start time
    start = time.time()

    result_code, result_string = {}, ''

    get_code_from_tree(haffman_tree_generator(data), '', result_code)

    for letter in data:
        result_string += result_code[letter]

    print(len(result_code.values()), len(result_string))

    for letter, replace_string in result_code.items():
        print(letter + ': ' + replace_string)

    print(result_string)

    # Show time
    print('Time: ', time.time() - start, 's')


if __name__ == "__main__":
    main()
