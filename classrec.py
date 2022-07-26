class Rectangle:
    def get_data(self,l,b):
        self.length=l
        self.breadth=b
    def print_data(self):
        print("Length =",self.length)
        print("Breadth =",self.breadth)        
    def area(self):
        area=self.length+self.breadth
        print("Area =",area)
a1=Rectangle()
l1=int(input("Enter the length: "))
l2=int(input("Enter the breadth: "))
a1.get_data(l1,l2)
a1.print_data()
a1.area()
