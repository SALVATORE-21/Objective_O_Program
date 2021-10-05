a1 = input("Holder_1: ")
a2 = input("Holder_2: ")
a3 = input("Holder_3: ")
a4 = input("Holder_4: ")
a5 = input("Holder_5: ")
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print("\n")

class Bank:
     def __init__(self,name):
        self.name = name
        self.__Acct_no = 8989
        self.__Balance = 7878
        self.__Fixed_dp = 878
        self.__loan = 988

     def display(self):
         
         print("NAME",self.name)

     def get_Acct_no(self):
         return self.__Acct_no
     def get_Balance(self):
         return self.__Balance
     def get_Fixed_dp(self):
         return self.__Fixed_dp
     def get_loan(self):
         return self.__loan

     def set_Acct_no(self,f):
         self.__Acct_no = f
     def set_Balance(self,g):
         self.__Balance = g
     def set_Fixed_dp(self,h):
         self.__Fixed_dp = h
     def set_loan(self,i):
         self.__loan = i

pin = input("Enter pin: ")
if(pin == "19ELC202"):
     s1 = Bank(a1)
     s1.display()
     s1.set_Acct_no(9876543210)
     print("Acct_no:",s1.get_Acct_no())
     s1.set_Balance(25000)
     print("Balance:",s1.get_Balance())
     s1.set_Fixed_dp(10000)
     print("Fixed_dp",s1.get_Fixed_dp())
     s1.set_loan(50000)
     print("loan:",s1.get_loan())
     print("\n")

     s2 = Bank(a2)
     s2.display()
     s2.set_Acct_no(9876543648)
     print("Acct_no:",s2.get_Acct_no())
     s2.set_Balance(5000)
     print("Balance:",s2.get_Balance())
     s2.set_Fixed_dp(1000000)
     print("Fixed_dp",s2.get_Fixed_dp())
     s2.set_loan(5000)
     print("loan:",s2.get_loan())
     print("\n")

     s3 = Bank(a3)
     s3.display()
     s3.set_Acct_no(4578943220)
     print("Acct_no:",s3.get_Acct_no())
     s3.set_Balance(6000)
     print("Balance:",s3.get_Balance())
     s3.set_Fixed_dp(720000)
     print("Fixed_dp",s3.get_Fixed_dp())
     s3.set_loan(450000)
     print("loan:",s3.get_loan())
     print("\n")

     s4 = Bank(a4)
     s4.display()
     s4.set_Acct_no(5678902535)
     print("Acct_no:",s4.get_Acct_no())
     s4.set_Balance(65000)
     print("Balance:",s4.get_Balance())
     s4.set_Fixed_dp(500000)
     print("Fixed_dp",s4.get_Fixed_dp())
     s4.set_loan(82000)
     print("loan:",s4.get_loan())
     print("\n")

     s5= Bank(a5)
     s5.display()
     s5.set_Acct_no(8903462748)
     print("Acct_no:",s5.get_Acct_no())
     s5.set_Balance(45600)
     print("Balance:",s5.get_Balance())
     s5.set_Fixed_dp(200000)
     print("Fixed_dp",s5.get_Fixed_dp())
     s5.set_loan(4100)
     print("loan:",s5.get_loan())
     print("\n")
else:
     print("Re-try again")



        
