class rectangle():

    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length  * self.width
obj=rectangle(2,3)
obj1=rectangle(10,2)
print(obj.area())
print(obj1.area())
