class Point: # __new__ __init__ __str__ __eq__
    def __init__(self, valx, valy): # a method
    
        self.x=valx # definition and initialization of the attribute x
        self.y=valy # definition and initialization of the attribute x
    def __str__(self):
        return f"<{self.x},{self.y}>"
    def distance(self, other):
        import math
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    def __add__(self, val):
        return Point(self.x+val, self.y+val)
    def clear(self):
        self.x=self.y=0
    def __eq__(self, other):
        return self.x==other.x and self.y ==other.y
    
p1=Point(3,4) # c1=complex(2.3, 4.5)
# 1) p1=Point.__new__()
# 2) p1.__init__(1,3)
# 3) __init__(p1, 1, 3)

print(p1.x, p1.y) # 1 3
print(p1) # <1,3>
# 1) print(str(p1))
# 2) print(p1.__str__()))

p1.x=8
# 1) p1.__setattr__("x", 8)
p1.y=10
print(p1) # <8,10>

p2=Point(5,6)
print(p2)
d=p1.distance(p2) # compute the distance between p1 and p2
print("distance is", d)
p2.x=8
p2.y=10
print(p1, p2)
if p1 == p2: # if p1.__eq__(p2):
    print("They are equal")
else:
    print("They are different")
    
p3=p2+5
# 1) p3=p2.__add__(5)

print(p3) # <13,15>

p2.clear()
print(p2) # <0,0>