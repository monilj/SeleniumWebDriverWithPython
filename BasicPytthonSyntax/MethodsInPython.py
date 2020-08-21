"""
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""


def additionOfNumbers(n1, n2):
    print(n1 + n2)


additionOfNumbers(2, 8)

additionOfNumbers(3, 3)

numbered_list = [1, 2, 3]
print(numbered_list.append(4))
print(numbered_list)

print(len(numbered_list))

"""
Methods which adds data having different data type
Methods with if-else 
"""


def sum_nums(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums(2, 8)

sum2 = sum_nums(3, 3)

# string_add = sum_nums('one', 2)
# print(string_add)

print(sum1)
print("*************")


def isItHub(city):
    city_list = ['Pune', 'Mumbai', 'Bangalore']

    if city in city_list:
        return True
    else:
        return False


y = isItHub('Noida')
print(y)

y = isItHub('Bangalore')
print(y)

"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""


def sum_nums(n1, n2=4):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2


sum1 = sum_nums(4, n2=12)
print(sum1)

"""
Variable Scope
"""

a = 10


def test_method(a):
    print("Value of local 'a' is: " + str(a))
    a = 2
    print("New value of local 'a' is: " + str(a))


print("Value of global 'a' is: " + str(a))
test_method(a)
print("Did the value of global 'a' change? " + str(a))

a = 10


def test_method():
    global a
    print("Value of 'a' inside the method is: " + str(a))
    a = 2
    print("New value of 'a' inside the method is changed to: " + str(a))


print("Value of global a is: " + str(a))
test_method()
print("Did the value of global 'a' change? " + str(a))
