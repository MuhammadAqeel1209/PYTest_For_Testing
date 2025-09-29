# from main import func
# def test_answer():
#     assert func(4) == 5

import pytest

# Assertion

# def test_zero_division():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0

# def test_recursion_depth():
#     with pytest.raises(RuntimeError) as excinfo:

#         def f():
#             f()

#         f()
#     assert "maximum recursion" in str(excinfo.value)


# def myfunc():
#     raise ValueError("Exception 13 raised")


# def test_match():
#     with pytest.raises(ValueError, match=r".* 13 .*"):
#         myfunc()

# def test_exception_in_group():
#     with pytest.RaisesGroup(ValueError):
#         raise ExceptionGroup("group msg", [ValueError("value msg")])
#     with pytest.RaisesGroup(ValueError, TypeError):
#         raise ExceptionGroup("foo", [ValueError("foo"), TypeError("bar")])

# def test_structure():
#     # flatten_subgroups=False → only top-level exceptions are considered.
#     # flatten_subgroups=True → pytest flattens nested groups and checks inner exceptions too.

#     # allow_unwrapped=False (default) → only ExceptionGroup is allowed.
#     # allow_unwrapped=True → bare exceptions of expected type(s) are also accepted.
    
#     with pytest.RaisesGroup(pytest.RaisesGroup(ValueError)):
#         raise ExceptionGroup("", (ExceptionGroup("1st", (ValueError("1st"),)),))
#     with pytest.RaisesGroup(ValueError, flatten_subgroups=True):
#         raise ExceptionGroup("1st group", [ExceptionGroup("1st group", [ValueError("1st group")])])
#     with pytest.RaisesGroup(ValueError, allow_unwrapped=True):
#         raise ValueError


# def func(x):
#     if x <= 0:
#         raise ValueError("x needs to be larger than zero")


# pytest.raises(ValueError, func, x=-1)

# def test_set_comparison():
#     set1 = set("1308")
#     set2 = set("13088031")
#     assert set1 == set2

# class Foo:
#     def __init__(self, val):
#         self.val = val

#     def __eq__(self, other):
#         return self.val == other.val

# def pytest_assertrepr_compare(op, left, right):
#     if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
#         return [
#             "Comparing Foo instances:",
#             f"   vals: {left.val} != {right.val}",
#         ]


# def test_compare():
#     f1 = Foo(1)
#     f2 = Foo(0+2)
#     assert f1 == f2




# Fixture
