class vehicles:
    def __init__(self,vehicle_name,company,colour,cc,capacity):
        self.vehicle_name = vehicle_name
        self.company = company
        self.colour = colour
        self.cc = cc
        self.capacity = capacity
    def myfunc(self):
        print("Vehicle name: ", self.vechicle_name)
        print("Company: ", self.comapny)
        print("Colour: ", self.colour)
        print("cc: ", self.cc)
        print("capacity: " , self.capacity)

a1 = vehicles("CAR" , "BENZ" , "BROWN" , "1000", "4\n")
a2 = vehicles("BIKE" , "BMW" , "BLACK" , "1500", "2\n")
a1 = vehicles("CYCLE" , "HERO" , "RED" , "2000", "1")
a1.myfuc()
a2.myfunc()
a3.mufunc()
