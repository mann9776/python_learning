# classes are user defined blueprint or prototype
# Sum or multiplication or addition or constant
# Methods, class variables, instance variables,  constructor etc
# Objects for your classes
# self keyword is mandatory for calling variable names into methods
# instance and class variables have whole different purpose
# constructor name should be __init__
# New keyword is not required when you create object

class Calculator:
    num = 100   # class variables
    # default constructor
    def __init__(self, a , b):
        self.firstnumber  = a
        self.secondnumber = b
        print("I am called automatically when object is created")
    def getData(self):
        print("I am now executing as method")

    def summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num


#obj = Calculator(2, 3)  # syntax to create objects in python
#obj.getData()
#print(obj.summation())

#obj2 = Calculator(4, 5)
#obj.getData()
#print(obj2 .summation())



