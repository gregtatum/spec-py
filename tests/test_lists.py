from functools import reduce


def test_list_basics():
    list = ["a", "b", "c"]
    assert list.index("b") == 1, "Can get the index of a list element"
    list.append("d")
    assert list.index("d") == 3, "Can get the index of a list element"


def test_list_comparison():
    list_1: list[str] = ["a", "b", "c"]
    list_2 = ["a", "b", "c"]
    list_3 = ["a", "b", "c", "d"]
    list_1_ref = list_1
    assert list_1 == list_2, "This checks the equality of two lists by comparing them"
    assert list_1 != list_3, "These lists are not equal"
    assert list_1 is list_1_ref, "Multiple bindings can point to the same object"
    assert list_1 is not list_2, "Different lists show up as different"


def test_list_iteration():
    numbers: list[float] = [0, 1, 2, 3]
    sum: float = 0
    for n in numbers:
        sum += n

    assert sum == 6, "Can iterate simply through a list"


def test_list_comprehension_copying():
    numbers = [0, 1, 2, 3]
    numbers_copy = [x for x in numbers]
    assert numbers == numbers_copy, "List comprehension can by itself copies an array"
    assert numbers is not numbers_copy, "The two lists have different identities"


def test_list_comprehension_filter():
    numbers = [0, 1, 2, 3]
    evens = [x for x in numbers if x % 2 == 0]
    assert evens == [0, 2], "List comprehension can filter things"


def test_list_comprehension_map():
    numbers = [0, 1, 2, 3]
    doubles = [x * 2 for x in numbers]
    assert doubles == [0, 2, 4, 6], "List comprehension can map things"


def test_list_comprehension_map_and_filter():
    numbers = [0, 1, 2, 3]
    doubles = [x * 2 for x in numbers if x <= 2]
    assert doubles == [
        0,
        2,
        4,
    ], "List comprehension can map and filter, but filters first"


def test_iterables():
    list = [x for x in range(4)]
    assert list == [0, 1, 2, 3], "Iterables can be used as well."


def test_map_function():
    numbers = [0, 1, 2, 3]
    doubles = map(lambda x: x * 2, numbers)
    assert list(doubles) == [0, 2, 4, 6], "The map function can double items"


def test_filter_function():
    numbers = [0, 1, 2, 3]
    evens = filter(lambda x: x % 2 == 0, numbers)
    assert list(evens) == [0, 2], "The filter function can filter items"


def test_reduce_function():
    numbers = [0, 1, 2, 3]
    # Notice that this has to be imported from functools
    sum = reduce(lambda x, y: x + y, numbers)
    assert sum == 6, "Reduce can combine values"
