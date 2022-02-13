from algo.insertion_sort import insertion_sort


def test_insertion_sort():
    assert [1, 2, 3, 5, 8, 9] == insertion_sort([3, 5, 8, 9, 1, 2])
