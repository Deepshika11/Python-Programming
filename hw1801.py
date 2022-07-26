l1=[10,[2,5],[1,[2,3]],[5,6,[7,8]]]
l=[]
def flatten(l1,l):
    for i in l1:
        if type(i)!=list:
            l.append(i)
        else:
            flatten(i,l)
flatten(l1,l)            
print(l)
 #Shallow copy               
l=[0]*5
l1=l
l1[0]=10
print(l)
print(id(l),id(l1))
l2=[[0]*3]*4
print(l2)
l2[0][0]=10
print(l2)
#deepcopy
import copy   
l=[1,2,3,4,5]
l1=copy.deepcopy(l)
l1[0]=10
print(l)
print(l1)
l=[0 for i in range(4)]
print(id(l[0]),id(l[1]))

l=[0]*5
l=[[0 for i in range(4)] for x in range(4)]
l[0][0]=10
print(l)
print(id(l[0]))
print(id(l[1]))
