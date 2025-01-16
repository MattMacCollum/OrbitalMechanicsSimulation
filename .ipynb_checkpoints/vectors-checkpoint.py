import math


class Vector:
    
    def __init__(self, x=0.,y=0.,z=0.):
        self.x=x
        self.y=y
        self.z=z
        
    def __repr__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
    def __getitem__(self, item):
        
        if item == 0:
            return self.x
        elif item ==1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("3-D vector only has 3 elements; Provided index is out of bounds")
            
            
            
            
    def __add__(self, other):
        
        return Vector(self.x + other.x, 
                      self.y + other.y, 
                      self.z + other.z)
        
        
    def __sub__(self, other):
        
        return Vector(self.x - other.x, 
                      self.y - other.y, 
                      self.z - other.z)
    
    
    
    
    def __mul__(self, other):
        
        if isinstance(other, Vector):
            
            return Vector(self.x*other.x +
                          self.y*other.y +
                          self.z*other.z)
        
        elif isinstance(other, (int,float)):
            
            return Vector(self.x*other,
                          self.y*other,
                          self.z*other)
        
        else:
            raise TypeError("Second arguement must be of type Vector, int or float")
        
            
            
    def __truediv__(self, other):
        if isinstance(other, (int,float)):
            return Vector(self.x/other,
                          self.y/other,
                          self.z/other)
        
        else:
            raise TypeError("Operand must be of type int or float")
    
    
    
    
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
        
    def normalise(self):
        mag = self.get_magnitude()
        
        return Vector(self.x/mag,
                      self.y/mag,
                      self.z/mag)