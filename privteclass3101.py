'''class student:
    def __init__(self,n,r):
        self.name=n
        self.__roll=r
    def show(self):
        print("Name:",self.name)
        print("Roll:",self.__roll)
s1=student('Gopal',1)
s1.show()
print(s1.name)
print(s1.__roll)
'''

class A:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def show(self):
        print("Name in A:",self.name)
        print("Roll in A:",self.roll)
class B(A):
    def __init__(self,n,r):
        A.__init__=(self,n,r)
        self.name=n
        self.roll=r
    def C(B):
        def __init__(self,n,r):
            B.__init__(self,n,r)
            self.name=n
            self.roll=r
    def display(self):
        print(self.name)
        print(self.roll)
ob=B("Deepshi",1)
ob.display()
        
