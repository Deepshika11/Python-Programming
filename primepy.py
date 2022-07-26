def prime(n):
    flag=0
    i=2
    while i<n/2:
        if n%i==0:
            flag=1
            break
        i=i+1
    return flag

def main():
    n=int(input("Enter any Integer:"))
    i=2
    while i<=n:
        if not (prime(i)):
            if n%i==0:
                print(i,'',end='')
                n=n/i
                continue
            i=i+1
if __name__=='__main__':
    main()
