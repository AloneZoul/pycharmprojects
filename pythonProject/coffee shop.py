menu={1:'coffe',2:'tea', 3:'lime', 4:'shake'}
print(menu)
choice=int(input("Enter Your Choice"))
if(choice>4) or (choice<=0):
    print("Choice Is Invalid")
else:
    print("You Have Ordered:"+menu[choice])
