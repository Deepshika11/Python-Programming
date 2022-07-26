#1.
class student:
    count=0
    def __init__(self):
        self.rollNum=student.count + 1
        self.name=input("Student's name: ")
        student.count+=1
        self.stream=input("Stream:")
    def setMarks(self):
        self.marks=[]
        for i in range(1,5):
            self.marks.append(int(input("Enter the marks scored in Sub{}: ".format(i))))
    def percentage(self):
        self.percentage=(sum(self.marks)/500*100)

    def gradeGen(self):
        if self.percentage >=90:
            self.grade='A'
        elif self.percentage >=80:
            self.grade='B'
        elif self.percentage >=65:
            self.grade='C'
        elif self.percentage >=40:
            self.grade='D'
        else:
            self.grade='E'
    def display(self):
        print("Roll No:",self.rollNum)
        print("Name:",self.name)
        print("Marks Obtained:",self.marks)
        print("Overall Percentage:",self.percentage)
        print("Grade:",self.grade)
ob1=student()
ob1.setMarks()
ob1.percentage()
ob1.gradeGen()
ob1.display()




