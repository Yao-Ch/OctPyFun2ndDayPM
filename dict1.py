

phone={"maria":34567, 
       "yann":56789,
       "lou":76555}

print(phone, len(phone))

for n in phone:
    print(n)
    
phone["lou"]=89887      # To update an existing pair
phone["marco"]=87776    # To add a new pair

print(phone, len(phone))

if "yan" in phone:
    print(phone["yan"])
    
print(phone.keys())
print(phone.values())

phone.pop("maria")

print(phone, len(phone))

for k, v in phone.items():
    print(k,"->", v)


