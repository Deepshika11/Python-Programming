#Q1.
'''def recMul(a,b):
    if (b==0):
        return 
    elif (b>0):
        return (a+recMul(a,b-1))          
a=int(input("Enter the first positive number:"))
b=int(input("Enter the second positive number: "))
print(recMul(a,b))

#Q2.
def digit(n):
    if n==0:
        return 
    elif n>0:
        d=n%10
        digit(n//10)
        print(d,'',end='')
n=int(input("Enter numbers: "))
digit(n)


#Q3.
def rev(n):
    if n==0:
        return 
    elif n>0:
        d=n%10
        print(d,'',end='')  
        rev(n//10)
        
n=int(input("Enter numbers: "))
rev(n)
'''
#Q4.

def rev(n,l):
    if n==0:
        return 
    if n>0:
        d=n%10
        if d not in l:
            l.append(d)
        rev(n//10,l)
    return l      
n=int(input("Enter numbers: "))
l=[]
print(rev(n,l))

