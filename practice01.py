'''def fibo(n):
     if n<0:
          return ("ERROr")
     if n<=1:
          return n
     else:
          return fibo(n-1)+fibo(n-2)
n=int(input("Enter the position:"))
print(fibo(n))
    
def gcd(a,b):
      if a==0:
           return b
      if b==0:
           return a
      if a==b:
           return a
      else:
           return gcd(b,a%b)
a=int(input())
b=int(input())
print("The gcd of {} and {} is {}".format(a,b,gcd(a,b)))
'''

