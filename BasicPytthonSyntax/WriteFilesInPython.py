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
With / As Keywords
"""
# print("Normal Write Start")
# my_write = open("textfile.txt", "w")
# my_write.write("Trying to write to the file")
# my_write.close()



print("With As Write Start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is an example of with as write/read")
