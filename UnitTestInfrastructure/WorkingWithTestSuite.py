import unittest
from UnitTestInfrastructure.TestClass1InTestSuite import TestClass1
from UnitTestInfrastructure.TestClass2InTestSuite import TestClass2

# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)