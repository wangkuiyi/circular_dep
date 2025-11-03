import b


def test_b_function():
    assert b.function_from_b() == "b"


def test_b_calls_a():
    assert b.call_a() == "a"
