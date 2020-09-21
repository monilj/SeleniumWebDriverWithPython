import pytest


@pytest.yield_fixture()
def setUp():
    print("Running demo2 setUp")
    yield
    print("Running demo2 tearDown")


def test_demo2_methodA(setUp):
    print("Running demo2 method A")


def test_demo2_methodB(setUp):
    print("Running demo2 method B")


'''
 To run this code follow the steps mentioned below:
 1.	Open command prompt in administrator mode
2.	Go to Project Directory using cd command 
3.	cd path_till_project_directory
4.	Hit command dir and verify you are getting all the packages
5.	Hit command set PYTHONPATH=%PYTHONPATH%;%CD% to set the current directory to path
6.	Hit command echo %PYTHONPATH%
7.	It should list the value of path variable separated by semi-colon 
8.	It must include python project path
9.	Hit command py.test
10.	It will run the test and shows the test result
11.	But if you want to show the Print statements on the console hit command py.test -s -v
12.	Validate the test execution
'''