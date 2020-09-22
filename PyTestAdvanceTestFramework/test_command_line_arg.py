import pytest


# Run using conftest
def test_command_line_methodA(oneTimeSetUp, setUp):
    print("Running method A")


def test_command_line_methodB(oneTimeSetUp, setUp):
    print("Running method B")
