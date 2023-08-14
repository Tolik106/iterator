class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):

        sum_list = sum(self.list_of_list, [])

        if len(sum_list) - 1 == self.position:
            raise StopIteration
        else:
            self.position += 1
        return sum_list[self.position]




def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for item in FlatIterator(list_of_lists_1):
        print(item)