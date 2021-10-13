

phone={"maria":[34567, 56788], 
       "yann":[56789],
       "lou":[]}

print(phone, len(phone), type(phone))

for n in phone:
    print(n)
    
phone["lou"].append(89887)     # To update an existing pair
phone["marco"]=[87776]    # To add a new pair

print(phone, len(phone))

if "yan" in phone:
    print(phone["yan"])
    
print(phone.keys())
print(phone.values())

phone.pop("maria")

print(phone, len(phone))

for k, v in phone.items():
    print(k,"->", v)


