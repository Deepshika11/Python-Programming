'''def fact():
    num=5
    factorial=1
    for i in range(1,num+1):
                   factorial=factorial*i
    return factorial
f1=fact()
print("The factorial of 5 is",f1)
    
HiHi
'''

try:
    if'1'!=1:
        raise"someError"
    else:
        print("someError has not occured")
except"someError":
    print("someError has occured")
