import sys


# Задача на программирование: очередь с приоритетами
# Задача: Первая строка входа содержит число операций 1 <= n <= 10^5.
# Каждая из последующих nn строк задают операцию одного из следующих двух типов:
#   Insert x , где 0 <= x <= 10^9 — целое число;
#   ExtractMax
# Первая операция добавляет число xx в очередь с приоритетами,
# вторая — извлекает максимальное число и выводит его.

# Input:
# 6
# Insert 200
# Insert 10
# ExtractMax
# Insert 5
# Insert 500
# ExtractMax

# Output:
# 200
# 500

class PriorityQueue:

    def __init__(self):
        self.data = []

    # Insert element to array and shift up
    def insert_element(self, element: int) -> None:

        self.data.append(element)
        current_index = len(self.data)

        # shift up
        while current_index != 1 and self.data[int(current_index / 2) - 1] < self.data[current_index - 1]:
            self.data[int(current_index / 2) - 1], self.data[current_index - 1] = self.data[current_index - 1], self.data[int(current_index / 2) - 1]
            current_index = int(current_index / 2)

    # Get head element, change head with last and shift down
    def extract_max(self) -> int:

        max_value = self.data[0]

        if len(self.data) > 1:
            self.data[0] = self.data[-1]

            # More fast then self.data = self.data[:-1]
            del self.data[-1]

            current_index = 1
            array_len = len(self.data)

            first_child = 2 if array_len > 1 else None
            second_child = 3 if array_len > 2 else None

            # shift down
            while first_child and self.data[first_child - 1] > self.data[current_index - 1] or \
                    second_child and self.data[second_child - 1] > self.data[current_index - 1]:

                if first_child and second_child and self.data[first_child - 1] > self.data[second_child - 1] or not second_child:
                    self.data[first_child - 1], self.data[current_index - 1] = self.data[current_index - 1], self.data[first_child - 1]
                    current_index = first_child
                else:
                    self.data[second_child - 1], self.data[current_index - 1] = self.data[current_index - 1], self.data[second_child - 1]
                    current_index = second_child

                first_child = (2 * current_index) if array_len >= (2 * current_index) else None
                second_child = (2 * current_index + 1) if array_len >= (2 * current_index + 1) else None
        else:
            self.data = []

        return max_value


if __name__ == "__main__":
    inst = PriorityQueue()

    operation_count = int(sys.stdin.readline())
    result_list = []

    for _ in range(0, operation_count):
        operation = sys.stdin.readline()

        if 'Insert' in operation:
            value = int(operation.split(' ')[1])
            inst.insert_element(value)
        else:
            # print(inst.data)
            result_list.append(str(inst.extract_max()))

    print('\n'.join(result_list))
