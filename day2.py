class result():
    def __init__(self):
        self.name=''
    def get(self):
        self.name=input('Enter the your Name:')
    def printstring(self):
        print(self.name.upper())
c=result()
c.get()
c.printstring()