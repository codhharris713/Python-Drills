from abc import ABC, abstractmethod
#defining parent class
class Main(ABC):
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    #regular method
    def foo(self):
        print('this is number one %d and number two %d' % (self.num_1, self.num_2))

    #abstract method
    @abstractmethod
    def bar(self):
        pass
#child class inheriting from Main and implementing abstract method bar()
class secondary(Main):
    number = 3
    
    def bar(self):
        return self.num_1 * secondary.number

#call bar method
obj = secondary(1, 2)
obj.foo()
x = obj.bar()
print('1 + 2 is:', x)

    
              
