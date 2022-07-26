n=int(input("Enter any number: "))
def sum(n):
    sum1=0
    i=1
    while i<=n:
        sum1=sum1+(1/i)
        i=i+1
    return sum1
print("The sum of the series is ",sum(n))

'''
def sums(n):
    sum1=0
    i=1
    fact=1
    while i<=n:
        fact=fact*i
        sum1=sum1+(i/fact)
        i=i+1
    return sum1
print("The sum of the series is ",sums(n))
'''


