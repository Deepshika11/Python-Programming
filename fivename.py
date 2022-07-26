'''
#A Write a program to print first 5 character of your name using for loop.
n=input("Your name please: ")
for i in range(len(n[0:5])):
    print(n[i])
    #OR
n=input("Your name please: ")
for i in range(5):
    print(n[i])

#C input:’institute’. Output:{‘i’:2,’u’:1,’e’:1}
def vowel_freq(str1,vowels):
    str1=str1.casefold()
    count={}.fromkeys(vowels,0)
    for character in str1:
        if character in count:
            count[character]+=1
    return count
str1=input("Enter any string: ")
vowels='aeiou'
print(vowel_freq(str1,vowels))

#D Write a program to calculate sum of the following series: 1+2+3+...+n
n=int(input("Enter any number: "))
sum=0
for i in range(1,n+1):
      sum=sum+i
print("The sum of {} number of series is {}".format(n,sum))

#E Write a function that takes a string as a parameter and returns a string 
#with every successive repetitive character replaced with a star(*). For 
#example, ‘balloon’ is returned as ‘bal*o*n’.
def repeat_char(str):
    new_str=''
    print(str[0],end="")
    for i in range(1,len(str)):
        if str[i]==str[i-1]:
            new_str+='*'
        else:
            new_str+=str[i]
    print(new_str)
str=input("Enter a string: ")
repeat_char(str)
'''

#F. Write a function thant takes a list of integers as a parameters andd 
#returns third smallest number from the list. For example, 
#input:[34,89,54,20,50,76,10,45,90] output: 34
l=[int(l) for l in input("Enter the list: ").split(",")]
print("Your List: ",l)
def thirdSmallest(l):
    l.sort()
    #n=l[0]
    
    #for i in range(len(l)):
     #   if l[i]<n:
      #      n=l[i]
       
    print("The 3rd smallest number is ",l[2:3])        

thirdSmallest(l)
 
