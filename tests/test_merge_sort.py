from algo.sorting_algorithms.merge_sort import merge_sort


def test_merge_sort_odd_nums():
    assert [1, 2, 3, 4, 5, 6, 7] == merge_sort([5, 4, 1, 2, 3, 7, 6])


def test_merge_sort_even_nums():
    assert [1, 2, 3, 4, 5, 6, 7, 8] == merge_sort([6, 4, 3, 8, 7, 1, 2, 5])


def test_merge_sort_two_nums():
    assert [1, 2, 2, 2, 3, 4] == merge_sort([3, 2, 4, 2, 1, 2])


def test_merge_sort_same_numbers():
    assert [9, 9, 9, 9, 9] == merge_sort([9, 9, 9, 9, 9])


def test_merge_sort_empty_array():
    assert [] == merge_sort([])
