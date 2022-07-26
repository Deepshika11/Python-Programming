'''try:
    f1=open('test1.py','r')
    print(f1.read())
    f1.close
except FileNotFoundError:
    print("File does not exist")
    print("Find another file which exist.")
   

try:
    b=0
    a=12/b

    print("Hello World",b)
except ZeroDivisionError:
    print("Divide by zero is undefined.")
except:
    print("Must Execute")


def mystry(l):
    l=l[0:5]
    return()
list1=[44,71,12,8,23,17,16]
mystry(list1)

def fun(s,r):
    if len(s)==0:
        return r
    else:
        print(s[-1])
        return fun(s[:-1],r+s[-1])
r=''
print(fun('BCA',r))
'''
p=q=r=10
print(r)
