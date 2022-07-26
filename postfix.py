class Evaluate:
    def __init__(self,capacity): 
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def isEmpty(self):
        if self.top==-1: 
            return True
        else:
            return False
    def pop(self):
        if not self.isEmpty():
            self.top -=1
            return self.array.pop()
        else:
            return "*"
    def push(self,op):
        self.top +=1
        self.array.append(op)
    def evaluatePostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2+i+val1)))
        return int(self.pop)
exp="5 6 2 + * 12 4 / -"
obj=Evaluate(len(exp))
print("postfix evaluation: %d" %(obj.evaluatePostfix(exp)))
        
        
         
