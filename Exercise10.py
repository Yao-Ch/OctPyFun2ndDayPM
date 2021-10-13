
"""
Exercise 10:
    
    Stack FILO
    
    attributes:
        maxSize: an int
        content: a list
    methods:
        push()
        pop()
        __init__()
        __str__()
        __len__()
        __eq__()
        
"""

s1=Stack(10) # a stack of 10 elements (10 is a maximum)

s1.push(45)
s1.push(56)
s1.push(78)

print(s1) # (3/10) [45,56,78]

print(len(s1)) # 3

top=s1.pop()
print(top) # 78

print(s1) # (2/10) [45,56]

top=s1.pop()
print(top) # 56

print(s1) # (1/10) [45]

top=s1.pop()
print(top) # 45

print(s1) # (0/10) []
top=s1.pop() # Exception raised