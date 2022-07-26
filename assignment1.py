class MyDate:
    def __init__(self):
        self.d=int(input("Enter  the Day:"))
        self.m=int(input("Enter  the Month:"))
        self.y=int(input("Enter  the Year:"))
        print("Your entered Date is:{}-{}-{}".format(self.d,self.m,self.y))
    def addDays(self):
        a=int(input("Enter how many days you want to add:"))
        newDay=self.d+a
        month=self.m
        year=self.y
        while newDay>31:
            if month in[1,3,5,7,8,10] and newDay>31:
                newDay=newDay-31
                month=month+1
            elif month in[4,6,9,11] and newDay>31:
                newDay=newDay-30
                month=month+1
            elif month==2:
                if year%4==0 and newDay>29:
                    newDay=newDay-29
                    month=month+1
                elif year%4!=0 and newDay>28:
                    newDay=newDay-28
                    month=month+1
            elif month==12 and newDay>31:
                newDay=newDay-31
                month=1
                year=year+1
        self.d=newDay
        self.m=month
        self.y=year
        print("Your New Date with added days is:{}-{}-{}".format(self.d,self.m,self.y))
    def addMonths(self):
        b=int(input("Enter how many months you want to add:"))
        newmonth=self.m+b
        day=self.d
        year=self.y
        while newmonth>12:
            if newmonth>12:
                newmonth=newmonth-12
                year=year+1
            elif newmonth in[1,3,5,7,8,10] and day>31:
                date=date-31
                newmonth=newmonth+1
                year=year+1
            elif newmonth in[4,6,9,11] and day>30:
                date=date-30
                newmonth=newmonth+1
                year=year+1
            elif newmonth==2:
                if year%4==0 and day>29:
                    day=day-29
                    month=month+1
                elif year%4!=0 and day>28:
                    day=day-28
                    month=month+1
        self.d=day
        self.m=newmonth
        self.y=year
        print("Your New Date with added months is:{}-{}-{}".format(self.d,self.m,self.y))

    def addYears(self):
        c=int(input("Enter how many years you want to add:"))
        newyear=self.y+c
        month=self.m
        day=self.d
        if month==2:
            if newyear%4==0 and day>29:
                day=29
            elif newyear%4!=0 and day>28:
                day=28
        self.d=day
        self.m=month
        self.y=newyear
        print("Your New Date with added yearsis:{}-{}-{}".format(self.d,self.m,self.y))
            
            
s1=MyDate()
s1.addDays()
s1.addMonths()
s1.addYears()
                
