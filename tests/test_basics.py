shadowed_value = "This is global"

# Just run through some trival tests.


def test_basics():
    my_string = "Value"
    assert my_string == "Value", "Variables are scoped to their function."
    # Set a global for the next test.


def test_global_vs_local():
    shadowed_value = "This is local"
    assert shadowed_value == "This is local", "Setting a variable will be local."


def test_globals_access():
    global shadowed_value
    assert shadowed_value == "This is global", "Globals arent overwritten"
    # Mutate the value:
    shadowed_value = "This is global rewritten"


def test_globals3():
    global shadowed_value
    assert (
        shadowed_value == "This is global rewritten"
    ), "Can be accessed and mutated using the global keyword"


def test_int_float():
    assert type(1) == int, "No trailing dot means a number is an integral value"
    assert type(1.0) == float, "A trailing dot means a number is a float value"
    assert type(1 + 1.0) == float, "Adding an int to a float creates a float"
    assert type(1.0 + 1) == float, "Adding a float to an int creates a float"
    assert 1_000_000 == 1e6, "You can use various types of notation"
    assert type(1e6) == float, "Floats can use e notation as well"
    assert 1 == 1.0, "You can do equality checks on int vs float"
    assert float("inf") > 0, "Infinity can be represented"
    assert float("-inf") < 0, "-Infinity can be represented"
    assert str(-0.0) == "-0.0", "Negative zero exists"
    assert 0.0 == -0.0, "Comparisons of zeros are equal"


def test_max_int_size():
    # This is the maximum size a `long` type can store, python doesn't use
    # this internally.
    max_long_size: int = 9_223_372_036_854_775_807

    assert str(max_long_size) == "9223372036854775807"
    assert str(max_long_size - 1) == "9223372036854775806"
    assert str(max_long_size + 0) == "9223372036854775807"
    assert str(max_long_size + 1) == "9223372036854775808"
    assert str(max_long_size + 2) == "9223372036854775809"
    assert str(max_long_size + 3) == "9223372036854775810"

    assert str(9223372036854775806 + 1) == "9223372036854775807"
    assert str(9223372036854775806 + 2) == "9223372036854775808"
    assert str(9223372036854775806 + 3) == "9223372036854775809"
    assert str(9223372036854775806 + 4) == "9223372036854775810"
    assert (
        str(99999999999999999999999999999999999999999999999999999999999999999)
        == "99999999999999999999999999999999999999999999999999999999999999999"
    )


def test_max_double_size():
    max_double_size: float = 1.7976931348623157e308
    assert max_double_size == 1.7976931348623157e308
    assert (
        max_double_size + 1.0 == max_double_size
    ), "There is not enough precision to increase this number."
    assert max_double_size * 2.0 == float(
        "inf"
    ), "This is just a double, and we have exceeded its capacity"


def test_number_wats():
    fake_float: float = 1
    assert type(fake_float) == int
    # This is a type error:
    fake_int: int = 1.0  # type: ignore
    assert type(fake_int) == float


def test_decorator():
    """This test uses the decorator behavior to take a result and double it."""

    def double_result(func):
        """This is the decorator"""

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * 2.0

        return wrapper

    @double_result
    def add_doubled(a, b):
        return a + b

    assert add_doubled(1, 2) == 6
    assert add_doubled(2, 7) == 18
