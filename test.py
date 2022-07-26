celcius=float(input("Enter the temp in celcius degree: "))
fahrenheit=(celcius*1.8)+32
def compare(celcius,fahrenheit):
    if celcius==-40 and celcius==fahrenheit:
        return True
    else:
        return False
    
def main(): 
    print(celcius," Degree celcius is ",fahrenheit,"Degree  in fahrenheit")
    if celcius==fahrenheit:
        print("-40 gives same temperature in both celcius and fahrenheit")
    else:
        print("Enter -40 as input.")

if __name__=='__main__':
    compare=compare(celcius,fahrenheit)
    main()
