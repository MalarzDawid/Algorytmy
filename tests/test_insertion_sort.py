from algo.sorting_algorithms.insertion_sort import insertion_sort


def test_insertion_sort_normal():
    assert [1, 2, 3, 5, 8, 9] == insertion_sort([3, 5, 8, 9, 1, 2])


def test_insertion_sort_two_nums():
    assert [1, 2, 2, 5, 6, 45] == insertion_sort([5, 2, 1, 2, 45, 6])


def test_insertion_sort_same_number():
    assert [1, 1, 1, 1, 1, 1] == insertion_sort([1, 1, 1, 1, 1, 1])

