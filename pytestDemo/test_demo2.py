# Any pytest filename should start with test_ or end with _test
# in pytests write code always wrapped in methods and call them as test methods and name start with test_
# multiple test methods should not have same name in one file
# method names should have sense
# -k stands for method names execution, -s logs in output, -v more info metadata, -m used for marks
# we also can run specific file with py.test <filename>, we can mark (or tag) test cases with @pytest.mark.smoke
# data driven and parameterization can be done with return statements in tuple format
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"  # need for some operations in other tests.
    assert msg == "Hi", "Test failed due to string not matched"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == b, "Addition do not match"



def test_fixtureDemo(setup):
    print(" I will be executing in fixtureDemo method")