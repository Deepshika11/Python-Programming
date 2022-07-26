class Stack:
    def __init__(self,m):
        self.max=m
        self.l=[]
        self.top=-1
    def Push(self):
        if self.top==self.max-1:
            print("## Stack Overflow")
            return
        item = int(input("Enter the Item: "))
        self.top+=1
        self.l.append(item)
        print(">> ",item,"is Inserted the to Stack")
        print(self.l)
    def Pop(self):
        if self.top == -1:
            print("## Stack is Empty")
            return
        item=self.l.pop(self.top)
        self.top-=1
        print(">> ",item, "is Deleted From Stack")
        print(self.l)
    def Traverse(self):
        if self.top == -1:
            print("## Stack is Empty")
            return
        print(self.l)
m=int(input("Enter the maximum size of Stack: "))
obj = Stack(m)
while True:
    print("<< **** STACK OPERATIONS **** >>")
    print("\t\t1.Push ")
    print("\t\t2.Pop ")
    print("\t\t3.Traverse")
    print("\t\t0.Exit")
    n=int(input("Enter Your Choice: "))
    if n==1:
        obj.Push()
    if n == 2:
        obj.Pop()
    if n == 3:
        obj.Traverse()
    if n==0:
        break
