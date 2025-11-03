import a


def test_a_function():
    assert a.function_from_a() == "a"


def test_a_calls_b():
    assert a.call_b() == "b"
