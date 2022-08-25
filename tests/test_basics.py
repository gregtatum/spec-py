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
