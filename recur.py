#Q1. WAP to find the factorial of a natural number.
def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
n=int(input("Enter any natural number: "))
fac(n)

#Q2.WAP to determine the nth term to fibonacci series.
def fib(n):
    a=0
    b=1
    if n<=0:
        print("Incorrect input.")
    
    elif n==1:
        return b
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b
n=int(input("Enter the term? "))
if __name__=='__main__':
    print("The fibonacci term is",fib(n))

#Q3. WAP to calculate GCD of two natural numbers.
def gcd(a,b):
    if(a==0):
        return b
    elif(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("The GCD of",a,"and",b,"is",gcd(a,b))

    
    

