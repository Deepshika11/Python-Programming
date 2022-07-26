'''lst1=eval(input("Enter your list:"))
total=0
print(lst1)
for i in range(len(lst1)):
    print(lst1[i])
for i in range(0,len(lst1)):
    total=total+lst1[i]
print("The sum of the given list is ",total)
'''
lst=eval(input("Enter your list: "))
n=len(lst)
j=n-1
while j>=1:
    for i in range(0,j):
        if lst[i]>lst[i+1]:
            t=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=t
    j=j-1
print(lst)
