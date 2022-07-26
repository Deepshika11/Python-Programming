f1=open('fact.py','r')
print(f1.read())
f1.close()
f1=open('fact.py','a')
f1.write('Hi')
f1.close()
f1=open('fact.py','r')
print(f1.read())
f1.close()


