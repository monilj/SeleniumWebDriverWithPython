import pytest


@pytest.fixture()
def setUp():
    print("Running setUp method")


def test_demo1_method1(setUp):
    print("Running demo1 method A")


def test_demo1_method2(setUp):
    print("Running demo1 method B")
