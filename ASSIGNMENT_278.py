#defining parent class
class Main:
    def __init__(self):
        #protected attributes
        self._protected = 0
        #private attributes
        self.__private = 2
    #creating function
    def foo(self):
        print("function")







#creating object of class
obj = Main()
#calling method inside class
obj._protected = 1
obj.__private = 3
#accessing proctected
print(obj._protected)
#accessing private
print(obj.__private)
        
        
        
