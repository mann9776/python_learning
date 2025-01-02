# Any pytest filename should start with test_ or end with _test
# in pytests write code always wrapped in methods and call them as test methods and name start with test_
# multiple test methods should not have same name in one file
import pytest


@pytest.mark.smoke # annotations
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail  # test case will run but report will not generate
def test_SecondgreetCreditCard():
    print("Good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

