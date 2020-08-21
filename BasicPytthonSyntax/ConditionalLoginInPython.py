"""
Conditional Logic in Python
"""
print("Code for if-else conditional loop")
if 90 > 35:
    print("Ninety is greater than Thirty five")

value = 'Cycle'

if value == 'Cycle':
    print("Need efforts")
elif value == 'Bike':
    print("Less effort")
else:
    print("Walk")

print("It will always print")

"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""
print("Code for while conditional loop")
x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

empty_list = []
num = 0
while num < 10:
    empty_list.append(num)
    print("Value of num is: " + str(num))
    num += 1

print(empty_list)

"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""
print("Code for while-break-else conditional loop")
x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

    if x == 8:
        break
    print("This example is awesome")
    print("*"*20)
else:
    print("Just broke out of the loop")

print("Code for while-continue conditional loop")
x = 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x + 1

    if x == 8:
        continue
    print("This example is awesome")
    print("*"*20)

print("Just broke out of the loop")

"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""
print("Code for for-range conditional loop")
a = range(0, 20, 6)
print(a)
print(type(a))

print(list(a))


l = [1, 2, 3]

for num in range(1, 4):
    print(num)