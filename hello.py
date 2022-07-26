print("Hello, pp how are you?")
a=10
b=12
s=a+b
print("The sum of {} and {} is {}".format(a,b,s))
j=1
while j<=5:
    i=1
    while i<=5:
        print(j,i,' ',end='')
        i=i+1
    j=j+1
    print()
#2,4,6...
n=100
i=1
while i<=n:
    a=i*i
    print(a,'',end='')
    i=i+1

#1+2+3+...
n=int(input("Enter the term: "))
sum=0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum=sum+j
print(sum)
