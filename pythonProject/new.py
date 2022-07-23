select={1:'biriyani',2:'kuzhmandhi',3:'Fried Rice'}
print(select)
meal=int(input("enter a meal"))
if (meal > 3) or (meal <= 0):
    print("Invalid Meal")
else:
     print("You Have Selected:" + select[meal])
