def Merge(L,l,m,h):
    i=l
    j=m+1
    c=[]
    k=0
    while(i<=m  and j<=h):
        if L[i]<=L[j]:
            c.append(L[i])
            i+=1
        else:
            c.append(L[j])
            j+=1
    while(i<=m):
        c.append(L[i])
        i+=1
    
    while(i<=m):
        c.append(L[i])
        i+=1
    while(j<=h):
        c.append(L[j])
        j+=1

    i=l 
    k=0
    while i<=h:
        L[i]=c[k]
        i+=1
        k+=1

def MergeSort(L,l,h):
    if l<h:
        m=(l+h)//2
        MergeSort(L,l,m)
        MergeSort(L,m+1,h)
        Merge(L,l,m,h)
 
L=[21,11,10,8,55,60]
MergeSort(L,l,h)
print(L)

    

    

