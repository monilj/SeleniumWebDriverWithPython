import sys

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
print(car)
print(car['make'])
car['avg'] = 12
print(car)

# Nested dictionaries
dic = {'key1': {'nestedKey1': 'nestedValue1', 'nestedKey2': 'nestedValue2'},
       'key2': 'value2'}
print(dic)
print(dic['key1']['nestedKey1'])

print(dic.values())
print(sys.version)
print(sys.version_info)

# cars.keys: List all the key present in dictionary
# cars.values : List all the values present in dictionary
# cars.items: all the items as a list (key value) it is known as couple
# car_c=cars.copy(): create copy of dictionary
# car.clear()  : make list empty
print("Car methods")
print(car.keys())
print(car.values())
print(car.items())
copyOfCar = car.copy()
print(copyOfCar)