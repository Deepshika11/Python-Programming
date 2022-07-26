def fun():
    print('Deepshika')
fun()
p1=fun
p1()
fun.author='Avipsa'
fun.date='4th jan'
   print(fun.author)
print(p1.date)
