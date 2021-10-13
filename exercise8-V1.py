
def addList(li1, li2):
    if len(li1) != len(li2):
        raise Exception ("The 2 lists must be of the same size")
    res=[]
    for i in range(len(li2)):
        res.append(li1[i]+li2[i])
   
    return res

    
    
l1=[1,2,3]
l2=[3,4,5]
l3=addList(l1,l2)
print (l3) # [4,6,8,10,23]

l2=[1,2,3,10,23]
l1=[3,4,5]
l3=addList(l1,l2)
print (l3) # [4,6,8,10,23]

