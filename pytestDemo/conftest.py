# This file generalize the fixture and can be used everywhere in other files
import pytest


#@pytest.fixture() # Will be used for calling the part of program which can be used any other test cases like opening a browser

@pytest.fixture(scope="class")  # Using this we don't need to put fixture's method name in every methods where it is called
# it just enables when class start and teared down after class is completed
def setup():
    print("I will be executing first")
    yield  # This makes the part of the program execute at the last. like closing a browser
    print("executing at last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]

@pytest.fixture(params=[("Chrome","Rhaul","Shetty"),("Firefox","shetty"),("IE","SS")])
def crossBrowser(request):
    return request.param
