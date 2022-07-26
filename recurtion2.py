#REVERSE
'''def rev(str):
    if str=='':
        return str
    else:
        return(str[-1]+rev(str[:-1]))
str=input("Enter any string: ")
print(rev(str))

#Palindrome
def ispalindrome(str):
    if str=='':
        return True
    elif str==1:
        return True
    elif str[0]==str[-1]and ispalindrome(str[1:-1]):
        return True
    else:
        return False
str=input("Enter the string: ")
print(ispalindrome(str))
'''
def rev(str):
    if str=='':
        return str
    else:
        return(str[::-1])
str =input("Enter your messege:")
print(rev(str))
