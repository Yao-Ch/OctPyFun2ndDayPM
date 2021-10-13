def addList(li1, li2):
    """
    addList will add the elements .....

    Parameters
    ----------
    li1 : a list
        DESCRIPTION.
    li2 : list
        DESCRIPTION.

    Returns
    -------
    res : list
        DESCRIPTION.

    """
    li1_tmp=li1.copy() # li1_tmp=li1[:]
    li2_tmp=li2.copy()
    
    if len(li1) < len(li2):
        li1_tmp.extend([0]*(len(li2)-len(li1)))
        
    elif len(li2) < len(li1):
        li2_tmp.extend([0]*(len(li1)-len(li2)))   
        
    res=[]
    for i in range(len(li1_tmp)):
        res.append(li1_tmp[i]+li2_tmp[i])
   
    return res

    
l1=[1,2,3]
l2=[3,4,5]
l3=addList(l1,l2)
print (l3) # [4,6,8,10,23]

l1=[1,2,3,10,23]
l2=[3,4,5]
l3=addList(l1,l2)
print (l3) # [4,6,8,10,23]


l2=[1,2,3,10,23]
l1=[3,4,5]

print("l1", l1)

l3=addList(l1,l2)
print (l3) # [4,6,8,10,23]

print("l1", l1)

help(addList)

