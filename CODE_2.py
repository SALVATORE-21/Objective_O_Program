a1 = input("NAME_student1:")
a2 = input("NAME_student2:")
a3 = input("NAME_student3:")
a4 = input("NAME_student4:")
a5 = input("NAME_student5:")

class student:
    def __init__(self, name ,**b):
        self.name = name
        self.marks = b

    def display(self):
        print("NAME:", self.name)
        print("MARKS", self.marks)

s1 = student(a1 , Maths = 50 , Physics = 48 , Chemistry = 49 , Biology = 47)
s1.display()
s2 = student(a1 , Maths = 40 , Physics = 46 , Chemistry = 45 , Biology = 44)
s2.display()
s3 = student(a1 , Maths = 42 , Physics = 47 , Chemistry = 44 , Biology = 47)
s3.display()
s4 = student(a1 , Maths = 38 , Physics = 37 , Chemistry = 39.5 , Biology = 33)
s4.display()
s5 = student(a1 , Maths = 43 , Physics = 45 , Chemistry = 50 , Biology = 50)
s5.display()
