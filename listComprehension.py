
data=[34,-56,-67,100, 78,89,-67,34, 100]

def fct(a):
    return a**3

result=list(map(fct, data))
print(result)


result=[]

for e in data:
    result.append(e**3)
print(result)

# List comprehension

result= [e**3 for e in data]
print(result)

result= [e**3 for e in data if e > 0]
print(result)

# Set comprehension

result= {e**3 for e in data if e > 0}
print(result)