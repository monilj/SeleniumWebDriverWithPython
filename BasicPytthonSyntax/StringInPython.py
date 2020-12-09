"""
Examples to show how strings works in python

Sequence of characters
Contains a-z, 0-9, @
In double or single quotes
"""

a = "This is a simple string"
b = 'Using single quotes'

print(a)
print(b)

c = "Need to use 'quotes' inside a string"
print(c)

d = "Another way to handle \"quotes\""
print(d)

a = "This is a single\
 string"
print(a)

"""
Examples to show how string formatting works in python
"""

city = "Pune"
event = "drama"

print("Welcome to " + city + " and enjoy the " + event)
print("Welcome to %s" % city)
print("Welcome to %s and enjoy the %s" % (city, event))

# Accessing characters in strings
# len(): length of string
# lower(): convert all the character of a string to lower case method
# upper(): convert all the character of a string to upper case method
# str(): convert non string value to string representation
# Replace some character in sting

# index starts from zero
first = "Pune"[0]
print(first)
new_str = "Access"
print(len(new_str))
print(new_str.upper())
print(new_str.lower())
print(new_str.replace('s', 'S'))
print(new_str + str(2))

# Sub-Strings
# starting index is inclusive
# Ending index is exclusive
sub = a[1:6]
step = a[1:6:2]
print(sub)
print(step)

print("========== Newly Added code ==========")

courseN = "RahulShetty.com"
author = "Rahul"

print(author in courseN)
var = courseN.split(".")
print(var)

checkTrim ="   great   "
print(checkTrim)
print(checkTrim.strip())
print(checkTrim.lstrip())
print(checkTrim.rstrip())
