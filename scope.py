'''def outer():
    x=10
    print(x)
    def inner():

        x=20
        print(x)
    inner()
    print(x)
x=5
outer()
print(x)
'''
def sum(a):
    a=a-1
    if (a>0):
        sum(a)
    print(a)
sum(5)
