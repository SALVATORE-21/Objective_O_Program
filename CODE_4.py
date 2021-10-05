class polygon:
    __width = None
    __length = None
    __height = None
    __base = None

    def set_value(self,width,length,height,base):
        self.__width = width
        self.__length = length
        self.__height = height
        self.__base = base

    def get_width(self):
        return self.__width
    def get_length(self):
        return self.__length
    def get_height(self):
        return self.__height
    def get_base(self):
        return self.__base

class square(polygon):
    def area(self):
        return self.get_length()** 2
    def perimeter(self):
        return self.get_length()*4
                
class rectangle(polygon):
    def area(self):
        return self.get_length() *  self.get_width()
    def perimeter(self):
        return 2*(self.get_length() + self.get_width())
    
class triangle(polygon):
    def area(self):
        return 1/2 * self.get_base() * self.get_height()
    def perimeter(self):
        return self.get_length()* 3
    
class parallelogram(polygon):
    def area(self):
        return self.get_base() * self.get_height()
    def perimeter(self):
        return 2*(self.get_length() + self.get_width())
print('Polygon - 1 - SQUARE')
s1 = square()
s1.set_value(0,4,0,0)
print("Area of square:",s1.area())
print("Perimeter of square:",s1.perimeter())
print("\n")

print('Polygon - 2 - RECTANGLE')
s2 = rectangle()
s2.set_value(12,6,0,0)
print("Area of rectangle:",s2.area())
print("Perimeter of rectangle:",s2.perimeter())
print("\n")

print('Polygon - 3 - TRIANGLE')
s3 = triangle()
s3.set_value(0,0,5,10)
print("Area of equilateral triangle:",s3.area())
print("Perimeter of equilateral triangle:",s3.perimeter())
print("\n")

print('Polygon - 4 - PARALLELOGRAM')
s4 = parallelogram()
s4.set_value(2,4,6,8)
print("Area of parallelogram:",s4.area())
print("Perimeter of parallelogram:",s4.perimeter())



    

    
        
            
            
        
        
            
    
