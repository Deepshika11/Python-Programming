#Q1.Print the series using function concept in python.
 #   1 3 5 7...N
def odd(n):
    i=1
    while i<=n:
        print(i,'',end='')
        i=i+2
n=99
odd(n)

OUTPUT:
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 
    


#Q2.WAP in python to the given integer is odd using is odd using the concept of function in python.
def odd():
    i=int(input("Enter your number:"))
    if (i%2!=0):
        print("The number is odd.")
    else:
        print("The number is not odd.")
odd()

OUTPUT:
Enter your number:55
The number is odd.


#Q3.WAP to create a function that will returun the largest number among three integers.
def large(i,j,k):
    if i>j and i>k:
        print("The largest integer is ",i)
    elif j>i and j>k:
        print("The largest integer is ",j)
    else:
        print("The largest integer is ",k)
i=int(input("Enter first integer:"))
j=int(input("Enter second integer:"))
k=int(input("Enter third integer:"))
large(i,j,k)

OUTPUT:
Enter first integer:10
Enter second integer:20
Enter third integer:55
The largest integer is  55

#Q4.WAP to find the X of the following series using the fun cincept. You need to pass N to the fun and return X from it.
#X=1*2*3*...*N
def fact(n):
    i=1
    fact=1
    while i<=n:
        fact=fact*i
        i=i+1
    return fact
n=int(input("Enter any number: "))
a=fact(n)
print(a)

OUTPUT:
Enter any number: 5
120

#Q5.WAP to create the following pattern.
#1 1 1 1
#2 2 2 2
#3 3 3 3
#4 4 4 4
#Number of rows and columns must be user input and that will create pattern.
r=int(input("Enter row number: "))
j=1
while j<=r:
    i=1
    while i<=r:
        print(j,' ',end='')
        i=i+1
    j=j+1
    print()
print()

OUTPUT:
Enter row number: 4
1  1  1  1  
2  2  2  2  
3  3  3  3  
4  4  4  4


#Q6.WAP in python to reverse a integer.
#Input:123456789
#Output:987654321
#Write a fun that will accept one parameter and return the reserved value of that.
def rev(n):
    a=0
    while n>0:
        d=n%10
        a=a*10+d
        n//=10
    return a
n= int(input("Write any integer:"))
r=rev(n)
print(r)

OUTPUT:
Write any integer:12345
54321


#Q7.WAP in python to create the following series.
#0 1 1 2 3 5 8 13 21....N terms
n=int(input("Enter any number:"))
def Fibo(n):
    a=0
    b=1
    if n<=0:
        print("Invalid input")
    elif n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a, b,'',end="")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,'',end="")
def main():
    fibo=Fibo(n)
    
if __name__=='__main__':
    main()
OUTPUT:
Enter any number:15
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


#Q8.WAP in python to prove that at -40 both, centigrade and fahrenheit shows the same temprature.
#Write compare() and main()function.Compare() will return TRUE/FALSE based on the comparision result.
celcius=float(input("Enter the temp in celcius degree: "))
fahrenheit=(celcius*1.8)+32
def compare(celcius,fahrenheit):
    if celcius==-40 and celcius==fahrenheit:
        return True
    else:
        return False
    
def main(): 
    print(celcius," Degree celcius is ",fahrenheit,"Degree  in fahrenheit")
    if celcius==fahrenheit:
        print("-40 gives same temperature in both celcius and fahrenheit")
    else:
        print("Enter -40 as input.")

if __name__=='__main__':
    compare=compare(celcius,fahrenheit)
    main()


OUTPUT:
Enter the temp in celcius degree: -40
-40.0  Degree celcius is  -40.0 Degree  in fahrenheit
-40 gives same temperature in both celcius and fahrenheit








    
    
