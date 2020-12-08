class Calculator:
    num = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I am called when object is getting created")

    def add(self):
        return self.a + self.b


obj1 = Calculator(4, 5)
print(obj1.add())


class ChildImp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 5)

    def getCompleteData(self):
        return self.num2 + self.num + self.add()


obj = ChildImp()
print(obj.getCompleteData())
