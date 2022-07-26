#Q1.REVERSE A STRING
'''
def rev(str):
    str1=''
    index=len(str)
    while index>0:
        str1=str1+str[index-1]
        index=index-1
    return str1
str=input("Enter your string : ")
print(rev(str))

#Q2. print Fibonacci series in reverse order
def revfibo(n):
    a=[0]*n
    a[0]=0
    a[1]=1
    for i in range(2,n):
        a[i]=a[i-2]+a[i-1]
    for i in range(n-1,-1,-1):
        print(a[i],'',end='')
def main():
    n=int(input("Enter any number: "))
    revfibo(n)
if __name__=='__main__':
    main()
'''
#Q3.Print vowel characters present in a string.
def vowel(str):
    count=0
    v=['a','e','i','o','u',]
    for i in str:
        if i in v:
            count=count+1
    return count
def main():
    str=input("Enter your sentence :")
    print("Number of vowels= ",vowel(str))
if __name__=='__main__':
    main()

        
        
