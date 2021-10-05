class vehicle:
    def __init__(self,name):
        print("Main class:",name)

class cat_1(vehicle):
    def __init__(self):
        super().__init__("Vehicle")
        print("Category 1: land vehicle")
        print("Category 2: Water vehicle")
        print("Category 3: Air vehicle")
cat_1_obj = cat_1()
print("\n")

class By_category:
    __land_vehicle_1 = None
    __land_vehicle_2 = None
    __Water_vehicle = None
    __Air_vehicle_1 = None
    __Air_vehicle_2 = None

    def set_value(self,land_vehicle_1,land_vehicle_2,Water_vehicle,Air_vehicle_1,Air_vehicle_2):
        self.__land_vehicle_1 = land_vehicle_1
        self.__land_vehicle_2 = land_vehicle_2
        self.__Water_vehicle = Water_vehicle
        self.__Air_vehicle_1 = Air_vehicle_1
        self.__Air_vehicle_2 = Air_vehicle_2
        
    def get_land_vehicle_1(self):
        return self.__land_vehicle_1
    def get_land_vehicle_2(self):
        return self.__land_vehicle_2
    def get_Water_vehicle(self):
        return self.__Water_vehicle
    def get_Air_vehicle_1(self):
        return self.__Air_vehicle_1
    def get_Air_vehicle_2(self):
        return self.__Air_vehicle_2

class type1(By_category):
    def main_1(self):
        return self.get_land_vehicle_1()
    def main_1_1(self):
        return self.get_land_vehicle_2()

class type2(By_category):
    def main_2(self):
        return self.get_Water_vehicle()

class type3(By_category):
    def main_3(self):
        return self.get_Air_vehicle_1()
    def main_3_1(self):
        return self.get_Air_vehicle_2()

print("#Land_vehicle")
s1 = type1()
s1.set_value(4,2,0,0,0)
print('Wheels:',s1.main_1())
print("Wheels:",s1.main_1_1())

print("#Water_vehicle")
s2 = type2()
s2.set_value(0,0,0,0,0)
print("Category:",s2.main_2())

print("#Air_vehicle")
s3 = type3()
s3.set_value(0,0,0,"Powered","Unpowered")
print("Subdivision_1",s3.main_3())
print("Subdivision_1",s3.main_3_1())
print("\n")


class final_1:
    def __init__(self,name_1):
        print(name_1)

class final_2:
    def __init__(self,name_2):
        print(name_2)

class A(final_1):
    def __init__(self):
        super().__init__("land vehicle-4Wheels")
        print("car")
        super().__init__("land vehicle-2Wheels")
        print("Motor cycle")
        print("Bicycle")
        
class B(final_2):
    def __init__(self):
         super().__init__("Air vehicle-Powered")
         print("Propeller")
         print("Jet")
         print("\n")
   
A_obj = A()
B_obj = B()

print(cat_1.__mro__)
print(type1.__mro__)
print(type2.__mro__)
print(type2.__mro__)
print(A.__mro__)
print(B.__mro__)





    
    
    
    
    










                    
    
    





        
