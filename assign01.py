'''
def count(s):
    dict={}
    for i in s:
        for i in ['a','e','i','o','u']:
            c=s.count(i)
            dict.update({i:c})
    print(dict)
s=input("Enter a word : ").lower()
count(s)



n=int(input("Enter range : "))
s=0
for i in range (n+1):
    s+=i  
print(s)

'''
s=input("Enter any string: ")
new=""
print(s[0],end="")
for i in range (1,len(s)):
    if s[i]==s[i-1]:
        new+="*"
    else:
        new+=s[i]

print(new)
'''
#Write a function thant takes a list of integers as a parameters andd 
#returns third smallest number from the list.
def res(list):
    n=list[0]
    for i in range (list):
        if  i<n:
            n=a
    return n
    print(n)
'''