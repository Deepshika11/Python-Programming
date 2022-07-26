 #1.Write a Python function threesquares(m) that takes an integer m as input and returns True
#if m can be expressed as the sum of three squares and False otherwise. (If m is not positive, 
#our function should return False.)
def threesquares(m):
    if m<0:
        return False
    for i in range(m+1):
        for j in range(m+1):
            for k in range(m+1):
                n = i**2 + j**2 + k**2
                if n==m:
                    return True
                else:
                    break
    return False
m=int(input("Enter any integer: "))
print(threesquares(m))



#2.Write a function repfree(s) that takes as input a string s and checks whether any 
#character appears more than once. The function should return True if there are no repetitions 
#and False otherwise.
def repfree(s):
    count=0
    for i in range(len(s)):    
        for j in range(len(s)):
            if s[i]==s[j]:
                count+=1
        if(count>=2):
            return False
        else:
            return True    
s=input("Enter your String: ")
print(repfree(s))



#3.Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is 
#a hill or a valley, and False otherwise.
def hillvalley(l):
    if (len(l)<2):
        return False
    up_count=0
    dwn_count=0
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            up_count+=1
        elif l[i]>l[i+1]:
            dwn_count+=1
    if up_count==len(l)-1 or dwn_count==len(l)-1:
        return False
    return True
l=input("Enter your list: ")
print(hillvalley(l))
 

      
