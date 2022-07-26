class a:
    def __init__(self,n):
        self.name=n
    def fun1(self):
            print("Name:",self.name)
class b:
    def __init__(self,r):
        self.roll=r
    def fun2(self):
        print("Roll:",self.roll)
class c(a,b):
    def __init__(self,n,r,d):
        a.__init__(self,n)
        b.__init__(self,r)
        self.department=d
    def fun3(self):
        a.fun1(self)
        b.fun2(self)
        print("Department:",self.department)
obj=c("Deepshika",15,"MCA")
obj.fun3()
        
        
            
