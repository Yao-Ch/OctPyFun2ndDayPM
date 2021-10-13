data=[34,56,67,78,89,-67,100]

# def fct(a):
#     return a**3

result=list(map(lambda a: a**3, data))

print(result)

text="34;45;67;78;89"
result=text.split(";")
print(result)
result=list(map(int, result))
print(result)

data=[34,56,-67,-78,89,-67,100]

# def isPos(a):
#     return a > 0

result=list(filter(lambda a: a>0, data))
print(result)

# def isEven(a):
#     return a % 2 == 0

result=list(filter(lambda a: a%2 == 0, data))
print(result)

import functools

data=[34,56,-67,-78,89,-67,100]

# def add(a, b):
#     return a+b

result=functools.reduce(lambda a,b: a+b, data)
print(result)