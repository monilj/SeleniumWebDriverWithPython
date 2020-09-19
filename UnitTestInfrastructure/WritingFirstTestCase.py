import unittest


class FirstTestCase(unittest.TestCase):

    def setUp(self):
        print("I will run once before every test demo")

    def test_method1(self):
        print("Running method 1")

    def test_method2(self):
        print("Running method 2")

    def tearDown(self):
        print("I will run after every test demo")


if __name__ == "__main__":
    unittest.main(verbosity=2)
