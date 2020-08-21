"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""

my_list = [1, 2, 3]

my_file = open("firstfile.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

"""
File I/O
Reading a file -> .read()
Reading line by line -> .readline()
"""

my_file = open("firstfile.txt", 'r')

print(str(my_file.read()))
my_file.close()

print("Line by line ========>>")

my_file_line = open("firstfile.txt", 'r')
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))

my_file_line.close()

"""
With / As Keywords
"""
# print("Normal Write Start")
# my_write = open("textfile.txt", "w")
# my_write.write("Trying to write to the file")
# my_write.close()
#
#
# print("Normal Read Start")
# my_read = open("textfile.txt", "r")
# print(str(my_read.read()))

print("With As Write Start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of with as write/read")

print()
print("With As Read Start")
with open("withas.txt", "r") as with_as_read:
    print(str(with_as_read.read()))
