'''class student:
    def given_data(self,r,n):
        self.roll=r
        self.name=n
    def show_data(self):
        print(self.roll)
        print(self.name)
s1=student()
s1.given_data(1,'Deepshika')
s1.show_data()
s2=student()
s2.given_data(2,'Agya')
s2.show_data()

class student:
    def __init__(self,n,r):
        self.roll=r
        self.name=n
    def show_data(self):
        print('Roll:',self.roll)
        print('Name:',self.name)
s1=student('Deepshika',1)
s1.show_data()        
s2=student('Avik',2)
s2.show_data()
'''
class student:
    count=0
    def __init__(self,n):
        student.count+=1
        self.roll=student.count
        self.name=n
    def __str__(self):
       return(f"Name:{self.name} Roll:{self.roll}")
s1=student('Deepshika')
print(s1.__str__())
s2=student('Avik')
print(s2.__str__())
